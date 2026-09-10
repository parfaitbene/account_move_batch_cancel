# -*- coding: utf-8 -*-
{
    "name": "Account Move Batch Cancel",
    "version": "18.0.1.0.0",
    "category": "Accounting",
    "summary": "Batch draft & cancel journal entries from the list view",
    "description": "This module allows users to batch cancel or draft account moves.",
    "author": "Parfait BENE",
    "maintainer": "Parfait BENE",
    "website": "https://parfaitbene.com/",
    "depends": ["account"],
    "data": [
        "security/ir.model.access.csv",
        "views/account_move_batch_cancel_views.xml",
    ],
    "images": ["static/description/icon.png"],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": False,
}