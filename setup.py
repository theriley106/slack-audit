#!/usr/bin/env python

from distutils.core import setup

setup(name='slack-audit',
      version='1.0',
      description='Python scripts to be run in Lambda to help audit slack',
      author='Auth0',
      url='https://github.com/auth0/slack-audit',
      scripts=['access_lambda_function.py', 'integrations_lambda_function.py']
     )
