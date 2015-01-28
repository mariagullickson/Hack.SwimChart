#!/usr/bin/python

import bottle
import json
import urllib2


@bottle.route('/hello/<name>')
def hello(name):
    return bottle.template('hello', name=name)


@bottle.route('/swimchart')
def showStuff():
    # load the raw data
    jsonData = urllib2.urlopen(
        'http://toolbox.rico.snagajob.corp:83/swimchart')
    data = json.loads(jsonData.read())
    nodeColors = {
        'swimlane': 'orange',
        'Presentation/HTML/UI': 'red',
        'Foxpro': 'red',
        'REST API/IIS Hosted Service': 'purple',
        'WCF Service Adapter': 'purple',
        'Windows Service (EXE)': 'purple',
        'Pervasive': 'purple',
        'Mongo Config': 'blue',
        'MySQL Database': 'blue',
        'Solr 4.x': 'blue',
        'Solr': 'blue',
        }

    return bottle.template('swimchart', data=data['List'],
                           nodeColors=nodeColors)


@bottle.route('/assets/:filepath#.*#')
def asset(filepath):
    return bottle.static_file(filepath, root='./assets/')


bottle.run(host='localhost', port=8765)
