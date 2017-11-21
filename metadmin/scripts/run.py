import argparse
import subprocess

parser = argparse.ArgumentParser(description='Metassistant wrapper for Django\'s \'runserver\'.')
parser.add_argument('--port', help='port to listen on', type=int, default=80)
parser.add_argument('--public', help='listen for public connections', action='store_true')
parser.add_argument('-f', '--force', help='force listening on port < 1024 and != 80', action='store_true')

args = parser.parse_args()

if args.port < 1 or args.port > 2 ** 16:
    print('This is not a port you can listen to, \'{port}\'. Try 1024 < port < 65536.'.format(port=args.port))
    quit()

if args.port != 80 and not args.force:
    if args.port < 1024:
        print('It is not recommended to listen on a port < 1024 and not 80. Use the [-f | --force] arg.')
        quit()

# todo: add logging with browserable terminal (only local!)
# terminal_port = 10777
# if args.port == terminal_port:
#     terminal_port += 1

command = 'python ../../metassistant/manage.py runserver {public}{port}'.format(public='0:' * int(args.public), port=args.port)

subprocess.run(command, shell=True)
