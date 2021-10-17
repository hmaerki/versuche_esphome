# Design of esphome

## pytest mixed with components

## Editor component

Used for devicepower: Codemirror

https://stackshare.io/stackups/ace-vs-codemirror

https://ace.c9.io/

esphome/esphome/config.py

## Yaml error messages including line numbers


esphome/esphome/config.py
```python
def line_info(config, path, highlight=True):
    """Display line config source."""
    if not highlight:
        return None
    obj = config.get_deepest_document_range_for_path(path)
    if obj:
        mark = obj.start_mark
        source = "[source {}:{}]".format(mark.document, mark.line + 1)
        return color(Fore.CYAN, source)
    return "None"
```

esphome/esphome/yaml_util.py
```python
class ESPHomeLoader(yaml.SafeLoader):  # pylint: disable=too-many-ancestors
    """Loader class that keeps track of line numbers."""
```

esphome/esphome/yaml_util.py
```python
# Check if it is a duplicate key
if key in seen_keys:
    raise yaml.constructor.ConstructorError(
        f'Duplicate key "{key}"',
        key_node.start_mark,
        "NOTE: Previous declaration here:",
        seen_keys[key],
    )
seen_keys[key] = key_node.start_mark
```

https://github.com/alecthomas/voluptuous

esphome/esphome/components/scd30/sensor.py
```python
CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(SCD30Component),
            cv.Optional(CONF_CO2): sensor.sensor_schema(
                unit_of_measurement=UNIT_PARTS_PER_MILLION,
                icon=ICON_MOLECULE_CO2,
                accuracy_decimals=0,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_TEMPERATURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_HUMIDITY): sensor.sensor_schema(
                unit_of_measurement=UNIT_PERCENT,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_HUMIDITY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_AUTOMATIC_SELF_CALIBRATION, default=True): cv.boolean,
            cv.Optional(CONF_ALTITUDE_COMPENSATION): cv.All(
                cv.float_with_unit("altitude", "(m|m a.s.l.|MAMSL|MASL)"),
                cv.int_range(min=0, max=0xFFFF, max_included=False),
            ),
            cv.Optional(CONF_AMBIENT_PRESSURE_COMPENSATION, default=0): cv.pressure,
            cv.Optional(CONF_TEMPERATURE_OFFSET): cv.temperature,
        }
    )
    .extend(cv.polling_component_schema("60s"))
    .extend(i2c.i2c_device_schema(0x61))
)
```

esphome/esphome/components/gpio/switch/__init__.py
```python
CONFIG_SCHEMA = switch.SWITCH_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(GPIOSwitch),
        cv.Required(CONF_PIN): pins.gpio_output_pin_schema,
        cv.Optional(CONF_RESTORE_MODE, default="RESTORE_DEFAULT_OFF"): cv.enum(
            RESTORE_MODES, upper=True, space="_"
        ),
        cv.Optional(CONF_INTERLOCK): cv.ensure_list(cv.use_id(switch.Switch)),
        cv.Optional(
            CONF_INTERLOCK_WAIT_TIME, default="0ms"
        ): cv.positive_time_period_milliseconds,
    }
).extend(cv.COMPONENT_SCHEMA)
```

esphome/esphome/components/gpio/binary_sensor/__init__.py
```python
CONFIG_SCHEMA = binary_sensor.BINARY_SENSOR_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(GPIOBinarySensor),
        cv.Required(CONF_PIN): pins.gpio_input_pin_schema,
    }
).extend(cv.COMPONENT_SCHEMA)
```

esphome/esphome/jsonschema.py

esphome/esphome/config_validation.py
## VSCode ??

.devcontainer/devcontainer.json

esphome/esphome/vscode.py

Plugin: Remote - Containers v0.202.4
==> Open vscode in folder ==> Reopen using container

```python
class EsphomeVscodeHandler(EsphomeCommandWebSocket):
    def build_command(self, json_message):
        return ["esphome", "--dashboard", "-q", "vscode", "dummy"]
```

## https://github.com/yaml/pyyaml/
https://github.com/yaml/pyyaml/blob/master/lib/yaml/constructor.py
construct_yaml_int

```python
import yaml
yaml.load("""
a: -05_5:7.6
b: -0x5_5:7.6
c: 0x5_5:7.6
d: 0x57
e: 1:2:3:4
f: -1:2:3:4
g: -01:2:3:4
h: 0xA01
j: 0XA01
k: 0xA_01
l: {1:2}
m: { 1:2}
n: { 1: 2}
o: { 1 :2}
p: { 1 : 2}
q: { 1_ : 2}
r: { _1 : 2}
""", Loader=yaml.SafeLoader)
```
