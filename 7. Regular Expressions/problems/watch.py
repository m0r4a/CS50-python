import re


def main():
    print(parse(input("HTML: ")))


def parse(html):
    if youtube_url := get_url(html):
        return re.sub(r"https?://(?:www)?\.?youtube.com/embed", "https://youtu.be", youtube_url)
    else:
        return None


def get_url(html):
    pattern = r'^<iframe.*src=\"(.+youtu[^ ]+)\"[^.]'
    if match := re.search(pattern, html):
        return match.group(1)
    else:
        return False


if __name__ == "__main__":
    main()
