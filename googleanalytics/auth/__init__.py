# encoding: utf-8

"""
Convenience functions for authenticating with Google
and asking for authorization with Google, with
`authenticate` at its core.

`authenticate` will do what it says on the tin, but unlike
the basic `googleanalytics.oauth.authenticate`, it also tries
to get existing credentials from the keyring, from environment
variables, it prompts for information when required and so on.
"""

from . import keyring
from . import oauth
from .oauth import Flow, Credentials

def navigate(accounts, account=None, webproperty=None, profile=None, default_profile=True):
    if webproperty and not account:
        raise KeyError("Cannot navigate to a webproperty or profile without knowing the account.")
    if profile and not (webproperty and account):
        raise KeyError("Cannot navigate to a profile without knowing account and webproperty.")

    if profile:
        return accounts[account].webproperties[webproperty].profiles[profile]
    elif webproperty:
        scope = accounts[account].webproperties[webproperty]
        if default_profile:
            return scope.profile
        else:
            return scope
    elif account:
        return accounts[account]
    else:
        return accounts

def find(**kwargs):
    return oauth.Credentials.find(**kwargs)

def identity(name):
    return find(identity=name)

def authenticate(
        client_id=None, client_secret=None,
        client_email=None, private_key=None,
        access_token=None, refresh_token=None,
        account=None, webproperty=None, profile=None,
        identity=None, prefix=None, suffix=None,
        interactive=False, save=False):
    """
    The `authenticate` function will authenticate the user with the Google Analytics API,
    using a variety of strategies: keyword arguments provided to this function, credentials
    stored in in environment variables, credentials stored in the keychain and, finally, by
    asking for missing information interactively in a command-line prompt.

    If necessary (but only if `interactive=True`) this function will also allow the user
    to authorize this Python module to access Google Analytics data on their behalf,
    using an OAuth2 token.
    """

    #Skip

    #credentials = oauth.Credentials.find(
    #    valid=True,
    #    interactive=interactive,
    #    prefix=prefix,
    #    suffix=suffix,
    #    client_id=client_id,
    #    client_secret=client_secret,
    #    client_email=client_email,
    #    private_key=private_key,
    #    access_token=access_token,
    #    refresh_token=refresh_token,
    #    identity=identity,
    #    )

    #if credentials.incomplete:
    #    if interactive:
    #        credentials = authorize(
    #            client_id=credentials.client_id,
    #            client_secret=credentials.client_secret,
    #            save=save,
    #            identity=credentials.identity,
    #            prefix=prefix,
    #            suffix=suffix,
    #            )
    #    elif credentials.type == 2:
    #        credentials = authorize(
    #            client_email=credentials.client_email,
    #            private_key=credentials.private_key,
    #            identity=credentials.identity,
    #            save=save,
    #            )
    #    else:
    #        raise KeyError("Cannot authenticate: enable interactive authorization, pass a token or use a service account.")
    
    credentials = dict()
    credentials["access_token"] = None
    credentials["client_email"] = None
    credentials["client_id"] = None
    credentials["client_secret"] = None
    credentials["identity"] = "info@ranksense.com"
    credentials["private_key"] = None
    credentials["refresh_token"] = None

    #accounts = oauth.authenticate(credentials)
    
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

    from googleanalytics import account
    
    accounts = [account.Account(raw, service, credentials) for raw in raw_accounts]
    
    #return addressable.List(accounts, indices=['id', 'name'], insensitive=True)

    #scope = navigate(accounts, account=account, webproperty=webproperty, profile=profile)
    
    return accounts #scope

def authorize(client_id=None, client_secret=None, client_email=None, private_key=None, save=False, identity=None, prefix=None, suffix=None):
    base_credentials = oauth.Credentials.find(
        valid=True,
        interactive=True,
        identity=identity,
        client_id=client_id,
        client_secret=client_secret,
        client_email=client_email,
        private_key=private_key,
        prefix=prefix,
        suffix=suffix,
        )

    if base_credentials.incomplete:
        credentials = oauth.authorize(base_credentials.client_id, base_credentials.client_secret)
        credentials.identity = base_credentials.identity
    else:
        credentials = base_credentials

    if save:
        keyring.set(credentials.identity, credentials.serialize())

    return credentials

def revoke(client_id, client_secret,
        client_email=None, private_key=None,
        access_token=None, refresh_token=None,
        identity=None, prefix=None, suffix=None):

    """
    Given a client id, client secret and either an access token or a refresh token,
    revoke OAuth access to the Google Analytics data and remove any stored credentials
    that use these tokens.
    """

    if client_email and private_key:
        raise ValueError('Two-legged OAuth does not use revokable tokens.')
    
    credentials = oauth.Credentials.find(
        complete=True,
        interactive=False,
        identity=identity,
        client_id=client_id,
        client_secret=client_secret,
        access_token=access_token,
        refresh_token=refresh_token,
        prefix=prefix,
        suffix=suffix,
        )

    retval = credentials.revoke()
    keyring.delete(credentials.identity)
    return retval
