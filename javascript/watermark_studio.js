/**
 * Watermark Studio Extension JavaScript
 * 
 * This file provides client-side functionality for the Watermark Studio extension.
 */

(function() {
    'use strict';

    // Extension initialization
    console.log('[Watermark Studio] JavaScript module loaded');

    // Wait for the page to be fully loaded
    document.addEventListener('DOMContentLoaded', function() {
        initializeWatermarkStudio();
    });

    function initializeWatermarkStudio() {
        console.log('[Watermark Studio] Initializing UI enhancements');
        
        // Add keyboard shortcuts
        addKeyboardShortcuts();
        
        // Enhance UI elements
        enhanceUIElements();
        
        // Add tooltips
        addTooltips();
    }

    function addKeyboardShortcuts() {
        document.addEventListener('keydown', function(e) {
            // Ctrl+Shift+W to toggle watermark studio accordion
            if (e.ctrlKey && e.shiftKey && e.key === 'W') {
                e.preventDefault();
                toggleWatermarkStudioAccordion();
            }
        });
    }

    function toggleWatermarkStudioAccordion() {
        // Look for watermark studio accordions and toggle them
        const accordions = document.querySelectorAll('[id*="watermark_studio_"]');
        accordions.forEach(accordion => {
            if (accordion.tagName === 'BUTTON' && accordion.textContent.includes('Watermark Studio')) {
                accordion.click();
            }
        });
    }

    function enhanceUIElements() {
        // Add visual feedback for watermark settings
        setTimeout(() => {
            const textInputs = document.querySelectorAll('[id*="watermark_studio_text_"]');
            textInputs.forEach(input => {
                if (input.tagName === 'TEXTAREA' || input.tagName === 'INPUT') {
                    input.addEventListener('input', function() {
                        if (this.value.trim()) {
                            this.style.borderColor = '#28a745';
                        } else {
                            this.style.borderColor = '#dc3545';
                        }
                    });
                }
            });
        }, 1000);

        // Add preview on hover for position dropdown
        setTimeout(() => {
            const positionDropdowns = document.querySelectorAll('[id*="watermark_studio_position_"]');
            positionDropdowns.forEach(dropdown => {
                dropdown.addEventListener('change', function() {
                    showPositionPreview(this.value);
                });
            });
        }, 1000);
    }

    function showPositionPreview(position) {
        // Create a temporary visual indicator for watermark position
        const preview = document.createElement('div');
        preview.innerHTML = `<span style="
            position: fixed; 
            top: 50%; 
            left: 50%; 
            transform: translate(-50%, -50%);
            background: rgba(0,0,0,0.8); 
            color: white; 
            padding: 10px 15px; 
            border-radius: 5px;
            z-index: 10000;
            font-size: 14px;
        ">Watermark position: ${position}</span>`;
        
        document.body.appendChild(preview);
        
        setTimeout(() => {
            document.body.removeChild(preview);
        }, 2000);
    }

    function addTooltips() {
        const tooltipData = {
            'watermark_studio_enabled': 'Enable or disable watermarking for generated images',
            'watermark_studio_text': 'Enter the text that will appear as a watermark',
            'watermark_studio_opacity': 'Control how transparent the watermark appears (0.1 = very transparent, 1.0 = opaque)',
            'watermark_studio_position': 'Choose where on the image the watermark will be placed',
            'watermark_studio_auto': 'Automatically apply watermark to all generated images without manual intervention'
        };

        setTimeout(() => {
            Object.keys(tooltipData).forEach(id => {
                const elements = document.querySelectorAll(`[id*="${id}"]`);
                elements.forEach(element => {
                    if (!element.title) {
                        element.title = tooltipData[id];
                    }
                });
            });
        }, 2000);
    }

    // Custom tab enhancements
    function enhanceCustomTab() {
        // Add drag and drop functionality for image upload
        const imageInputs = document.querySelectorAll('[id*="watermark_studio_input_image"]');
        imageInputs.forEach(input => {
            addDragDropFunctionality(input);
        });
    }

    function addDragDropFunctionality(element) {
        element.addEventListener('dragover', function(e) {
            e.preventDefault();
            this.style.backgroundColor = '#e3f2fd';
        });

        element.addEventListener('dragleave', function(e) {
            e.preventDefault();
            this.style.backgroundColor = '';
        });

        element.addEventListener('drop', function(e) {
            e.preventDefault();
            this.style.backgroundColor = '';
            // Handle file drop (this would need integration with Gradio's file handling)
            console.log('[Watermark Studio] Files dropped:', e.dataTransfer.files);
        });
    }

    // Export functions for potential external use
    window.WatermarkStudio = {
        toggleAccordion: toggleWatermarkStudioAccordion,
        showPositionPreview: showPositionPreview
    };

    // Re-initialize when new content is loaded (for dynamic updates)
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
                // Check if watermark studio elements were added
                mutation.addedNodes.forEach(node => {
                    if (node.nodeType === 1 && node.querySelector && 
                        node.querySelector('[id*="watermark_studio"]')) {
                        setTimeout(enhanceUIElements, 500);
                        setTimeout(enhanceCustomTab, 500);
                    }
                });
            }
        });
    });

    observer.observe(document.body, {
        childList: true,
        subtree: true
    });

})();

console.log('[Watermark Studio] JavaScript enhancements loaded');