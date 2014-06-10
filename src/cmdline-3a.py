import os
from pprint import pprint

import settings

env = os.environ.get('PYSCHOOL_DATABASE', 'default')
print('Current environment is "{}".'.format(env))

if env in settings.DATABASES:
    pprint(settings.DATABASES[env])
else:
    print('Unknown environment for database settings.')
