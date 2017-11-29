import os
import re
import subprocess

import metassistant


def app(args):
    try:
        if re.compile(r'^\w+$').match(args.name) is None:
            return 'The name given is does not match /^\w*$/'
    except AttributeError:
        return 'There was no name given'

    command = 'cd {0} && python manage.py startapp {1}'.format(os.path.join(metassistant.PATH, 'metaproject'),
                                                               args.name)
    try:
        if 0 != subprocess.call(command, shell=True):
            raise ValueError
    except Exception:
        return 'There was an error when running "{0}".'.format(command)

    # check installation
    if not os.path.exists(os.path.join(metassistant.PATH, 'metaproject', args.name)):
        return '''I am not sure why the directory "{0}" was not created, 
even though "django-admin" returned successfully.'''.format(args.name)

    return 'All good'
