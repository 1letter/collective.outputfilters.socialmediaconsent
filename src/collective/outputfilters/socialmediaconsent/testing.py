from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import TEST_USER_PASSWORD
from plone.testing.zope import Browser
from plone.testing.zope import WSGI_SERVER_FIXTURE

import collective.outputfilters.socialmediaconsent
import unittest


class Layer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.

        self.loadZCML(package=collective.outputfilters.socialmediaconsent)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "Products.CMFPlone:dependencies")
        applyProfile(portal, "collective.outputfilters.socialmediaconsent:default")
        portal.portal_workflow.setDefaultChain("simple_publication_workflow")


FIXTURE = Layer()

INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name="Collective.outputfilters.SocialmediaconsentLayer:IntegrationTesting",
)


FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE, WSGI_SERVER_FIXTURE),
    name="Collective.outputfilters.SocialmediaconsentLayer:FunctionalTesting",
)


ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="Collective.outputfilters.SocialmediaconsentLayer:AcceptanceTesting",
)


class BaseFunctionalTest(unittest.TestCase):

    layer = FUNCTIONAL_TESTING

    def anonymous_browser(self):
        """Browser of anonymous"""
        import transaction

        transaction.commit()
        browser = Browser(self.layer["app"])
        browser.handleErrors = False
        # browser.addHeader("Accept-Language", "de")
        return browser

    def manager_browser(self):
        """Browser with Manager authentication
        :return: Browser object with manager HTTP basic authentication header
        """
        return self._auth_browser(SITE_OWNER_NAME, SITE_OWNER_PASSWORD)

    def member_browser(self):
        """Browser with Member authentication
        :return: Browser object with member HTTP basic authentication header
        """
        return self._auth_browser(TEST_USER_NAME, TEST_USER_PASSWORD)

    def user_browser(self, login, password):
        """Browser with Member authentication
        :return: Browser object with member HTTP basic authentication header
        """
        return self._auth_browser(login, password)

    def _auth_browser(self, login, password):
        """Browser of authenticated user
        :param login: A known user login
        :param password: The password for this user
        """
        browser = self.anonymous_browser()
        browser.addHeader(
            "Authorization",
            "Basic {}:{}".format(
                login,
                password,
            ),
        )

        return browser
