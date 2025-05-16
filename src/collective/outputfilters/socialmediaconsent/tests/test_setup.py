"""Setup tests for this package."""

from collective.outputfilters.socialmediaconsent import PACKAGE_NAME
from collective.outputfilters.socialmediaconsent.testing import INTEGRATION_TESTING
from plone.base.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.carusnet is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if plonetheme.carusnet is installed."""
        self.assertTrue(self.installer.is_product_installed(PACKAGE_NAME))

    def test_browserlayer(self):
        """Test that IPlonethemeCarusnetLayer is registered."""
        from collective.outputfilters.socialmediaconsent.interfaces import IBrowserLayer
        from plone.browserlayer import utils

        self.assertIn(IBrowserLayer, utils.registered_layers())

    def test_profile_last_version(self):
        """Test latest version of default profile."""

        version = self.portal.portal_setup.getLastVersionForProfile(
            f"{PACKAGE_NAME}:default"
        )
        profile_last_version = None
        if version:
            profile_last_version = version[0]

        self.assertEqual(profile_last_version, "1000")

    def test_registry_values(self):
        from collective.outputfilters.socialmediaconsent import CUSTOM_ATTRIBUTES
        from collective.outputfilters.socialmediaconsent import VALID_TAGS
        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility

        registry = getUtility(IRegistry)

        record = registry.records.get("plone.valid_tags")
        for valid_tag in VALID_TAGS:
            self.assertIn(
                valid_tag, record.value, f"{valid_tag} should be in 'plone.valid_tags'"
            )

        record = registry.records.get("plone.custom_attributes")
        for valid_tag in CUSTOM_ATTRIBUTES:
            self.assertIn(
                valid_tag,
                record.value,
                f"{valid_tag} should be in 'plone.custom_attributes'",
            )

    def test_bundle_registration(self):
        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility

        registry = getUtility(IRegistry)

        record = registry.records.get(
            "plone.bundles/collective.outputfilters.socialmediaconsent.jscompilation"
        )

        self.assertTrue(
            "collective.outputfilters.socialmediaconsent.min.js" in record.value
        )


class TestUninstall(unittest.TestCase):
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        self.installer.uninstall_product(PACKAGE_NAME)

    def test_product_uninstalled(self):
        """Test if plonetheme.carusnet is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(PACKAGE_NAME))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeCarusnetLayer is removed."""
        from collective.outputfilters.socialmediaconsent.interfaces import IBrowserLayer
        from plone.browserlayer import utils

        self.assertNotIn(IBrowserLayer, utils.registered_layers())
