================================
Client for Honeywell Thermostats
================================

**NOTE:** This is for the US model and website. Be aware that EU models are different!

Installing
----------

::

  $ pip install somecomfort
  $ somecomfort -h
  usage: somecomfort [-h] [--get-fan_mode] [--set-fan_mode SET_FAN_MODE]
                     [--get-system_mode] [--set-system_mode SET_SYSTEM_MODE]
                     [--get-setpoint_cool]
                     [--set-setpoint_cool SET_SETPOINT_COOL]
                     [--get-setpoint_heat]
                     [--set-setpoint_heat SET_SETPOINT_HEAT]
                     [--get-current_temperature] [--username USERNAME]
                     [--password PASSWORD] [--device DEVICE]
  
  optional arguments:
    -h, --help            show this help message and exit
    --get-fan_mode        Get fan_mode
    --set-fan_mode SET_FAN_MODE
                          Set fan_mode
    --get-system_mode     Get system_mode
    --set-system_mode SET_SYSTEM_MODE
                          Set system_mode
    --get-setpoint_cool   Get setpoint_cool
    --set-setpoint_cool SET_SETPOINT_COOL
                          Set setpoint_cool
    --get-setpoint_heat   Get setpoint_heat
    --set-setpoint_heat SET_SETPOINT_HEAT
                          Set setpoint_heat
    --get-current_temperature
                          Get current_temperature
    --username USERNAME   username
    --password PASSWORD   password
    --device DEVICE       device

Using
-----

::

  $ somecomfort --username foo --password bar
  +----------+---------+---------------+
  | Location |  Device |      Name     |
  +----------+---------+---------------+
  | 0123456  | 1177223 | My Thermostat |
  +----------+---------+---------------+
  $ somecomfort --username foo --password bar --get_current_temperature
  58.0
  $ somecomfort --username foo --password bar --get_setpoint_heat
  58.0
  $ somecomfort --username foo --password bar --set_setpoint_heat 56
  $ somecomfort --username foo --password bar --get_setpoint_heat
  56.0

  
