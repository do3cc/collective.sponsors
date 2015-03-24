# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig

import collective.sponsors


class CollectiveSponsorsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        xmlconfig.file(
            'configure.zcml',
            collective.sponsors,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.sponsors:default')


COLLECTIVE_SPONSORS_FIXTURE = CollectiveSponsorsLayer()


COLLECTIVE_SPONSORS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_SPONSORS_FIXTURE,),
    name='CollectiveSponsorsLayer:IntegrationTesting'
)


COLLECTIVE_SPONSORS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_SPONSORS_FIXTURE,),
    name='CollectiveSponsorsLayer:FunctionalTesting'
)


COLLECTIVE_SPONSORS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_SPONSORS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveSponsorsLayer:AcceptanceTesting'
)
