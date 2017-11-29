import subprocess
import sys

import os

import metassistant

def run(args):
    if args.port < 1 or args.port > 2 ** 16:
        return 'This is not a port you can listen to, \'{port}\'. Try 1024 < port < 65536.'.format(port=args.port)

    command = 'python {0} runserver '.format(os.path.join(metassistant.PATH, 'metaproject', 'manage.py'))

    if args.public:
        command += '0:{}'.format(args.port)
    else:
        command += str(args.port)

    try:
        # todo: make this asyncio.subprocess
        if 0 != subprocess.call(command):
            return 'The command: "{0}" did not complete successfully'.format(command)
    except OSError:
        return 'The command: "{0}" raised an OSError'.format(command)

    return 'All good'