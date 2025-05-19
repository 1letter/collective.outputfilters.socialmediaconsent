from bs4 import BeautifulSoup
from collective.outputfilters.socialmediaconsent.interfaces import (
    ISocialMediaConsentFilter,
)
from collective.outputfilters.socialmediaconsent.utils import is_thirdparty_url
from collective.outputfilters.socialmediaconsent.utils import is_youtube_url
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from uuid import uuid1
from zope.interface import implementer

import json


@implementer(ISocialMediaConsentFilter)
class SocialMediaConsentFilter:
    """Convert markup with external social media content to dsgvo ready markup."""

    order = 2000

    def is_enabled(self):
        return self.context is not None

    def __init__(self, context=None, request=None):
        self.context = context
        self.request = request

    def __call__(self, data):

        return self.transform_markup(data)

    def transform_markup(self, html):
        # replace elements with placeholder
        """
        Youtube iframe:
        <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/PivpCKEiQOQ?si=-r--c7rnSixOlmLm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        """

        soup = BeautifulSoup(html, "html.parser")

        # transform all youtube iframes
        elements = soup.find_all("iframe", src=is_youtube_url)
        for element in elements:

            snippet = ViewPageTemplateFile("browser/templates/snippet-youtube.pt")(
                self,
                cos=json.dumps({"markup": str(element), "consent": "youtube"}),
                id=uuid1(),
            )

            tag = BeautifulSoup(snippet, "html.parser")

            element.replace_with(tag)

        # transform all third-party iframes
        elements = soup.find_all("iframe", src=is_thirdparty_url)
        for element in elements:

            snippet = ViewPageTemplateFile("browser/templates/snippet-thirdparty.pt")(
                self,
                cos=json.dumps({"markup": str(element), "consent": "third_party"}),
                id=uuid1(),
            )

            tag = BeautifulSoup(snippet, "html.parser")

            element.replace_with(tag)

        return str(soup)
