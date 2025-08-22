# Contributing to Watermark Studio Extension

Thank you for your interest in contributing to the Watermark Studio Extension! This document provides guidelines for contributing to this project.

## 🤝 How to Contribute

### Reporting Issues

If you find a bug or have a feature request:

1. **Search existing issues** first to avoid duplicates
2. **Use the issue templates** if available
3. **Provide detailed information**:
   - Steps to reproduce the bug
   - Expected vs actual behavior
   - Screenshots/videos if applicable
   - System information (OS, WebUI version, extension version)

### Submitting Changes

1. **Fork the repository**
2. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** following our coding standards
4. **Test your changes** thoroughly
5. **Update documentation** if needed
6. **Submit a pull request**

## 🧪 Development Setup

### Prerequisites

- Python 3.8+
- AUTOMATIC1111 Stable Diffusion WebUI
- Git

### Local Development

1. Clone your fork:
   ```bash
   git clone https://github.com/your-username/sd-webui-watermark-studio.git
   ```

2. Install in development mode:
   ```bash
   cd sd-webui-watermark-studio
   python install.py
   ```

3. Run tests:
   ```bash
   python test_extension.py
   ```

## 📝 Coding Standards

### Python Code

- Follow **PEP 8** style guidelines
- Use **type hints** where appropriate
- Write **docstrings** for all functions and classes
- Keep functions **small and focused**
- Use **meaningful variable names**

### JavaScript Code

- Follow **modern JavaScript** standards
- Use **const/let** instead of var
- Add **JSDoc comments** for functions
- Use **semantic naming**

### CSS Code

- Use **BEM methodology** for class naming
- Group related styles together
- Add comments for complex selectors
- Ensure **mobile responsiveness**

## 🔍 Code Review Process

1. All submissions require **code review**
2. Maintainers will review PRs within **48 hours**
3. Address **feedback promptly**
4. Ensure **all tests pass** before merge
5. **Squash commits** if requested

## 📚 Documentation

- Update README.md for user-facing changes
- Update CHANGELOG.md following semantic versioning
- Add inline code comments for complex logic
- Include examples in docstrings

## 🎯 Areas for Contribution

We especially welcome contributions in these areas:

### High Priority
- **Image watermarking** functionality
- **Batch processing** improvements
- **Template system** implementation
- **Performance optimizations**

### Medium Priority
- **Additional positioning options**
- **Real-time preview** feature
- **Export format options**
- **Accessibility improvements**

### Low Priority
- **UI/UX enhancements**
- **Additional language support**
- **Integration with other extensions**

## ⚡ Quick Start Checklist

- [ ] Fork the repository
- [ ] Create a feature branch
- [ ] Make minimal, focused changes
- [ ] Add/update tests as needed
- [ ] Update documentation
- [ ] Test thoroughly
- [ ] Submit pull request with clear description

## 💬 Getting Help

- **GitHub Discussions** for questions and ideas
- **GitHub Issues** for bug reports
- **Code comments** for implementation questions

## 📄 License

By contributing, you agree that your contributions will be licensed under the same [Unlicense](LICENSE) as the project.

---

Thank you for contributing to make Watermark Studio Extension better for everyone! 🎉