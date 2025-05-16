from collective.outputfilters.socialmediaconsent import PACKAGE_NAME
from collective.outputfilters.socialmediaconsent.utils import set_registry_records
from plone.base.interfaces import INonInstallable
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
