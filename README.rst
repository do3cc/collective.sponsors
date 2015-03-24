====================
collective.sponsors
====================

Sometimes, customers receive Sponsoring in some form and one of the rewards is a logo of the Sponsor on each page.

Often, this is at the bottom of the page and some customers have changing sponsors each year.

Usually, changing these logoos is quite urgent and usually, we are doing other things.

This package provides a simple mechanism that allows your customer to update the sponsor images.

This package provides a small viewlet that lists all links from a specific folder. It provides little helpers for content creators, for example a hint that the folder is missing.

Installation
------------
This package can be installed like every egg. Make it a dependency in your policy package or add it to your buildout.

The viewlet registers itself for the viewlet manager at the bottom. If you have your own viewlet manager, you need to register it for this viewlet manager on your own.

This package will not create the folder to add logos on its own. But it will allow the user to create one with a single click.

Configuration
-------------
You can hide the viewlet like any viewlet via `@@manage-viewlets`. The folder has no marker interface or something, it is just identified by name.

If you create the folder by following the `Create Folder` link provided by the viewlet. The folder will already be marked as not being shown in the navigation. If you modify the settings, make sure not to add the folder to the navigation by accident.

This package uses acquisition to look for the sponsor page, so it supports multilingual sites.
