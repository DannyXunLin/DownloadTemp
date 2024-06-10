import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    # 獲取使用者輸入的帳號和密碼
    # username = input("請輸入帳號: ")
    # password = input("請輸入密碼: ")
    username = 'B2313780'
    password = 'Auo123456***'
    page = context.new_page()
    page.goto("https://apmis.epa.gov.tw/air2/login")
    page.get_by_role("button", name="Close").click()
    page.locator("#username").click()
    page.locator("#username").fill(username)
    page.locator("#password").click()
    page.locator("#password").fill(password)

      # 檢查是否出現 captcha 驗證碼
    if page.locator("#captcha").is_visible():
        # 請使用者輸入 captcha 驗證碼
        captcha_text = input("請輸入驗證碼: ")

        # 填充 captcha 驗證碼
        page.locator("#captcha").fill(captcha_text)
        page.locator("#btnLogin").click()
    time.sleep(10)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
