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
    # url = 'http://toolbox.rico.snagajob.corp:83/swimchart'
    url = 'http://localhost:54422/swimchart'
    if 'swimlane' in bottle.request.query:
        url += '?swimlaneid=%s' % bottle.request.query['swimlane']
    jsonData = urllib2.urlopen(url)
    data = json.loads(jsonData.read())
    nodeColors = {
        'root': 'orange',
        'swimlane': 'red',
        'Presentation/HTML/UI': 'purple',
        'Foxpro': 'purple',
        'REST API/IIS Hosted Service': 'blue',
        'WCF Service Adapter': 'blue',
        'Windows Service (EXE)': 'blue',
        'Pervasive': 'blue',
        'Mongo Config': 'green',
        'Mongo Database': 'green',
        'MySQL Database': 'green',
        'Solr 4.x': 'green',
        'Solr': 'green',
        'Database' : 'green',
        'BadDatabase' : 'lightgreen',
        'Api' : 'blue',
        'BadApi' : 'lightblue',
        'Service' : 'blue',
        'BadService' : 'lightblue',
        'Web' : 'purple',
        'BadWeb' : 'lightpurple',
        }

    if 'swimlane' not in bottle.request.query:
        bottle.request.query['swimlane'] = ''

    return bottle.template('swimchart',
                           data=data['List'],
                           nodeColors=nodeColors,
                           swimlane=bottle.request.query['swimlane'])


@bottle.route('/assets/:filepath#.*#')
def asset(filepath):
    return bottle.static_file(filepath, root='./assets/')


bottle.run(host='localhost', port=8765)
