from pprint import pprint

import settings

pprint(dir(settings))
pprint({'DEBUG': settings.DEBUG})
pprint(settings.DATABASES['default'])

