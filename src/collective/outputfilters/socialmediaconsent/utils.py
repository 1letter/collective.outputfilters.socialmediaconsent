from collective.outputfilters.socialmediaconsent import CUSTOM_ATTRIBUTES
from collective.outputfilters.socialmediaconsent import NASTY_TAGS
from collective.outputfilters.socialmediaconsent import VALID_TAGS
from plone import api
from plone.registry.interfaces import IRegistry
from urllib.parse import urlparse
from zope.component import getUtility

import json


def is_youtube_url(src):

    valid_domains = api.portal.get_registry_record(
        "collective.outputfilters.socialmediaconsent.valid_domains"
    ).get("youtube")

    domain = urlparse(src).netloc.replace("www.", "")

    if domain in valid_domains:
        return True

    return False


def is_thirdparty_url(src):

    valid_domains = api.portal.get_registry_record(
        "collective.outputfilters.socialmediaconsent.valid_domains"
    ).get("thirdparty")

    domain = urlparse(src).netloc.replace("www.", "")

    if domain in valid_domains:
        return True

    return False


def set_registry_records():

    registry = getUtility(IRegistry)

    values = registry.records.get("plone.valid_tags").value
    for valid_tag in VALID_TAGS:
        values.append(valid_tag)
    values = sorted(list(set(values)))
    registry.records["plone.valid_tags"].value = values

    values = registry.records.get("plone.custom_attributes").value
    for custom_attribute in CUSTOM_ATTRIBUTES:
        values.append(custom_attribute)
    values = sorted(list(set(values)))
    registry.records["plone.custom_attributes"].value = values

    values = registry.records.get("plone.nasty_tags").value
    for nasty_tag in NASTY_TAGS:
        values.remove(nasty_tag)
    values = sorted(list(set(values)))
    registry.records["plone.nasty_tags"].value = values

    values = registry.records.get("plone.other_settings").value
    values = json.loads(values)
    values.update(
        {
            "sandbox_iframes": True,
            "sandbox_iframes_exclusions": [
                "youtube.com",
                "youtu.be",
                "vimeo.com",
                "player.vimeo.com",
                "youtube-nocookie.com",
            ],
        }
    )
    values = json.dumps(values)
    registry.records["plone.other_settings"].value = values
