from bs4 import BeautifulSoup
from collective.outputfilters.socialmediaconsent.interfaces import (
    ISocialMediaConsentFilter,
)
from collective.outputfilters.socialmediaconsent.utils import iframe_youtube
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implementer

import json


def transform_markup(html, filter=None):
    # replace elements with placeholder
    """
    Youtube iframe:
    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/PivpCKEiQOQ?si=-r--c7rnSixOlmLm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    """
    if not filter:
        return html

    soup = BeautifulSoup(html, "html.parser")
    elements = soup.find_all("iframe", src=iframe_youtube)
    for element in elements:
        snippet = ViewPageTemplateFile("snippet.pt")(
            filter, data_html=json.dumps({"html": str(element)})
        )
        tag = BeautifulSoup(snippet, "html.parser")
        element.replace_with(tag)

    return str(soup)


@implementer(ISocialMediaConsentFilter)
class SocialMediaConsentFilter:
    """Convert markup with external social media content to dsgvo ready markup."""

    order = 1954

    def is_enabled(self):
        return self.context is not None

    def __init__(self, context=None, request=None):
        self.context = context
        self.request = request

    def __call__(self, data):

        return transform_markup(data, self)
