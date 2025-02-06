from io import StringIO
from lxml import etree


class TestFilterFunctional:

    def test_filter_with_plugin_markup(self, portal_with_content, manager_browser):

        browser = manager_browser
        browser.open(f"{portal_with_content.doc1.absolute_url()}")
        tree = etree.parse(StringIO(browser.contents), etree.HTMLParser())

        result = tree.xpath("//*[contains(@class,'placeholder-socialmedia-consent')]")

        assert len(result) == 2

    def test_filter_without_plugin_markup(self, portal_with_content, manager_browser):

        browser = manager_browser
        browser.open(f"{portal_with_content.doc2.absolute_url()}")

        assert "<p>The answer is 42</p>" in browser.contents
