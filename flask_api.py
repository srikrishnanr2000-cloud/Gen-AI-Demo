from flask import Flask, jsonify
import asyncio
from playwright.async_api import async_playwright

app = Flask(__name__)

async def youtube_automation():
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)

        # Open new page
        page = await browser.new_page()

        # Open YouTube
        await page.goto("https://www.youtube.com")

        # Wait for search box
        await page.wait_for_selector('input[name="search_query"]')

        # Search ARR songs
        await page.fill('input[name="search_query"]', "ARR songs")

        # Press Enter
        await page.press('input[name="search_query"]', "Enter")

        # Wait for results
        await page.wait_for_selector('ytd-video-renderer')

        # Click first video
        await page.locator('ytd-video-renderer a#video-title').first.click()

        # Wait for 5 seconds
        await page.wait_for_timeout(5000)

        # Close browser
        await browser.close()


@app.route('/')
def home():
    return "Flask Playwright Automation Running"


@app.route('/run-playwright')
def run_playwright():
    asyncio.run(youtube_automation())
    return jsonify({
        "status": "success",
        "message": "YouTube automation completed"
    })


if __name__ == '__main__':
    app.run(debug=True)