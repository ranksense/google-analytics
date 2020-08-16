# encoding: utf-8

import json
import webbrowser

import addressable
from oauth2client import client
from apiclient import discovery

from googleanalytics import utils, account
from .credentials import Credentials, normalize


class Flow(client.OAuth2WebServerFlow):
    def __init__(self, client_id, client_secret, redirect_uri):
        super(Flow, self).__init__(client_id, client_secret,
            scope='https://www.googleapis.com/auth/analytics.readonly',
            redirect_uri=redirect_uri)

    def step2_exchange(self, code):
        credentials = super(Flow, self).step2_exchange(code)
        return Credentials.find(complete=True, **credentials.__dict__)

# a simplified version of `oauth2client.tools.run_flow`
def authorize(client_id, client_secret, port=5000):
    flow = Flow(client_id, client_secret,
        redirect_uri='http://localhost:{port}/'.format(port=port))

    authorize_url = flow.step1_get_authorize_url()
    webbrowser.open(authorize_url, new=1, autoraise=True)
    qs = utils.single_serve(
        message='Authentication flow completed. You may close the browser tab.',
        port=port)
    return flow.step2_exchange(qs['code'])

@normalize
def revoke(credentials):
    return credentials.revoke()

@normalize
def authenticate(credentials):
    client = credentials.authorize()
    service = discovery.build('analytics', 'v3', http=client)
    #raw_accounts = service.management().accounts().list().execute()['items']
    
    raw_accounts = [{'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties',
   'type': 'analytics#webproperties'},
  'created': '2006-06-07T20:01:28.000Z',
  'id': 'XXXXXX',
  'kind': 'analytics#account',
  'name': 'sitename_11',
  'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
  'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX',
  'updated': '2019-07-02T18:00:31.573Z'},
 {'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXXXX/webproperties',
   'type': 'analytics#webproperties'},
  'created': '2014-02-13T03:15:18.155Z',
  'id': 'XXXXXXXX',
  'kind': 'analytics#account',
  'name': 'sitename_10',
  'permissions': {'effective': []},
  'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXXXX',
  'updated': '2016-07-14T19:41:40.634Z'},
 {'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXXXX/webproperties',
   'type': 'analytics#webproperties'},
  'created': '2014-05-05T18:50:09.025Z',
  'id': 'XXXXXXXX',
  'kind': 'analytics#account',
  'name': 'RankSense',
  'permissions': {'effective': ['COLLABORATE',
    'EDIT',
    'MANAGE_USERS',
    'READ_AND_ANALYZE']},
  'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXXX',
  'updated': '2017-02-25T17:20:39.203Z'},
 {'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXXX/webproperties',
   'type': 'analytics#webproperties'},
  'created': '2017-05-05T15:40:21.336Z',
  'id': 'XXXXXXXX',
  'kind': 'analytics#account',
  'name': 'http://sitename_09/',
  'permissions': {'effective': ['COLLABORATE',
    'EDIT',
    'MANAGE_USERS',
    'READ_AND_ANALYZE']},
  'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXXXX',
  'updated': '2017-05-05T15:40:21.336Z'}]

        
    accounts = [account.Account(raw, service, credentials) for raw in raw_accounts]
    return addressable.List(accounts, indices=['id', 'name'], insensitive=True)
