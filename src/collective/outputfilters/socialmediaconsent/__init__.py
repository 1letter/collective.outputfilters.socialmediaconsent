"""Init and utils."""

from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "collective.outputfilters.socialmediaconsent"

VALID_TAGS = ["input", "label", "iframe", "script", "noscript", "style"]

NASTY_TAGS = ["script", "style"]

CUSTOM_ATTRIBUTES = [
    "width",
    "height",
    "src",
    "title",
    "frameborder",
    "allow",
    "sandbox",
    "referrerpolicy",
    "allowfullscreen",
    "data-cos",
]

_ = MessageFactory(PACKAGE_NAME)

logger = logging.getLogger(PACKAGE_NAME)
