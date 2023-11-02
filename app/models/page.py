# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------

from app.models.core import Model


class Page(Model):

    fields = {
        "name":("","required"),
        "title": ("","required"),
        "elements":({},"required"),
        "path": ("","required")}
