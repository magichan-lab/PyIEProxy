# -*- coding: utf-8 -*-

import os
import argparse

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from logging import getLogger, StreamHandler, DEBUG, ERROR

try:
    from ieproxy import IEProxy
except OSError as e:
    import sys
    sys.exit()


PROG_NAME = 'ie_proxy'

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)


def proxy_on(**args):
    logger.debug("[PROXY ON]")
    proxy = IEProxy()
    if 'proxy' in args.keys() and args['proxy']:
        proxy.set_proxy(args['proxy'])
    proxy.enable()
    print_info(proxy)


def proxy_off(**args):
    logger.debug("[PROXY OFF]")
    proxy = IEProxy()
    proxy.disable()
    print_info(proxy)


def proxy_toggle(**args):
    logger.debug("[PROXY TOGGLE]")
    proxy = IEProxy()
    enable = proxy.is_enable()
    if enable:
        proxy.disable()
    else:
        proxy.enable()
    print_info(proxy)


def proxy_state(**args):
    logger.debug("[PROXY STATE]")
    proxy = IEProxy()
    print("PROXY SERVER : {}".format(proxy.get_proxy()))
    print("PROXY ENABLE : {}".format('ON' if proxy.is_enable() else 'OFF'))


def proxy_info(**args):
    logger.debug("[PROXY INFO]")
    print_info(IEProxy())


def print_info(proxy):
    print('{}'.format('ON' if proxy.is_enable() else 'OFF'))


def main():
    cmd_list = {'on': proxy_on,
                'off': proxy_off,
                'toggle': proxy_toggle,
                'info': proxy_info,
                'state': proxy_state}

    parser = argparse.ArgumentParser(prog=PROG_NAME)
    parser.add_argument('--proxy', type=str, default='', help='your proxy')

    parser.add_argument('-d', '--debug', action="store_true",
                        help='turn on debugging')

    parser.add_argument('command', type=str, default='info',
                        nargs='?', help='/'.join(cmd_list.keys()))

    args = parser.parse_args()

    if not args.debug:
        logger.setLevel(ERROR)

    if args.command in cmd_list.keys():
        cmd_list[args.command](proxy=args.proxy)
    else:
        parser.print_help()

    return

if __name__ == '__main__':
    main()
