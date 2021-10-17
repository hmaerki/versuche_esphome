# https://esphome.io/guides/getting_started_hassio.html


## https://esphome.io/guides/getting_started_command_line.html

## https://esphome.io/guides/contributing.html#build


```bash
git clone https://github.com/esphome/esphome.git
git checkout 2021.9.3


```bash
pyenv shell 3.9.7
python3 docker/build.py --tag dev --arch amd64 --build-type docker build
# ==> esphome/esphome-amd64:dev

python3 docker/build.py --tag dev --arch amd64 --build-type ha-addon build
# ==> esphome/esphome-hassio-amd64:dev

python3 docker/build.py --tag dev --arch amd64 --build-type lint build
# ==> esphome/esphome-lint-amd64:dev
```


## Run home assistant
```bash
docker run --rm --privileged \
  -e TZ=Europe/Zurich \
  -v /home/maerki/versuche_esphome/maerki_hassio_config:/config \
  -it \
  --network=host \
  --name=homeassistant \
  esphome/esphome-hassio-amd64:dev

==> Does NOT work

docker run \
  --rm -it \
  --name homeassistant \
  --privileged \
  -e TZ=Europe/Zurich \
  -v /home/maerki/versuche_esphome/maerki_hassio_config:/config \
  --network=host \
  esphome/esphome-hassio-amd64

==> Does NOT work
```

```bash
docker run \
  --rm -it \
  --name homeassistant \
  --privileged \
  -e TZ=Europe/Zurich \
  -v /home/maerki/versuche_esphome/maerki_hassio_config:/config \
  --network=host \
  ghcr.io/home-assistant/home-assistant:stable
```

browser: http://localhost:8123

maerki/bliblablo

# Configure firmware and built using platformio

```bash
docker run --rm -it --network=host --name=esphome -v /home/maerki/versuche_esphome/maerki_config:/config --device=/dev/ttyUSB0 esphome/esphome-amd64:dev
docker run --rm -it --network=host --name=esphome -v /home/maerki/versuche_esphome/maerki_config:/config esphome/esphome-amd64:dev
docker exec -it esphome /bin/bash
```

browser: http://localhost:6052/

Now follow: https://esphome.io/guides/getting_started_command_line.html#creating-a-project

```bash
esphome run livingroom.yaml
```

# My devices

## Sonoff RE5V1C 5V DC Dry Contact Inching/Selflock Module
https://esphome.io/devices/sonoff.html
https://itead.cc/product/sonoff-re5v1c/
https://itead.cc/wp-content/uploads/2021/08/RE5V1C-Application-Guide.pdf


Information gathered via eWeLink:
SONOFF
RE5V1C
100035a8c2
70:03:9F:74:34:9F
FW: PSF-801-GL

### Flashing
https://templates.blakadder.com/sonoff_RE5V1C.html
https://tasmota.github.io/docs/Getting-Started/#hardware-preparation

## SONOFF DUALR3 Dual Relay Module DIY MINI Power Metering Smart Switch Two Way Smart Home Control

https://esphome.io/devices/sonoff.html#sonoff-pow-r2
https://sonoff.tech/product-review/tutorial/how-to-pair-sonoff-smart-devices-with-ewelink-app/
https://templates.blakadder.com/sonoff_DUALR3_v2.html
https://community.home-assistant.io/t/the-new-sonoff-dualr3/286682/6
https://www.espthings.io/index.php/2021/03/01/the-new-sonoff-dual-r3-is-here/
https://www.espthings.io/index.php/2021/10/03/power-metering-for-the-sonoff-dual-r3-r1-6-using-esphome/

### esphome
cp -r esphome_components/components/* esphome/esphome/components/
cp https://github.com/berfenger/esphome_components/blob/main/example_sonoff_dual_r3_v1.yaml maerki_config/example_sonoff_dual_r3_v1.yaml

### flashing

https://community.home-assistant.io/t/help-with-flashing-sonoff-dual-r3-please/297547

## ESP32 Developer Board

https://esphome.io/devices/nodemcu_esp32.html

```bash
pip install esptool

sudo adduser $USER dialout
python3 -m esptool --chip esp32 --port /dev/ttyUSB0 --baud 460800 erase_flash
==> Device crashed

python3 -m esptool --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z --flash_mode dio --flash_freq 40m 0x1000 esp32devboard.bin
==> Device crashed

picocom -b 115200 /dev/ttyUSB0
```

### https://github.com/esphome/esphome-flasher

```bash
cd esphomeflasher
Remove wxWidgets from requirement.stxt
pip install .

esphomeflasher --port /dev/ttyUSB0 esp32devboard.bin
esphomeflasher --port /dev/ttyUSB0 sonoff-dual-r3-v1.bin
esphomeflasher --port /dev/ttyUSB0 sonoff-re5v1c.bin
```

Vscode settings: https://github.com/esphome/esphome/blob/272ceadbb00d5980aa00c0ad5043878a330d275f/.devcontainer/devcontainer.json