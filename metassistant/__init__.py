import socket
import os

PATH = os.path.dirname(os.path.abspath(__file__))

def settings(**kwargs):
    if 'INSTALLED_APPS' in kwargs:
        # todo: add config state check
        return get_apps()

    if 'ALLOWED_HOSTS' in kwargs:
        # todo: add config state check
        return ['localhost', '127.0.0.1'] \
               + [i[4][0] for i in socket.getaddrinfo(socket.gethostname(), None) if i[0] == socket.AF_INET]


def urls():
    # todo: add config state check
    return ['{0}.urls'.format(a) for a in get_apps()]


def get_apps():
    return os.listdir(os.path.join(os.path.dirname(__file__), os.pardir, 'apps'))
