from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    print("开始访问页面...")
    page.goto("http://192.168.240.128:1080/", timeout=30000)
    print("页面url：", page.url)
    page.wait_for_timeout(10000)
    print("页面标题：", page.title())
    browser.close()
    print("✅ 访问完成，没有超时")

