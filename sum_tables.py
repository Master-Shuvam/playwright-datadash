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
            url = f"https://sanand0.github.io/tdsdata/table/?seed={s}"
            await page.goto(url)
            await page.wait_for_load_state("networkidle")

            tables = await page.locator("table").all_inner_texts()

            for t in tables:
                nums = re.findall(r"-?\d+\.?\d*", t)
                total += sum(float(n) for n in nums)

        await browser.close()

    print("TOTAL:", total)

asyncio.run(main())
