from collective.outputfilters.socialmediaconsent.interfaces import ICookieSettingsView
from Products.Five.browser import BrowserView
from zope.interface import implementer


@implementer(ICookieSettingsView)
class CookieSettingsView(BrowserView):
    pass
