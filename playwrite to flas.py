from flask import Flask, jsonify
from playwright.sync_api import sync_playwright

app = Flask(__name__)

@app.route('/get-news', methods=['GET'])
def get_news():
    news_list = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        try:
            page.goto("https://www.bing.com", timeout=60000)
            search_input = page.locator('//*[@id="sb_form_q"]')
            search_input.wait_for(timeout=10000)
            search_input.fill("South Africa vs Australia latest news")
            search_input.press("Enter")

            page.wait_for_selector("li.nth-child(3) h2 a", timeout=15000)
            headlines = page.locator("li.b_algo h2 a")
            count = headlines.count()

            for i in range(min(5, count)):
                title = headlines.nth(i).text_content().strip()
                url = headlines.nth(i).get_attribute("href")
                news_list.append({"title": title, "url": url})

        except Exception as e:
            return jsonify({"error": "Failed to fetch news", "details": str(e)})

        finally:
            browser.close()

    return jsonify({"news": news_list})


if __name__ == '__main__':
    app.run(debug=True)
