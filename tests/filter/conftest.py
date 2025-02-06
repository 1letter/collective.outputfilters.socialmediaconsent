from plone import api
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.textfield.value import RichTextValue
from plone.testing.zope import Browser

import pytest
import transaction


TINYMCE_MARKUP = """
<p>Markup before</p>
<p>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/video1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>
<p>Markup between</p>
<p>
<iframe width="360" height="110" src="https://youtube.com/embed/video2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>
<p>Markup after</p>
"""

TINYMCE_MARKUP_NO_PLUGIN = "<p>The answer is 42</p>"


@pytest.fixture()
def markup_without_plugin():
    from collective.outputfilters.socialmediaconsent.filter import transform_markup

    return transform_markup(TINYMCE_MARKUP_NO_PLUGIN)


@pytest.fixture()
def markup_with_plugin():
    from collective.outputfilters.socialmediaconsent.filter import transform_markup

    return transform_markup(TINYMCE_MARKUP)


@pytest.fixture()
def app(functional):
    return functional["app"]


@pytest.fixture()
def portal(functional):
    return functional["portal"]


@pytest.fixture()
def portal_with_content(app, portal, markup_with_plugin, markup_without_plugin):
    """Plone portal with initial content."""
    with api.env.adopt_roles(["Manager"]):

        portal.invokeFactory("Document", "doc1")
        portal.doc1.text = RichTextValue(
            markup_with_plugin, "text/html", "text/x-html-safe"
        )

        portal.invokeFactory("Document", "doc2")
        portal.doc2.text = RichTextValue(
            markup_without_plugin, "text/html", "text/x-html-safe"
        )

    transaction.commit()

    return portal


@pytest.fixture()
def browser_factory(app, portal_with_content):
    """Fixture returning a Browser to call the Plone site."""

    def factory():
        transaction.commit()
        # Set up browser
        browser = Browser(app)
        browser.handleErrors = False
        return browser

    return factory


@pytest.fixture()
def anon_browser(browser_factory):
    """Anonymous Browser."""
    return browser_factory()


@pytest.fixture()
def manager_browser(browser_factory):
    """Manager Browser."""
    browser = browser_factory()
    browser.addHeader(
        "Authorization",
        "Basic {}:{}".format(
            SITE_OWNER_NAME,
            SITE_OWNER_PASSWORD,
        ),
    )
    yield browser
