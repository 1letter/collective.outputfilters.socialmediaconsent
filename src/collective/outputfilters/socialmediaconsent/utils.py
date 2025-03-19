from urllib.parse import urlparse


def is_youtube_url(src):

    domain = urlparse(src).netloc.replace("www.", "")

    if "youtube-nocookie.com" in domain:
        return True
    if "youtube.com" in domain:
        return True

    return False
