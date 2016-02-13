import argparse
import contextlib
import json
import os
import requests
import sys

import prettytable

import somecomfort


def get_or_set_things(client, args, device, settables, gettables):
    for thing in settables:
        value = getattr(args, 'set_%s' % thing)
        if value is not None:
            setattr(device, thing, value)
            return 0

    for thing in gettables:
        isset = getattr(args, 'get_%s' % thing)
        if isset:
            print(getattr(device, thing))
            return 0

    t = prettytable.PrettyTable(('Location', 'Device', 'Name'))
    for locid, location in client.locations_by_id.items():
        for devid, device in location.devices_by_id.items():
            t.add_row([locid, devid, device.name])
    print(t)


@contextlib.contextmanager
def persistent_session():
    statefile = os.path.join(os.path.expanduser('~'),
                             '.somecomfort')
    data = {}
    try:
        data = json.loads(open(statefile, 'rb').read().decode())
    except OSError:
        pass
    except:
        print('Failed to load data store: %s' % statefile)

    session = requests.Session()
    session.cookies.update(data.get('cookies', {}))
    try:
        yield session
    finally:
        data = {
            'cookies': dict(session.cookies.items()),
        }
        open(statefile, 'wb').write(json.dumps(data).encode())
        try:
            os.chmod(statefile, 0o600)
        except OSError:
            pass


def _main(session):
    number_things = ['setpoint_cool', 'setpoint_heat']
    string_things = ['fan_mode', 'system_mode']
    settable_things = {float: number_things, str: string_things}
    readonly_things = ['current_temperature']
    parser = argparse.ArgumentParser()
    for thingtype, thinglist in settable_things.items():
        for thing in thinglist:
            parser.add_argument('--get_%s' % thing,
                                action='store_const', const=True,
                                default=False,
                                help='Get %s' % thing)
            parser.add_argument('--set_%s' % thing,
                                type=thingtype, default=None,
                                help='Set %s' % thing)
    for thing in readonly_things:
        parser.add_argument('--get_%s' % thing,
                            action='store_const', const=True,
                            default=False,
                            help='Get %s' % thing)

    parser.add_argument('--username', help='username')
    parser.add_argument('--password', help='password')
    parser.add_argument('--device', help='device', default=None)
    parser.add_argument('--login', help='Just try to login',
                        action='store_const', const=True,
                        default=False)
    args = parser.parse_args()

    try:
        client = somecomfort.SomeComfort(args.username, args.password,
                                         session=session)
    except somecomfort.AuthError as ex:
        if not args.username and args.password:
            print('Login required and no credentials provided')
        else:
            print(str(ex))
        return 1

    if args.login:
        print('Success')
        return 0

    device = client.default_device
    if not device:
        if args.device:
            print('No such device `%s`' % args.device)
        else:
            print('No devices found')
        return 1

    try:
        return get_or_set_things(
            client, args, device,
            number_things + string_things,
            number_things + string_things + readonly_things)
    except somecomfort.SomeComfortError as ex:
        print('%s: %s' % (ex.__class__.__name__, str(ex)))


def main():
    with persistent_session() as session:
        _main(session)

if __name__ == '__main__':
    sys.exit(main())
