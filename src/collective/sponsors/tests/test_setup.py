# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.sponsors.testing import COLLECTIVE_SPONSORS_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that collective.sponsors is properly installed."""

    layer = COLLECTIVE_SPONSORS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.sponsors
           is installed with portal_quickinstaller.
        """
        self.assertTrue(self.installer.isProductInstalled(
            'collective.sponsors'))

    def test_uninstall(self):
        """Test if collective.sponsors is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.sponsors'])
        self.assertFalse(self.installer.isProductInstalled(
            'collective.sponsors'))

    def test_browserlayer(self):
        """Test that ICollectiveSponsorsLayer is registered."""
        from collective.sponsors.interfaces import ICollectiveSponsorsLayer
        from plone.browserlayer import utils
        self.assertIn(ICollectiveSponsorsLayer, utils.registered_layers())
