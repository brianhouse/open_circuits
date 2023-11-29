# firmware: https://micropython.org/download/esp32/
# with espnow: https://github.com/glenn20/micropython-espnow-images
# choose the usbserial, not the SLAB

if [[ $# -eq 0 ]]
  then
    echo "[PORT]"
    ls -la /dev/tty.*
    exit 1
fi
PORT=$1
echo $PORT
read -p "Erase $PORT [y/N]? " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "Flashing..."
    python -m esptool --chip esp32 --port $PORT --baud 115200 write_flash --flash_mode keep --flash_size keep --erase-all 0x1000 firmware-esp32-GENERIC.bin
    echo "--> done"
else
    echo "Exiting..."
fi
