"""Installer for the collective.outputfilters.socialmediaconsent package."""

from pathlib import Path
from setuptools import find_packages
from setuptools import setup


long_description = f"""
{Path("README.md").read_text()}\n
{Path("CONTRIBUTORS.md").read_text()}\n
{Path("CHANGES.md").read_text()}\n
"""


setup(
    name="collective.outputfilters.socialmediaconsent",
    version="1.0.0a0",
    description="Outputfilter for embedding social media plugins",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: 6.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="1letter",
    author_email="1letter@gmx.de",
    url="https://github.com/1letter/collective.outputfilters.socialmediaconsent",
    project_urls={
        "PyPI": "https://pypi.org/project/collective.outputfilters.socialmediaconsent",
        "Source": "https://github.com/1letter/collective.outputfilters.socialmediaconsent",
        "Tracker": "https://github.com/1letter/collective.outputfilters.socialmediaconsent/issues",
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["collective", "collective.outputfilters"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "beautifulsoup4",
        "plone.outputfilters",
        "setuptools",
        "Products.CMFPlone",
        "Products.CMFCore",
        "Products.GenericSetup",
        "zope.i18nmessageid",
        "zope.interface",
        "zope.publisher",
    ],
    extras_require={
        "test": [
            "zest.releaser[recommended]",
            "zestreleaser.towncrier",
            "plone.app.testing",
            "plone.app.robotframework[debug]",
            "pytest",
            "pytest-cov",
            "pytest-plone>=0.5.0",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = collective.outputfilters.socialmediaconsent.locales.update:update_locale
    """,
)
