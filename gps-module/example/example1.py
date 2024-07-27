#!/usr/bin/env python3

# Example code from the "pyubx2" project
# Ref: https://pypi.org/project/pyubx2/
#
# All we have changed is:
# - the default baud rate
# - the device used to access the module
# - addition of a loop to handle messages repeatedly
from serial import Serial
from pyubx2 import UBXReader, NMEA_PROTOCOL, UBX_PROTOCOL
with Serial('/dev/ttyUSB2', 9600, timeout=3) as stream:
  ubr = UBXReader(stream, protfilter=NMEA_PROTOCOL | UBX_PROTOCOL)
  while True:
    raw_data, parsed_data = ubr.read()
    if parsed_data is not None:
      print(parsed_data)
