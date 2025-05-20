"""Setup tests for this package."""

from collective.outputfilters.socialmediaconsent.testing import INTEGRATION_TESTING
from plone import api

import unittest


class TestUtils(unittest.TestCase):
    """Test that plonetheme.carusnet is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]

        # set the registry record for tests
        valid_domains = {
            "youtube": ["youtube-nocookie.com", "youtube.com"],
            "thirdparty": ["plone.org"],
        }
        api.portal.set_registry_record(
            "collective.outputfilters.socialmediaconsent.valid_domains", valid_domains
        )

    def test_is_youtube_url(self):
        from collective.outputfilters.socialmediaconsent.utils import is_youtube_url

        checks = [
            ("https://youtube-nocookie.com", True),
            ("https://youtube.com", True),
            ("https://www.youtube-nocookie.com", True),
            ("https://www.youtube.com", True),
            ("http://youtube-nocookie.com", True),
            ("http://youtube.com", True),
            ("http://www.youtube-nocookie.com", True),
            ("http://www.youtube.com", True),
            ("http://plone.org", False),
            ("https://plone.org", False),
            ("http://www.plone.org", False),
            ("https://www.plone.org", False),
            ("https:/www.plone.org", False),
            ("www.plone.org", False),
        ]

        for url, expected in checks:
            result = is_youtube_url(url)
            self.assertTrue(
                result == expected,
                f"check for: {url} should be {expected}, bur extract_domain_from_url returns: {result}",
            )

    def test_is_thirdparty_url(self):
        from collective.outputfilters.socialmediaconsent.utils import is_thirdparty_url

        checks = [
            ("https://plone.org", True),
            ("http://plone.org", True),
            ("https://www.plone.org", True),
            ("http://www.plone.org", True),
            ("https://plone.de", False),
            ("http://www.plone.de", False),
            ("https://www.plone.de", False),
            ("https:/www.plone.org", False),
            ("www.plone.org", False),
        ]

        for url, expected in checks:
            result = is_thirdparty_url(url)
            self.assertTrue(
                result == expected,
                f"check for: {url} should be {expected}, bur extract_domain_from_url returns: {result}",
            )
