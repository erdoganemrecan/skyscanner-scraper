import asyncio
from playwright.async_api import async_playwright

async def fetch_flights(from_code, to_code, date):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        search_url = f"https://www.skyscanner.com/transport/flights/{from_code.lower()}/{to_code.lower()}/{date.replace('/', '')}/"
        await page.goto(search_url)
        await page.wait_for_timeout(10000)
        flights = await page.query_selector_all(".FlightsTicket_module__ticketBody___2ARjY")
        results = []
        for flight in flights[:3]:
            text = await flight.inner_text()
            results.append({"raw_text": text})
        await browser.close()
        return results