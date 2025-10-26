from playwright.sync_api import sync_playwright, Page, expect
import os

def run_verification(page: Page):
    # Get the absolute path to the HTML file
    file_path = os.path.abspath('index.html')
    # Use 'file://' to open the local HTML file
    page.goto(f'file://{file_path}')

    # The navigation link is hidden on mobile, so we directly show the page.
    page.evaluate("""
        document.querySelectorAll('.page').forEach(page => page.classList.remove('active'));
        const targetPage = document.getElementById('services-page');
        if (targetPage) targetPage.classList.add('active');
    """)

    # The button is inside the ".call-to-action-box"
    cta_box = page.locator(".call-to-action-box")

    # Expect the CTA box to be visible
    expect(cta_box).to_be_visible()

    # Take a screenshot of just the "Book A Reading Today!" section
    cta_box.screenshot(path="jules-scratch/verification/whatsapp_button_mobile_fixed.png")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    # Set a mobile viewport
    page = browser.new_page(viewport={'width': 375, 'height': 812})
    run_verification(page)
    browser.close()
