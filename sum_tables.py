import asyncio
import re
from playwright.async_api import async_playwright

seeds = range(66, 76)

async def main():
    total = 0

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        for s in seeds:
            url = f"https://sanand0.github.io/tdsdata/js_table/?seed={s}"
            await page.goto(url)

            # wait for JS table to render
            await page.wait_for_selector("table")

            text = await page.inner_text("body")

            numbers = re.findall(r"-?\d+\.?\d*", text)
            total += sum(float(n) for n in numbers)

        await browser.close()

    print(f"TOTAL={total}")

asyncio.run(main())
