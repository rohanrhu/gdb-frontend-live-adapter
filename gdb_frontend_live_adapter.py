# -*- coding: utf-8 -*-
#
# gdb-frontend is a easy, flexible and extensionable gui debugger
#
# https://github.com/rohanrhu/gdb-frontend-live-plugin
# https://oguzhaneroglu.com/projects/gdb-frontend-live-plugin/
#
# Licensed under GNU/GPLv3
# Copyright (C) 2020, Oğuzhan Eroğlu (https://oguzhaneroglu.com/) <rohanrhu2@gmail.com>

import importlib

import plugin

gdb = importlib.import_module("gdb")

class GdbFrontendLiveAdapterPlugin(plugin.GDBFrontendPlugin):
    def __init__(self):
        plugin.GDBFrontendPlugin.__init__(self)

    def loaded(self):
        pass

    def unloaded(self):
        pass