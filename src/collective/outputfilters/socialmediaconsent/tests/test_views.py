from collective.outputfilters.socialmediaconsent.interfaces import ICookieSettingsView
from collective.outputfilters.socialmediaconsent.testing import INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getMultiAdapter

import unittest


class TestCookieSettingsViewIntegrationTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_cookie_settings_view_is_registered(self):
        # only for portal root registered
        view = getMultiAdapter(
            (self.portal, self.portal.REQUEST), name="cos-cookie-settings"
        )
        self.assertTrue(view.__name__ == "cos-cookie-settings")

        self.assertTrue(ICookieSettingsView.providedBy(view))
