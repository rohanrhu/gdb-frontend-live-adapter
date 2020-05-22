# -*- coding: utf-8 -*-
#
# gdb-frontend is a easy, flexible and extensionable gui debugger
#
# https://github.com/rohanrhu/gdb-frontend-live-plugin
# https://oguzhaneroglu.com/projects/gdb-frontend-live-plugin/
#
# Licensed under GNU/GPLv3
# Copyright (C) 2020, Oğuzhan Eroğlu (https://oguzhaneroglu.com/) <rohanrhu2@gmail.com>

import json
import urllib
import os

import gdb

import api.debug

def run(request, params):
    if params is None: params = {}

    url_path = urllib.parse.urlparse(request.path)
    qs_params = urllib.parse.parse_qs(url_path.query)

    result_json = {}
    result_json["ok"] = True

    try:
        source = qs_params["source"][0]
        executable = ".".join(source.split("/")[-1].split(".")[:-1])
        executable = "/".join(source.split("/")[:-1]) + "/" + executable
        
        os.system("gcc -o " + executable + " " + source + " -g")

        if "gflive_gdb_executable" not in globals() or globals()["gflive_gdb_executable"] != executable:
            print("[GDBFrontendLive]", "Loading executable.")

            globals()["gflive_gdb_executable"] = executable

            api.debug.load(executable)

            if "break" in qs_params:
                api.debug.addBreakpoint(source, int(qs_params["break"][0]))

        result_json["executable"] = executable
    except:
        result_json["ok"] = False

    request.send_response(200)
    request.send_header("Content-Type", "application/json; charset=utf-8")
    request.end_headers()
    request.wfile.write(json.dumps(result_json).encode())