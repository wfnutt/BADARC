# BADARC
Bedford and District Amateur Radio Club

This repo contains demonstration/experimental code for the Bedford and District Amateur Radio Club,
located in the village of Ravensden near Bedford, United Kingdom.

## gps-module
Some toy examples provided as a get-you-working early bootstrap for use of
GPS modules from the likes of u-blox, with a default 9600baud serial interface.

The toy examples replicate some existing functionality available from tools such as gnssdump from the pygnssutils package,
but are intended as short examples for people new to Python, rather than examples of production-quality code for seasoned veterans.

The code and setup scripts currently assume that the USB serial device for comms to the GPS module is ``/dev/ttyUSB2``.
You will probably need to change the device to match your local circumstances.

### TL;DR
Run ``./setup.sh`` on Linux

When the container starts, run an example of your choice:
- ``example/example1.py``
- ``example/example2.py``

Any code changes made inside the container will be immediately available on the host machine, and will persist after the container exits.

``setup.sh`` downloads current .pdf documentation from the u-blox website, so that you can peruse their protocol description and work out what configuration you want to use for your project(s).
Examples to consider:
 - Increase the baud rate of the serial interface from 9600 to 115200
 - Switch off unwanted messaging
 - Configure the GPS module for your use case:
   - it is located on the ground
   - in a fixed position rather than some form of vehicle
   - consider use of alternate GNSS systems, as required
 - Write some additional code to convert the GPS coordinates
   - to a Maidenhead Locator such as IO92SE
   - to a WAB square such as TL05
     
### pyubx2
Rather than reinvent wheels, we simply leverage existing libraries such as https://pypi.org/project/pyubx2/ for the message encode/decode functionality.
