import re


def extract_domain(url):
    # Define a regular expression pattern for extracting the domain
    pattern = r"(https?://)?(www\d?\.)?(?P<domain>[\w\.-]+\.\w+)(/\S*)?"
    # Use re.match to search for the pattern at the beginning of the URL
    match = re.match(pattern, url)
    # Check if a match is found
    if match:
        # Extract the domain from the named group "domain"
        domain = match.group("domain")
        return domain
    else:
        return None


def iframe_youtube(src):

    domain = extract_domain(src)

    if "youtube-nocookie.com" in domain:
        return True
    if "youtube.com" in domain:
        return True
    return False
