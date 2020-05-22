/*
 * gdb-frontend is a easy, flexible and extensionable gui debugger
 *
 * https://github.com/rohanrhu/gdb-frontend-live-plugin
 * https://oguzhaneroglu.com/projects/gdb-frontend-live-plugin/
 *
 * Licensed under GNU/GPLv3
 * Copyright (C) 2020, Oğuzhan Eroğlu (https://oguzhaneroglu.com/) <rohanrhu2@gmail.com>
 *
 */

$(document).ready(function () {
    GDBFrontend.components.gdbFrontend.openSource({file: {path: GDBFrontend.config.workdir+'/main.c'}});
    GDBFrontend.components.gdbFrontend.$gdbFrontend_load_loadBtn.hide();
    GDBFrontend.components.gdbFrontend.$GDBFrontend_load_connectBtn.hide();
    
    GDBFrontend.components.gdbFrontend.$GDBFrontend_runtimeControls_btn__run.off('click.GDBFrontend');
    GDBFrontend.components.gdbFrontend.$GDBFrontend_runtimeControls_btn__run.on('click.GDBFrontend', function (event) {
        $.ajax({
            url: '/gdb-frontend-live-adapter/build',
            cache: false,
            method: 'get',
            data: {
                source: GDBFrontend.config.workdir+'/main.c',
                break: 20
            },
            success: function (result_json) {
                if (!result_json.ok) {
                    GDBFrontend.showMessageBox({text: 'An error occured.'});
                    console.trace('An error occured.');
                    return;
                }
                
                $.ajax({
                    url: '/api/runtime/run',
                    cache: false,
                    method: 'get',
                    data: {
                    },
                    success: function (result_json) {
                    },
                    error: function () {
                        GDBFrontend.showMessageBox({text: 'An error occured.'});
                        console.trace('An error occured.');
                    }
                });
            },
            error: function () {
                GDBFrontend.showMessageBox({text: 'An error occured.'});
                console.trace('An error occured.');
            }
        });
    });

    GDBFrontend.components.gdbFrontend.$gdbFrontend_layout_middle_right.width(500)
});