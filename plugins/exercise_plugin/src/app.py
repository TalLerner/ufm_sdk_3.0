#
# Copyright © 2013-2022 NVIDIA CORPORATION & AFFILIATES. ALL RIGHTS RESERVED.
#
# This software product is a proprietary product of Nvidia Corporation and its affiliates
# (the "Company") and all right, title, and interest in and to the software
# product, including all associated intellectual property rights, are and
# shall remain exclusively with the Company.
#
# This software product is governed by the End User License Agreement
# provided with the software product.
# @author: Tal Lerner
# @date:   Jan 22, 2024
# Plugin App Template

from flask import Flask

from api_calls import API

app = Flask(__name__)


@app.route('/ufm/telemetry')
def get_telemetry():
    get_telemetry_route = 'ufmRest/monitoring/session/0/data'
    api_call = API("10.209.36.170", "admin", "123456", get_telemetry_route)
    return api_call.run()


@app.route('/ufm/topology')
def get_topology():
    get_topology_route = "ufmRest/resources/links"
    api_call = API("10.209.36.170", "admin", "123456", get_topology_route)
    return api_call.run()


@app.route('/ufm/events')
def get_events():
    get_events_route = "ufmRest/app/events"
    api_call = API("10.209.36.170", "admin", "123456", get_events_route)
    return api_call.run()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8687)
