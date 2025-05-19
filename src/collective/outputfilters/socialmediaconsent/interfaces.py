"""Module where all interfaces, events and exceptions live."""

from plone.outputfilters.interfaces import IFilter
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IBrowserLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ISocialMediaConsentFilter(IFilter):
    """Marker interface that defines the filter."""


class ICookieSettingsView(Interface):
    """Marker Interface"""
