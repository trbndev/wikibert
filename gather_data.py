import wikipediaapi
import os
import re


MAX_DEPTH = 2


def get_wiki_page(title):
    wiki_wiki = wikipediaapi.Wikipedia("TechNova (admin@technova.org)", "en")
    page = wiki_wiki.page(title)
    return page


articles = {}


def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', "_", filename)


def gather_pages_recusively(page, depth=0):
    if depth > MAX_DEPTH:
        return

    if page.title in articles:
        return

    articles[page.title] = page.text

    # Create file for page in data folder
    sanitized_title = sanitize_filename(page.title)
    with open(f"data/{sanitized_title}.txt", "w", encoding="utf-8") as f:
        f.write(page.text)

    for link in page.links:
        gather_pages_recusively(page.links[link], depth + 1)


def prepare_data_folder():
    if not os.path.exists("data"):
        os.makedirs("data")


def main():
    prepare_data_folder()

    title = "Python (programming language)"
    page = get_wiki_page(title)

    gather_pages_recusively(page)

    print(articles.keys())


if __name__ == "__main__":
    main()
