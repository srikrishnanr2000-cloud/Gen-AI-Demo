import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Open YouTube
        await page.goto("https://www.youtube.com")

        # Wait for search box
        await page.wait_for_selector('input[name="search_query"]')

        # Type search text
        await page.fill('input[name="search_query"]', "ARR songs")

        # Press Enter
        await page.press('input[name="search_query"]', "Enter")

        # Wait for video results to load
        await page.wait_for_selector('ytd-video-renderer')

        # Click first video
        await page.locator('ytd-video-renderer a#video-title').first.click()

        # Wait to observe video playback
        await page.wait_for_timeout(5000)

        await browser.close()

# Run script
asyncio.run(run())