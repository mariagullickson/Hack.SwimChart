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
    url = 'http://toolbox.rico.snagajob.corp:83/swimchart'
    # url = 'http://localhost:54422/swimchart'
    if 'swimlane' in bottle.request.query:
        url += '?swimlaneid=%s' % bottle.request.query['swimlane']
    jsonData = urllib2.urlopen(url)
    data = json.loads(jsonData.read())
    nodeColors = {
        'root': 'orange',
        'swimlane': 'red',
        'Presentation/HTML/UI': 'indigo',
        'Foxpro': 'indigo',
        'REST API/IIS Hosted Service': 'darkblue',
        'WCF Service Adapter': 'darkblue',
        'Windows Service (EXE)': 'darkblue',
        'Pervasive': 'darkblue',
        'Mongo Config': 'darkgreen',
        'Mongo Database': 'darkgreen',
        'MySQL Database': 'darkgreen',
        'Solr 4.x': 'darkgreen',
        'Solr': 'darkgreen',
        'Database' : 'darkgreen',
        'BadDatabase' : 'green',
        'Api' : 'darkblue',
        'BadApi' : 'blue',
        'Service' : 'darkblue',
        'BadService' : 'blue',
        'Web' : 'indigo',
        'BadWeb' : 'purple',
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
