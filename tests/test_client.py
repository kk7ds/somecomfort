import os
import requests
import unittest
try:
    from unittest import mock
except ImportError:
    import mock

import betamax

from somecomfort import SomeComfort
import somecomfort


class RecordedTest(unittest.TestCase):
    def setUp(self):
        self.username = os.environ.get('SCUSER', 'fakeuser')
        self.password = os.environ.get('SCPASS', 'fakepass')
        self.location = int(os.environ.get('SCLOC', '1'))
        self.device = int(os.environ.get('SCDEV', '2'))
        with betamax.Betamax.configure() as config:
            config.define_cassette_placeholder(
                '<USER>', self.username.replace('@', '%40'))
            config.define_cassette_placeholder(
                '<PASS>', self.password)
            config.define_cassette_placeholder(
                '<LOC>', str(self.location))
            config.define_cassette_placeholder(
                '<DEV>', str(self.device))
            config.cassette_library_dir = 'tests/cassettes'
        self.session = requests.Session()
        self.patchers = []
        self.patchers.append(
            mock.patch('somecomfort.SomeComfort._get_session'))

        for patcher in self.patchers:
            patcher.start()

        SomeComfort._get_session.return_value = self.session

    def _get_device(self, client):
        return client.locations_by_id[self.location].devices_by_id[self.device]

    def tearDown(self):
        for patcher in self.patchers:
            patcher.stop()

    def test_login(self):
        recorder = betamax.Betamax(self.session)
        with recorder.use_cassette('basic'):
            c = SomeComfort(self.username, self.password)

        self.assertIn(self.location, c.locations_by_id)
        self.assertIn(self.device,
                      c.locations_by_id[self.location].devices_by_id)
        device = self._get_device(c)
        self.assertEqual('THERMOSTAT', device.name)

    def test_device_attributes(self):
        recorder = betamax.Betamax(self.session)
        with recorder.use_cassette('basic'):
            c = SomeComfort(self.username, self.password)

        device = self._get_device(c)
        self.assertEqual('THERMOSTAT', device.name)
        self.assertEqual(self.device, device.deviceid)
        self.assertFalse(device.fan_running)
        self.assertTrue(device.is_alive)
        self.assertEqual(77.0, device.setpoint_cool)
        self.assertEqual(58.0, device.setpoint_heat)
        self.assertEqual(58.0, device.current_temperature)
        self.assertEqual('F', device.temperature_unit)
        self.assertEqual('heat', device.system_mode)
        self.assertEqual('circulate', device.fan_mode)

    def _test_device_set_attribute(self, attr, value):
        recorder = betamax.Betamax(self.session)
        with recorder.use_cassette('set-attr-%s-%s' % (attr, value)):
            c = SomeComfort(self.username, self.password)
            device = self._get_device(c)
            setattr(device, attr, value)
            self.assertEqual(value, getattr(device, attr))

    def test_device_set_attributes(self):
        settings = {
            'setpoint_heat': 56,
            'setpoint_cool': 78,
            'fan_mode': 'auto',
            'system_mode': 'off',
        }
        for attr, value in settings.items():
            self._test_device_set_attribute(attr, value)

    def test_login_failed(self):
        recorder = betamax.Betamax(self.session)
        with recorder.use_cassette('badlogin'):
            self.assertRaises(somecomfort.AuthError,
                              SomeComfort, 'nosuchuser',
                              'definitelynotapassword')
