from collective.outputfilters.socialmediaconsent.testing import BaseFunctionalTest
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.textfield.value import RichTextValue


TINYMCE_MARKUP = """
<p>Markup before</p>
<p>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/video1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>
<p>Markup between</p>
<p>
<p>
<iframe src="https://www.youtube-nocookie.com/embed/yCMI5RHQMYc?si=8E_T2wHKYOAWXFR8" height="315" width="560" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen="allowfullscreen"></iframe>
</p>
<p>Markup after</p>
"""

TINYMCE_MARKUP_NO_PLUGIN = "<p>The answer is 42</p>"


class TestFilterFunctional(BaseFunctionalTest):

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

        self.portal.invokeFactory("Document", "doc1")
        self.portal.doc1.text = RichTextValue(
            TINYMCE_MARKUP, "text/html", "text/x-html-safe"
        )

        self.portal.invokeFactory("Document", "doc2")
        self.portal.doc2.text = RichTextValue(
            TINYMCE_MARKUP_NO_PLUGIN, "text/html", "text/x-html-safe"
        )

    def test_filter_with_plugin_markup(self):
        from io import StringIO
        from lxml import etree

        browser = self.manager_browser()
        browser.open(f"{self.portal.doc1.absolute_url()}")
        tree = etree.parse(StringIO(browser.contents), etree.HTMLParser())

        result = tree.xpath("//*[contains(@class,'placeholder-socialmedia-consent')]")

        self.assertTrue(len(result) == 2)

    def test_filter_without_plugin_markup(self):

        browser = self.manager_browser()
        browser.open(f"{self.portal.doc2.absolute_url()}")

        self.assertTrue("<p>The answer is 42</p>" in browser.contents)
