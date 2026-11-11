from playwright.sync_api import Page, expect

BASE_URL = "http://192.168.240.128:8081"

def test_ruoyi_login(page: Page):
    page.goto(BASE_URL)
    expect(page).to_have_title("若依管理系统")

