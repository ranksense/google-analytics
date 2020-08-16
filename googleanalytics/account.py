# encoding: utf-8

"""
"""

import functools

import yaml
import addressable

from . import utils
from . import query
from . import columns
from .columns import Column, Segment, ColumnList, SegmentList


class Account(object):
    """
    An account is usually but not always associated with a single
    website. It will often contain multiple web properties
    (different parts of your website that you've configured
    Google Analytics to analyze separately, or simply the default
    web property that every website has in Google Analytics),
    which in turn will have one or more profiles.

    You should navigate to a profile to run queries.

    ```python
    import googleanalytics as ga
    accounts = ga.authenticate()
    profile = accounts['debrouwere.org'].webproperties['UA-12933299-1'].profiles['debrouwere.org']
    report = profile.core.query('pageviews').range('2014-10-01', '2014-10-31').get()
    print(report['pageviews'])
    ```
    """

    def __init__(self, raw, service, credentials):
        
        self.service = None
        self.credentials = None
        self.raw = {'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties',
              'type': 'analytics#webproperties'},
             'created': '2006-06-07T20:01:28.000Z',
             'id': 'XXXXXX',
             'kind': 'analytics#account',
             'name': 'sitename_11',
             'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
             'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX',
             'updated': '2019-07-02T18:00:31.573Z'}

        self.id = 'XXXXXX'
        self.name = 'sitename_11'
        self.permissions = ['COLLABORATE', 'READ_AND_ANALYZE']
        
        #self.service = service
        #self.credentials = credentials
        #self.raw = raw
        #self.id = raw['id']
        #self.name = raw['name']
        #self.permissions = raw['permissions']['effective']

    @property
    @utils.memoize
    def webproperties(self):
        """
        A list of all web properties on this account. You may
        select a specific web property using its name, its id
        or an index.

        ```python
        account.webproperties[0]
        account.webproperties['UA-9234823-5']
        account.webproperties['debrouwere.org']
        ```
        """

        #raw_properties = self.service.management().webproperties().list(
        #    accountId=self.id).execute()['items']

        raw_properties = [{'accountId': 'ACCT_0',
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles',
          'type': 'analytics#profiles'},
          'created': '2006-06-07T20:01:28.000Z',
          'dataRetentionResetOnNewActivity': True,
          'dataRetentionTtl': 'INDEFINITE',
          'defaultProfileId': 'PROF_0',
          'id': 'UA-ACCT_1-1',
          'industryVertical': 'UNSPECIFIED',
          'internalWebPropertyId': 'WEB_0',
          'kind': 'analytics#webproperty',
          'level': 'STANDARD',
          'name': 'sitename_0',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX',
          'type': 'analytics#account'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'profileCount': 14,
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'updated': '2020-01-14T18:50:03.686Z',
          'websiteUrl': 'http://sitename_0'},
        {'accountId': 'ACCT_1',
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles',
          'type': 'analytics#profiles'},
          'created': '2013-10-29T19:06:37.094Z',
          'dataRetentionResetOnNewActivity': True,
          'dataRetentionTtl': 'INDEFINITE',
          'defaultProfileId': 'PROF_1',
          'id': 'UA-ACCT_1-3',
          'industryVertical': 'OTHER',
          'internalWebPropertyId': 'WEB_1',
          'kind': 'analytics#webproperty',
          'level': 'STANDARD',
          'name': 'sitename_1',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX',
          'type': 'analytics#account'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'profileCount': 1,
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'updated': '2018-05-24T16:31:06.244Z',
          'websiteUrl': 'http://sitename_1'},
        {'accountId': 'ACCT_1',
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles',
          'type': 'analytics#profiles'},
          'created': '2013-10-29T19:26:40.176Z',
          'dataRetentionResetOnNewActivity': True,
          'dataRetentionTtl': 'INDEFINITE',
          'defaultProfileId': 'PROF_2',
          'id': 'UA-ACCT_1-4',
          'industryVertical': 'UNSPECIFIED',
          'internalWebPropertyId': 'WEB_2',
          'kind': 'analytics#webproperty',
          'level': 'STANDARD',
          'name': 'sitename_2',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX',
          'type': 'analytics#account'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'profileCount': 1,
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'updated': '2018-05-24T16:31:22.440Z',
          'websiteUrl': 'http://sitename_2'},
        {'accountId': 'ACCT_1',
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles',
          'type': 'analytics#profiles'},
          'created': '2013-10-29T21:42:12.067Z',
          'dataRetentionResetOnNewActivity': True,
          'dataRetentionTtl': 'INDEFINITE',
          'defaultProfileId': 'PROF_3',
          'id': 'UA-ACCT_1-5',
          'industryVertical': 'OTHER',
          'internalWebPropertyId': 'WEB_3',
          'kind': 'analytics#webproperty',
          'level': 'STANDARD',
          'name': 'sitename_3',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX',
          'type': 'analytics#account'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'profileCount': 1,
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'updated': '2018-05-24T16:30:48.975Z',
          'websiteUrl': 'http://sitename_3'},
        {'accountId': 'ACCT_1',
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles',
          'type': 'analytics#profiles'},
          'created': '2014-03-04T23:17:50.901Z',
          'dataRetentionResetOnNewActivity': True,
          'dataRetentionTtl': 'INDEFINITE',
          'defaultProfileId': 'PROF_4',
          'id': 'UA-ACCT_1-6',
          'industryVertical': 'OTHER',
          'internalWebPropertyId': 'WEB_4',
          'kind': 'analytics#webproperty',
          'level': 'STANDARD',
          'name': 'sitename_4',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX',
          'type': 'analytics#account'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'profileCount': 1,
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'updated': '2018-05-24T16:30:21.291Z',
          'websiteUrl': 'http://sitename_4'},
        {'accountId': 'ACCT_1',
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles',
          'type': 'analytics#profiles'},
          'created': '2014-06-11T18:16:42.616Z',
          'dataRetentionResetOnNewActivity': True,
          'dataRetentionTtl': 'INDEFINITE',
          'defaultProfileId': 'PROF_5',
          'id': 'UA-ACCT_1-7',
          'industryVertical': 'OTHER',
          'internalWebPropertyId': 'WEB_5',
          'kind': 'analytics#webproperty',
          'level': 'STANDARD',
          'name': 'sitename_5',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX',
          'type': 'analytics#account'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'profileCount': 1,
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'updated': '2018-05-24T16:31:45.706Z',
          'websiteUrl': 'https://sitename_5'},
        {'accountId': 'ACCT_1',
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles',
          'type': 'analytics#profiles'},
          'created': '2017-09-12T21:58:59.630Z',
          'dataRetentionResetOnNewActivity': True,
          'dataRetentionTtl': 'INDEFINITE',
          'defaultProfileId': 'PROF_6',
          'id': 'UA-ACCT_1-8',
          'industryVertical': 'OTHER',
          'internalWebPropertyId': 'WEB_6',
          'kind': 'analytics#webproperty',
          'level': 'STANDARD',
          'name': 'sitename_6',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX',
          'type': 'analytics#account'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'profileCount': 1,
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'updated': '2018-05-24T16:30:06.752Z',
          'websiteUrl': 'https://sitename_6'}]
          

        _webproperties = [WebProperty(raw, self) for raw in raw_properties]
        return addressable.List(_webproperties, indices=['id', 'name'], insensitive=True)

    @property
    def query(self, *vargs, **kwargs):
        """ A shortcut to the first profile of the first webproperty. """
        return self.webproperties[0].query(*vargs, **kwargs)

    def __repr__(self):
        return "<googleanalytics.account.Account object: {} ({})>".format(
            self.name, self.id)


class WebProperty(object):
    """
    A web property is a particular website you're tracking in Google Analytics.
    It has one or more profiles, and you will need to pick one from which to
    launch your queries.
    """

    def __init__(self, raw, account):
        self.account = account
        self.raw = raw
        self.id = raw['id']
        self.name = raw['name']
        # on rare occassions, e.g. for abandoned web properties,
        # a website url might not be present
        self.url = raw.get('websiteUrl')

    @property
    def profile(self):
        default = self.raw['defaultProfileId']
        return self.profiles[default]

    @property
    @utils.memoize
    def profiles(self):
        """
        A list of all profiles on this web property. You may
        select a specific profile using its name, its id
        or an index.

        ```python
        property.profiles[0]
        property.profiles['9234823']
        property.profiles['marketing profile']
        ```
        """
        #raw_profiles = self.account.service.management().profiles().list(
        #    accountId=self.account.id,
        #    webPropertyId=self.id).execute()['items']

        raw_profiles = [{'accountId': 'ACCT_1',
          'botFilteringEnabled': True,
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXX/goals',
          'type': 'analytics#goals'},
          'created': '2006-06-07T20:01:29.000Z',
          'currency': 'USD',
          'eCommerceTracking': True,
          'enhancedECommerceTracking': False,
          'id': 'XXXXXX',
          'internalWebPropertyId': 'WEB_7',
          'kind': 'analytics#profile',
          'name': 'www.sitename_0',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'type': 'analytics#webproperty'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXX',
          'siteSearchCategoryParameters': 'category',
          'siteSearchQueryParameters': 'q',
          'stripSiteSearchCategoryParameters': False,
          'stripSiteSearchQueryParameters': False,
          'timezone': 'America/Toronto',
          'type': 'WEB',
          'updated': '2019-11-04T15:45:15.079Z',
          'webPropertyId': 'UA-WEB_0-1',
          'websiteUrl': 'http://sitename_0'},
        {'accountId': 'ACCT_1',
          'botFilteringEnabled': True,
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXX/goals',
          'type': 'analytics#goals'},
          'created': '2006-08-10T20:15:26.000Z',
          'currency': 'USD',
          'eCommerceTracking': False,
          'id': 'XXXXXX',
          'internalWebPropertyId': 'WEB_7',
          'kind': 'analytics#profile',
          'name': 'Amex Monthly Gifts',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'type': 'analytics#webproperty'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXX',
          'timezone': 'America/Toronto',
          'type': 'WEB',
          'updated': '2016-02-27T14:26:46.689Z',
          'webPropertyId': 'UA-WEB_1-1',
          'websiteUrl': 'http://sitename_0'},
        {'accountId': 'ACCT_1',
          'botFilteringEnabled': True,
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX/goals',
          'type': 'analytics#goals'},
          'created': '2015-04-01T00:15:09.899Z',
          'currency': 'USD',
          'eCommerceTracking': True,
          'enhancedECommerceTracking': False,
          'id': 'XXXXXX',
          'internalWebPropertyId': 'WEB_7',
          'kind': 'analytics#profile',
          'name': 'www.sitename_0 - TEST Environment',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'type': 'analytics#webproperty'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX',
          'siteSearchQueryParameters': 'q',
          'stripSiteSearchQueryParameters': False,
          'timezone': 'America/Toronto',
          'type': 'WEB',
          'updated': '2018-01-05T22:06:51.692Z',
          'webPropertyId': 'UA-WEB_1-1',
          'websiteUrl': 'http://sitename_0'},
        {'accountId': 'ACCT_1',
          'botFilteringEnabled': True,
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX/goals',
          'type': 'analytics#goals'},
          'created': '2015-04-01T00:15:34.040Z',
          'currency': 'USD',
          'defaultPage': 'Home.aspx',
          'eCommerceTracking': True,
          'enhancedECommerceTracking': False,
          'id': 'XXXXXX',
          'internalWebPropertyId': 'WEB_7',
          'kind': 'analytics#profile',
          'name': 'www.sitename_0 - UNFILTERED View',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'type': 'analytics#webproperty'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX',
          'siteSearchCategoryParameters': 'category',
          'siteSearchQueryParameters': 'q',
          'stripSiteSearchCategoryParameters': False,
          'stripSiteSearchQueryParameters': False,
          'timezone': 'America/Toronto',
          'type': 'WEB',
          'updated': '2016-10-27T13:15:11.156Z',
          'webPropertyId': 'UA-WEB_1-1',
          'websiteUrl': 'http://sitename_0'},
        {'accountId': 'ACCT_1',
          'botFilteringEnabled': True,
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX/goals',
          'type': 'analytics#goals'},
          'created': '2015-06-03T02:39:46.541Z',
          'currency': 'USD',
          'eCommerceTracking': True,
          'enhancedECommerceTracking': False,
          'id': 'XXXXXX',
          'internalWebPropertyId': 'WEB_7',
          'kind': 'analytics#profile',
          'name': 'GIV3 Traffic Only',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'type': 'analytics#webproperty'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX',
          'timezone': 'America/Toronto',
          'type': 'WEB',
          'updated': '2019-12-06T19:31:51.511Z',
          'webPropertyId': 'UA-WEB_1-1',
          'websiteUrl': 'http://sitename_0'},
        {'accountId': 'ACCT_1',
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX/goals',
          'type': 'analytics#goals'},
          'created': '2017-09-12T21:38:41.980Z',
          'currency': 'USD',
          'eCommerceTracking': False,
          'id': 'XXXXXX',
          'internalWebPropertyId': 'WEB_7',
          'kind': 'analytics#profile',
          'name': 'sitename_0 - excluding internal traffic',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'type': 'analytics#webproperty'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX',
          'timezone': 'America/New_York',
          'type': 'WEB',
          'updated': '2017-09-12T21:38:41.980Z',
          'webPropertyId': 'UA-WEB_1-1',
          'websiteUrl': 'http://sitename_0'},
        {'accountId': 'ACCT_1',
          'botFilteringEnabled': False,
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX/goals',
          'type': 'analytics#goals'},
          'created': '2018-01-04T14:55:08.146Z',
          'currency': 'USD',
          'eCommerceTracking': False,
          'id': 'XXXXXX',
          'internalWebPropertyId': 'WEB_7',
          'kind': 'analytics#profile',
          'name': 'www.sitename_0 - Donor Help & Charity Help View',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'type': 'analytics#webproperty'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX',
          'siteSearchQueryParameters': 's',
          'stripSiteSearchQueryParameters': False,
          'timezone': 'America/New_York',
          'type': 'WEB',
          'updated': '2018-08-15T14:56:24.119Z',
          'webPropertyId': 'UA-WEB_1-1',
          'websiteUrl': 'http://sitename_0'},
        {'accountId': 'ACCT_1',
          'botFilteringEnabled': True,
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX/goals',
          'type': 'analytics#goals'},
          'created': '2018-01-04T15:35:37.284Z',
          'currency': 'USD',
          'eCommerceTracking': True,
          'enhancedECommerceTracking': False,
          'id': 'XXXXXX',
          'internalWebPropertyId': 'WEB_7',
          'kind': 'analytics#profile',
          'name': 'www.sitename_0 - Angela TEST Environment',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'type': 'analytics#webproperty'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX',
          'siteSearchCategoryParameters': 'category',
          'siteSearchQueryParameters': 'q',
          'stripSiteSearchCategoryParameters': False,
          'stripSiteSearchQueryParameters': False,
          'timezone': 'America/Toronto',
          'type': 'WEB',
          'updated': '2018-06-07T14:23:17.083Z',
          'webPropertyId': 'UA-WEB_1-1',
          'websiteUrl': 'http://sitename_0'},
        {'accountId': 'ACCT_1',
          'botFilteringEnabled': False,
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX/goals',
          'type': 'analytics#goals'},
          'created': '2018-06-22T18:31:50.420Z',
          'currency': 'USD',
          'eCommerceTracking': True,
          'enhancedECommerceTracking': True,
          'id': 'XXXXXX',
          'internalWebPropertyId': 'WEB_7',
          'kind': 'analytics#profile',
          'name': 'Test View - CDN',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'type': 'analytics#webproperty'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX',
          'timezone': 'America/Los_Angeles',
          'type': 'WEB',
          'updated': '2018-08-10T16:48:09.300Z',
          'webPropertyId': 'UA-WEB_1-1',
          'websiteUrl': 'http://sitename_0'},
        {'accountId': 'ACCT_1',
          'botFilteringEnabled': False,
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX/goals',
          'type': 'analytics#goals'},
          'created': '2018-08-10T16:46:29.030Z',
          'currency': 'CAD',
          'eCommerceTracking': True,
          'enhancedECommerceTracking': False,
          'id': 'XXXXXX',
          'internalWebPropertyId': 'WEB_7',
          'kind': 'analytics#profile',
          'name': 'Events Only View',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'type': 'analytics#webproperty'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX',
          'timezone': 'America/Toronto',
          'type': 'WEB',
          'updated': '2018-09-14T12:48:44.581Z',
          'webPropertyId': 'UA-WEB_1-1',
          'websiteUrl': 'https://sitename_0'},
        {'accountId': 'ACCT_1',
          'botFilteringEnabled': False,
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX/goals',
          'type': 'analytics#goals'},
          'created': '2018-08-10T13:18:26.813Z',
          'currency': 'USD',
          'eCommerceTracking': True,
          'enhancedECommerceTracking': True,
          'id': 'XXXXXX',
          'internalWebPropertyId': 'WEB_7',
          'kind': 'analytics#profile',
          'name': 'CDN Only View',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'type': 'analytics#webproperty'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX',
          'timezone': 'America/Los_Angeles',
          'type': 'WEB',
          'updated': '2019-02-07T22:57:13.804Z',
          'webPropertyId': 'UA-WEB_1-1',
          'websiteUrl': 'http://sitename_0'},
        {'accountId': 'ACCT_1',
          'botFilteringEnabled': False,
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX/goals',
          'type': 'analytics#goals'},
          'created': '2018-08-10T18:50:34.929Z',
          'currency': 'USD',
          'eCommerceTracking': True,
          'enhancedECommerceTracking': False,
          'id': 'XXXXXX',
          'internalWebPropertyId': 'WEB_7',
          'kind': 'analytics#profile',
          'name': 'P2P View',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'type': 'analytics#webproperty'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX',
          'timezone': 'America/Toronto',
          'type': 'WEB',
          'updated': '2019-02-07T22:57:13.909Z',
          'webPropertyId': 'UA-WEB_1-1',
          'websiteUrl': 'https://sitename_0'},
        {'accountId': 'ACCT_1',
          'botFilteringEnabled': False,
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX/goals',
          'type': 'analytics#goals'},
          'created': '2018-08-15T13:13:09.842Z',
          'currency': 'CAD',
          'eCommerceTracking': True,
          'enhancedECommerceTracking': False,
          'id': 'XXXXXX',
          'internalWebPropertyId': 'WEB_7',
          'kind': 'analytics#profile',
          'name': 'Direct Site Only',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'type': 'analytics#webproperty'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX',
          'siteSearchCategoryParameters': 'category',
          'siteSearchQueryParameters': 'q',
          'stripSiteSearchCategoryParameters': False,
          'stripSiteSearchQueryParameters': False,
          'timezone': 'America/Toronto',
          'type': 'WEB',
          'updated': '2019-11-04T15:45:29.600Z',
          'webPropertyId': 'UA-WEB_1-1',
          'websiteUrl': 'http://sitename_0'},
        {'accountId': 'ACCT_1',
          'botFilteringEnabled': False,
          'childLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX/goals',
          'type': 'analytics#goals'},
          'created': '2018-09-07T15:36:03.285Z',
          'currency': 'CAD',
          'eCommerceTracking': False,
          'id': 'XXXXXX',
          'internalWebPropertyId': 'WEB_7',
          'kind': 'analytics#profile',
          'name': 'For Charities',
          'parentLink': {'href': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X',
          'type': 'analytics#webproperty'},
          'permissions': {'effective': ['COLLABORATE', 'READ_AND_ANALYZE']},
          'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/XXXXXX/webproperties/UA-XXXXXX-X/profiles/XXXXXXXXX',
          'timezone': 'America/Toronto',
          'type': 'WEB',
          'updated': '2019-06-06T15:29:47.740Z',
          'webPropertyId': 'UA-WEB_1-1',
          'websiteUrl': 'http://sitename_0'}]


        profiles = [Profile(raw, self) for raw in raw_profiles]
        return addressable.List(profiles, indices=['id', 'name'], insensitive=True)

    def query(self, *vargs, **kwargs):
        """
        A shortcut to the first profile of this webproperty.
        """
        return self.profiles[0].query(*vargs, **kwargs)

    def __repr__(self):
        return "<googleanalytics.account.WebProperty object: {} ({})>".format(
            self.name, self.id)


class Profile(object):
    """
    A profile is a particular analytics configuration of a web property.
    Each profile belongs to a web property and an account. As all
    queries using the Google Analytics API run against a particular
    profile, queries can only be created from a `Profile` object.

    ```python
    profile.query('pageviews').range('2014-01-01', days=7).get()
    ```
    """

    def __init__(self, raw, webproperty):
        self.raw = raw
        self.webproperty = webproperty
        self.account = webproperty.account
        self.id = raw['id']
        self.name = raw['name']
        self.core = CoreReportingAPI(self)
        self.realtime = RealTimeReportingAPI(self)

    def __repr__(self):
        return "<googleanalytics.account.Profile object: {} ({})>".format(
            self.name, self.id)


class ReportingAPI(object):
    REPORT_TYPES = {
        'ga': 'ga',
        'realtime': 'rt',
    }

    QUERY_TYPES = {
        'ga': query.CoreQuery,
        'realtime': query.RealTimeQuery,
    }

    def __init__(self, endpoint, profile):
        """
        Endpoint can be one of `ga` or `realtime`.
        """
        
        # various shortcuts
        self.profile = profile
        self.account = account = profile.account
        self.service = service = profile.account.service
        root = service.data()
        self.endpoint_type = endpoint
        self.endpoint = getattr(root, endpoint)()

        # query interface
        self.report_type = self.REPORT_TYPES[endpoint]
        Query = self.QUERY_TYPES[endpoint]
        self.query = Query(self)

        # optional caching layer
        self.cache = None

    @property
    @utils.memoize
    def all_columns(self):
        query = self.service.metadata().columns().list(
            reportType=self.report_type
            )
        raw_columns = query.execute()['items']
        hydrated_columns = utils.flatten(map(Column.from_metadata, raw_columns))
        return ColumnList(hydrated_columns, unique=False)

    @property
    @utils.memoize
    def columns(self):
        return addressable.filter(columns.is_supported, self.all_columns)

    @property
    @utils.memoize
    def segments(self):
        query = self.service.management().segments().list()
        raw_segments = query.execute()['items']
        hydrated_segments = [Segment(raw, self) for raw in raw_segments]
        return SegmentList(hydrated_segments)

    @property
    @utils.memoize
    def metrics(self):
        return addressable.filter(columns.is_metric, self.columns)

    @property
    @utils.memoize
    def dimensions(self):
        return addressable.filter(columns.is_dimension, self.columns)

    @property
    @utils.memoize
    def goals(self):
        raise NotImplementedError()

    def __repr__(self):
        return '<googleanalytics.account.{} object>'.format(self.__class__.__name__)


class CoreReportingAPI(ReportingAPI):
    def __init__(self, profile):
        super(CoreReportingAPI, self).__init__('ga', profile)


class RealTimeReportingAPI(ReportingAPI):
    def __init__(self, profile):
        super(RealTimeReportingAPI, self).__init__('realtime', profile)

    # in principle, we should be able to reuse everything from the ReportingAPI
    # base class, but the Real Time Reporting API is still in beta and some
    # things – like a metadata endpoint – are missing.
    @property
    @utils.memoize
    def all_columns(self):
        raw_columns = yaml.load(open(utils.here('realtime.yml')))
        hydrated_columns = utils.flatten(map(Column.from_metadata, raw_columns))
        return ColumnList(hydrated_columns)

