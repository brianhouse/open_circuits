# firmware: https://micropython.org/download/esp32/
# with espnow: https://github.com/glenn20/micropython-espnow-images
# python -m pip install esptool --user
# choose the usbserial, not the SLAB

## This hasn't been working, but doing it through Thonny has. Don't know why.

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
    echo
    echo "Erasing..."
    python -m esptool --chip esp32 --port $PORT erase_flash
    echo "--> done"    
    echo "Flashing..."
    python -m esptool --chip esp32 --port $PORT --baud 460800 write_flash -z 0x1000 firmware-esp32-GENERIC.bin
    echo "--> done"
else
    echo "Exiting..."
fi
