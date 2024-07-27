#!/usr/bin/env python3

# Example 2
# Show time and current position, along with quality of fix and
# count of Satellite Vehicles

from serial import Serial
from pyubx2 import UBXReader, NMEA_PROTOCOL, UBX_PROTOCOL

day = None; month = None; year = None
time = None
lat = None; NS = None; lon = None; EW = None
alt = None; altUnit = None
quality = None; numSV = None

with Serial('/dev/ttyUSB2', 9600, timeout=3) as stream:
  ubr = UBXReader(stream, protfilter=NMEA_PROTOCOL | UBX_PROTOCOL)
  while True:
    raw_data, parsed_data = ubr.read()
    if parsed_data is None \
       or (parsed_data.identity != 'GPZDA' \
           and parsed_data.identity != 'GPGGA'):
      continue

    if parsed_data.identity == 'GPZDA':
      day = parsed_data.day
      month = parsed_data.month
      year = parsed_data.year
      time = parsed_data.time
      print(f'{time} {day}-{month}-{year} '
            f'lon:{lon} lat:{lat} alt:{alt} '
            f'qual:{quality} SVs:{numSV}')

    elif parsed_data.identity == 'GPGGA':
      lat = parsed_data.lat
      NS = parsed_data.NS
      lon = parsed_data.lon
      EW = parsed_data.EW
      quality = parsed_data.quality
      numSV = parsed_data.numSV
      alt = parsed_data.alt
      altUnit = parsed_data.altUnit

