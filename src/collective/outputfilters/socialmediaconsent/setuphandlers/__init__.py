from collective.outputfilters.socialmediaconsent import CUSTOM_ATTRIBUTES
from collective.outputfilters.socialmediaconsent import PACKAGE_NAME
from collective.outputfilters.socialmediaconsent import VALID_TAGS
from plone.base.interfaces import INonInstallable
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles:
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            f"{PACKAGE_NAME}:uninstall",
        ]


def post_install(context):

    set_registry_records()


def set_registry_records():

    registry = getUtility(IRegistry)

    record = registry.records.get("plone.valid_tags")
    for valid_tag in VALID_TAGS:
        if valid_tag not in record.value:
            record.value.append(valid_tag)

    record = registry.records.get("plone.custom_attributes")
    for custom_attribute in CUSTOM_ATTRIBUTES:
        if custom_attribute not in record.value:
            record.value.append(custom_attribute)
