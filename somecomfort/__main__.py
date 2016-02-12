import argparse
import sys

import prettytable

import somecomfort


def find_device(client, dev):
    for location in client.locations_by_id.values():
        for device in location.devices_by_id.values():
            if dev is None or dev == device.deviceid:
                return device


def main():
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
    args = parser.parse_args()

    if not args.username or not args.password:
        print('Error: username and password are required. Try -h')
        return 1

    client = somecomfort.SomeComfort(args.username, args.password)
    device = find_device(client, args.device)

    for thing in number_things + string_things:
        value = getattr(args, 'set_%s' % thing)
        if value is not None:
            setattr(device, thing, value)
            return 0

    for thing in readonly_things + number_things + string_things:
        isset = getattr(args, 'get_%s' % thing)
        if isset:
            print(getattr(device, thing))
            return 0

    t = prettytable.PrettyTable(('Location', 'Device', 'Name'))
    for locid, location in client.locations_by_id.items():
        for devid, device in location.devices_by_id.items():
            t.add_row([locid, devid, device.name])
    print(t)


if __name__ == '__main__':
    sys.exit(main())
