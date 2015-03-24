from collective.sponsors.testing import COLLECTIVE_SPONSORS_INTEGRATION_TESTING  # noqa
from zope.component import getMultiAdapter
from zope.viewlet.interfaces import IViewletManager
from plone import api
from Products.Five.browser import BrowserView

import unittest


class TestViewlet(unittest.TestCase):

    layer = COLLECTIVE_SPONSORS_INTEGRATION_TESTING

    def setUp(self):
        self.request = self.layer['request']
        self.context = self.layer['portal']

    def test_viewlet_available(self):
        manager_name = 'xxx'
        view = BrowserView(self.context, self.request)
        manager = getMultiAdapter((self.context, self.request, view),
                                  IViewletManager,
                                  manager_name)

        manager.update()

        my_viewlet = [x for x in manager.viewlets if x.__name__ == 'xxx']
        self.assertTrue(my_viewlet)
