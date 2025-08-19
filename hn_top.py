import time
import requests

# Hacker NewsのトップストーリーIDを取得
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"


def main():
    # トップストーリーID一覧を取得
    response = requests.get(TOP_STORIES_URL)
    story_ids = response.json()

    # 最初の30件を処理
    for story_id in story_ids[:30]:
        story = requests.get(ITEM_URL.format(story_id)).json()

        title = story.get("title")
        link = story.get("url")

        # URLがない場合はNoneにする
        print({"title": title, "link": link if link else None})

        time.sleep(1)  # サーバーへのアクセス間隔を１秒空ける


if __name__ == "__main__":
    main()
