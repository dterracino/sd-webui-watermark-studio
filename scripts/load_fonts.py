from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Iterable, Optional

# Default folder (can be overridden by passing a different one to load_fonts)
DEFAULT_FONTS_FOLDER = "../assets/fonts"


def load_fonts(folder: str | None = None) -> Dict[str, str]:
    """
    Scan the given folder (top-level only) for .ttf files, extract each font's
    human-friendly name, and return a dict mapping {font_name: filename}.

    - If `folder` is None, DEFAULT_FONTS_FOLDER is used.
    - `folder` may be absolute or relative. Relative paths are resolved from the
      script's directory (where this file lives). If __file__ is unavailable
      (e.g., interactive), falls back to the current working directory.
    - If multiple files resolve to the same name, they are disambiguated with
      suffixes " (2)", " (3)", etc.

    Dependencies (optional but recommended):
      - fonttools  (best metadata via 'name' table)
      - Pillow     (fallback for family/style)
    """
    folder = folder or DEFAULT_FONTS_FOLDER

    base = Path(folder)
    if not base.is_absolute():
        base = (_get_script_dir() / base).resolve()

    if not base.exists() or not base.is_dir():
        raise FileNotFoundError(f"Fonts folder not found or not a directory: {base}")

    fonts_map: Dict[str, str] = {}
    seen: Dict[str, int] = {}

    for path in sorted(base.iterdir()):
        if not path.is_file() or path.suffix.lower() != ".ttf":
            continue

        font_name = (
            _try_name_with_fonttools(path)
            or _try_name_with_pillow(path)
            or path.stem
        )

        unique_name = _dedupe_name(font_name, seen)
        fonts_map[unique_name] = path.name  # filename only, per spec

    return fonts_map


# ---------- Helpers ----------

def _get_script_dir() -> Path:
    """Return the directory of this script, or CWD if __file__ is unavailable."""
    try:
        return Path(__file__).resolve().parent
    except NameError:
        return Path.cwd().resolve()


def _dedupe_name(name: str, seen: Dict[str, int]) -> str:
    """Ensure name uniqueness by appending ' (n)' when duplicates occur."""
    count = seen.get(name, 0) + 1
    seen[name] = count
    return name if count == 1 else f"{name} ({count})"


def _try_name_with_fonttools(path: Path) -> Optional[str]:
    """
    Best-effort extraction using fontTools:
    Prefer Full Font Name (nameID=4), else Family (nameID=1).
    Uses getattr-safe access so static type checkers don't complain.
    """
    try:
        from fontTools.ttLib import TTFont  # type: ignore
        tt = TTFont(str(path), lazy=True)
        name_tbl: Any = tt["name"]

        # First pass: try preferred encodings for Full/Family
        for name_id in (4, 1):  # Full name > Family
            for rec in _iter_name_records(name_tbl, name_id):
                s = _safe_name_string(rec)
                if s:
                    return s

        # Fallback: any record with nameID 4 or 1
        for rec in _iter_name_records(name_tbl, None):
            if getattr(rec, "nameID", None) in (4, 1):
                s = _safe_name_string(rec)
                if s:
                    return s
    except Exception:
        pass
    return None


def _iter_name_records(name_tbl: Any, name_id: Optional[int]) -> Iterable[Any]:
    """
    Safely iterate name records from the name table, optionally filtering by name_id.
    Yields Windows Unicode BMP (3,1), Windows UCS-4 (3,10), Mac Roman (1,0) first.
    """
    names = list(getattr(name_tbl, "names", []) or [])
    if not names:
        return []

    preferred, others = [], []
    for rec in names:
        pid = getattr(rec, "platformID", None)
        enc = getattr(rec, "platEncID", None)
        nid = getattr(rec, "nameID", None)
        if name_id is not None and nid != name_id:
            continue
        key = (pid, enc)
        (preferred if key in ((3, 1), (3, 10), (1, 0)) else others).append(rec)

    for rec in preferred:
        yield rec
    for rec in others:
        yield rec


def _safe_name_string(rec: Any) -> Optional[str]:
    """Safely decode a name record to a Python string, or return None."""
    try:
        s = rec.toUnicode().strip()  # type: ignore[attr-defined]
        return s or None
    except Exception:
        try:
            raw = getattr(rec, "string", None)
            if isinstance(raw, bytes):
                pid = getattr(rec, "platformID", None)
                enc = getattr(rec, "platEncID", None)
                codec = _encoding_for_record(pid, enc)
                s = raw.decode(codec, errors="ignore").strip()
            else:
                s = str(raw).strip() if raw is not None else ""
            return s or None
        except Exception:
            return None


def _encoding_for_record(platform_id: Optional[int], enc_id: Optional[int]) -> str:
    if platform_id == 3:  # Windows
        if enc_id in (1, 10):
            return "utf-16-be"
    if platform_id == 1:  # Macintosh
        return "mac_roman"
    return "utf-8"


def _try_name_with_pillow(path: Path) -> Optional[str]:
    """Fallback extraction using Pillow. Returns 'Family' or 'Family Style'."""
    try:
        from PIL import ImageFont  # type: ignore
        font = ImageFont.truetype(str(path), size=16)
        family, style = font.getname()
        family = (family or "").strip()
        style = (style or "").strip()
        if family and style and style.lower() != "regular":
            return f"{family} {style}"
        return family or None
    except Exception:
        return None


# ---------- Example CLI usage ----------
if __name__ == "__main__":
    fonts = load_fonts()  # uses DEFAULT_FONTS_FOLDER by default
    for k, v in fonts.items():
        print(f"{k} -> {v}")
