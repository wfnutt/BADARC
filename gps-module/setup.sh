#!/bin/sh

DOCKER_IMAGE=gps-module:workshop

# Grab documentation from GPS module manufacturer
wget -Nnv -P docs https://content.u-blox.com/sites/default/files/documents/MAX-M8_ProductSummary_UBX-16008997.pdf
wget -Nnv -P docs https://content.u-blox.com/sites/default/files/documents/MAX-M8-FW3_DataSheet_UBX-15031506.pdf
wget -Nnv -P docs https://content.u-blox.com/sites/default/files/MAX-M8_HardwareIntegrationManual_%28UBX-13004876%29.pdf
wget -Nnv -P docs https://content.u-blox.com/sites/default/files/products/documents/u-blox8-M8_ReceiverDescrProtSpec_UBX-13003221.pdf

sudo /bin/sh -c "docker build -t ${DOCKER_IMAGE} ./docker \
                && docker run -it --device=/dev/ttyUSB2 \
                          -v $(pwd)/docs:/home/badarc/gps-module/docs \
                          -v $(pwd)/example:/home/badarc/gps-module/example \
                          ${DOCKER_IMAGE}"
