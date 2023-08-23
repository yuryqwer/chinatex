import time
import base64
import asyncio
from pyppeteer import launch

WIDTH, HEIGHT = 900, 1080


async def main():
    browser = await launch(
        headless=False,
        ignoreHTTPSErrors=True, 
        args=["--disable-infobars"]
    )
    try:
        page = await browser.newPage()
        await page.setViewport({"width": WIDTH, "height": HEIGHT})
        await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
        await page.goto("https://inv-veri.chinatax.gov.cn/")
        await page.waitForSelector("#fpdm")
        await page.type("#fpdm", "032002200511")
        await page.type("#fphm", "98170237")
        await page.click("#pageshow > div.upgrade > a")
        await page.click("#pageshow > div.teachyou > a.teachyou_close")
        while True:
            filename = input("Please tag the picture: ")
            if filename == "": # picture cannot be recognized
                await page.click("#yzm_img")
                print("Cannot recognize, change another one.")
                continue
            if not "_" in filename:
                print("Wrong format!")
                continue
            color, text = filename.split("_")
            if len(color) != len(text):
                print("Wrong format!")
                continue
            if not all(i in (j for j in "YRBU") for i in color):
                print("Wrong format!")
                continue
            img = await page.J("#yzm_img")
            img = await img.getProperty("src")
            with open(f"./real_captcha/{filename}_{int(time.time())}.png", "wb") as f:
                f.write(base64.b64decode(img.toString()[31:]))
            await page.click("#yzm_img")
    finally:
        await browser.close()


asyncio.get_event_loop().run_until_complete(main())