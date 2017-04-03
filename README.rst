================================
Client for Honeywell Thermostats
================================

.. image:: https://travis-ci.org/kk7ds/somecomfort.svg?branch=master
    :target: https://travis-ci.org/kk7ds/somecomfort

**NOTE:** This is for the US model and website. Be aware that EU models are different!

Installing
----------

::

  $ pip install somecomfort
  $ somecomfort -h
  usage: somecomfort [-h] [--get_fan_mode] [--set_fan_mode SET_FAN_MODE]
                     [--get_system_mode] [--set_system_mode SET_SYSTEM_MODE]
                     [--get_setpoint_cool]
                     [--set_setpoint_cool SET_SETPOINT_COOL]
                     [--get_setpoint_heat]
                     [--set_setpoint_heat SET_SETPOINT_HEAT]
                     [--get_current_temperature] [--get_current_humidity]
                     [--get_outdoor_temperature] [--get_outdoor_humidity]
                     [--get_equipment_output_status] [--cancel_hold]
                     [--permanent_hold] [--hold_until HOLD_UNTIL] [--get_hold]
                     [--username USERNAME] [--password PASSWORD]
                     [--device DEVICE] [--login] [--devices]

  optional arguments:
    -h, --help            show this help message and exit
    --get_fan_mode        Get fan_mode
    --set_fan_mode SET_FAN_MODE
                          Set fan_mode
    --get_system_mode     Get system_mode
    --set_system_mode SET_SYSTEM_MODE
                          Set system_mode
    --get_setpoint_cool   Get setpoint_cool
    --set_setpoint_cool SET_SETPOINT_COOL
                          Set setpoint_cool
    --get_setpoint_heat   Get setpoint_heat
    --set_setpoint_heat SET_SETPOINT_HEAT
                          Set setpoint_heat
    --get_current_temperature
                          Get current_temperature
    --get_current_humidity
                          Get current_humidity
    --get_outdoor_temperature
                          Get outdoor_temperature
    --get_outdoor_humidity
                          Get outdoor_humidity
    --get_equipment_output_status
                          Get equipment_output_status
    --cancel_hold         Set cancel_hold
    --permanent_hold      Set permanent_hold
    --hold_until HOLD_UNTIL
                          Hold until time (HH:MM)
    --get_hold            Get the current hold mode
    --username USERNAME   username
    --password PASSWORD   password
    --device DEVICE       device
    --login               Just try to login
    --devices             List available devices

Using
-----

::

  $ somecomfort --username foo --password bar --login
  Success
  $ somecomfort --devices
  +----------+---------+---------------+
  | Location |  Device |      Name     |
  +----------+---------+---------------+
  | 0123456  | 1177223 | My Thermostat |
  +----------+---------+---------------+
  $ somecomfort --get_current_temperature
  58.0
  $ somecomfort --get_setpoint_heat
  58.0
  $ somecomfort --set_setpoint_heat 56
  $ somecomfort --get_setpoint_heat
  56.0

  
