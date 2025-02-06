import pytest


@pytest.mark.parametrize(
    "domain, expected",
    [
        ("youtube-nocookie.com", True),
        ("youtube.com", True),
        ("www.youtube-nocookie.com", True),
        ("www.youtube.com", True),
        ("youtube-nocookie.de", False),
        ("youtube.de", False),
        ("plone.org", False),
        ("test.local", False),
    ],
)
def test_iframe_youtube(domain, expected):
    from collective.outputfilters.socialmediaconsent.utils import iframe_youtube

    assert iframe_youtube(domain) is expected


@pytest.mark.parametrize(
    "markup, expected",
    [
        ("https://youtube-nocookie.com", "youtube-nocookie.com"),
        ("https://youtube.com", "youtube.com"),
        ("https://www.youtube-nocookie.com", "youtube-nocookie.com"),
        ("https://www.youtube.com", "youtube.com"),
        ("http://youtube-nocookie.com", "youtube-nocookie.com"),
        ("http://youtube.com", "youtube.com"),
        ("http://www.youtube-nocookie.com", "youtube-nocookie.com"),
        ("http://www.youtube.com", "youtube.com"),
        ("http://plone.org", "plone.org"),
        ("https://plone.org", "plone.org"),
        ("http://www.plone.org", "plone.org"),
        ("https://www.plone.org", "plone.org"),
    ],
)
def test_extract_domain(markup, expected):
    from collective.outputfilters.socialmediaconsent.utils import extract_domain

    assert extract_domain(markup) == expected
