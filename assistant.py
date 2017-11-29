""" Metassistant interface to abstract package calls

    Small list of commands to make UX as friendly as possible: [init, app, run]

    For help, use "python assistant.py --help" or "python assistant.py app --help" etc. """

import argparse

import metassistant.commands

parser = argparse.ArgumentParser(description='Metassistant interface to abstract all package calls')
subparsers = parser.add_subparsers(help='what can I help you with?')

# init command
init_parser = subparsers.add_parser('init', help='build the project, should only be run once')
init_parser.set_defaults(func=metassistant.commands.init)

# app command
app_parser = subparsers.add_parser('app', help='create a new app, should only be run after init')
app_parser.add_argument('name', help='what should I call this app?', type=str)
app_parser.add_argument('-a', '--advanced', help='show an advanced options file', action='store_true')
app_parser.set_defaults(func=metassistant.commands.app)

# run command
run_parser = subparsers.add_parser('run', help='run the server')
run_parser.add_argument('--port', help='port to listen on', type=int, default=80)
run_parser.add_argument('--public', help='listen for public connections', action='store_true')
run_parser.set_defaults(func=metassistant.commands.run)

args = parser.parse_args()
print(args.func(args))

