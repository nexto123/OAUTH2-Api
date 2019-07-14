# oAuth2 API App


[![Build Status](https://travis-ci.org/nexto123/ouath2-api.svg?branch=master)](https://travis-ci.org/nexto123/ouath2-api)


### Getting Started

This is a django app which illustrates the use of the oauth2 user authentication
system.


## Prerequisites

To get started   

All-auth comes with it's own Hashing sytem

As an extra security measure on top of what the standard Django password reset token generator is already facilitating, 
allauth now adds the user email address and password to the hash such that whenever the user’s email address changes the token is invalidated.

### Adapter

From allauth/account/adapter.py we  can further clean our passwords and override the default setting.
We can now then set our own parameters for passwords and 