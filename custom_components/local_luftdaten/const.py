from datetime import timedelta

from homeassistant.const import (
    CONF_HOST,
    CONF_NAME,
    CONF_RESOURCE,
    CONF_VERIFY_SSL,
    CONF_MONITORED_CONDITIONS,
    CONF_SCAN_INTERVAL,
    TEMP_CELSIUS
)

DOMAIN = "local_luftdaten"

DEFAULT_NAME = 'Luftdaten Sensor'
DEFAULT_RESOURCE = 'http://{}/data.json'
DEFAULT_VERIFY_SSL = True
DEFAULT_SCAN_INTERVAL = timedelta(minutes=3)

#Units of measurement
VOLUME_MICROGRAMS_PER_CUBIC_METER = 'µg/m3'

#Sensors
SENSOR_TEMPERATURE = 'temperature'
SENSOR_HUMIDITY = 'humidity'
SENSOR_BME280_TEMPERATURE = 'BME280_temperature'
SENSOR_BME280_HUMIDITY = 'BME280_humidity'
SENSOR_BME280_PRESSURE = 'BME280_pressure'
SENSOR_BMP_TEMPERATURE = 'BMP_temperature'
SENSOR_BMP_PRESSURE = 'BMP_pressure'
SENSOR_BMP280_TEMPERATURE = 'BMP280_temperature'
SENSOR_BMP280_PRESSURE = 'BMP280_pressure'
SENSOR_PM1 = 'SDS_P1'
SENSOR_PM2 = 'SDS_P2'
SENSOR_WIFI_SIGNAL = 'signal'
SENSOR_HTU21D_TEMPERATURE = 'HTU21D_temperature'
SENSOR_HTU21D_HUMIDITY = 'HTU21D_humidity'
SENSOR_SPS30_P0 = 'SPS30_P0'
SENSOR_SPS30_P2 = 'SPS30_P2'
SENSOR_SPS30_P4 = 'SPS30_P4'
SENSOR_SPS30_P1 = 'SPS30_P1'
SENSOR_PMS_P0 = 'PMS_P0'
SENSOR_PMS_P1 = 'PMS_P1'
SENSOR_PMS_P2 = 'PMS_P2'
SENSOR_HECA_TEMPERATURE = 'HECA_temperature'
SENSOR_HECA_HUMIDITY = 'HECA_humidity'
SENSOR_HPM_P1 = 'HPM_P1'
SENSOR_HPM_P2 = 'HPM_P2'

SENSOR_TYPES = {
    SENSOR_TEMPERATURE: ['Temperature', TEMP_CELSIUS, 'temperature'],
    SENSOR_HUMIDITY: ['Humidity', '%', 'humidity'],
    SENSOR_BME280_TEMPERATURE: ['Temperature', TEMP_CELSIUS, 'temperature'],
    SENSOR_BME280_HUMIDITY: ['Humidity', '%', 'humidity'],
    SENSOR_BME280_PRESSURE: ['Pressure', 'Pa', 'pressure'],
    SENSOR_BMP_TEMPERATURE: ['Temperature', TEMP_CELSIUS, 'temperature'],
    SENSOR_BMP_PRESSURE: ['Pressure', 'Pa', 'pressure'],
    SENSOR_BMP280_TEMPERATURE: ['Temperature', TEMP_CELSIUS, 'temperature'],
    SENSOR_BMP280_PRESSURE: ['Pressure', 'Pa', 'pressure'],
    SENSOR_PM1: ['PM10', VOLUME_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_PM2: ['PM2.5', VOLUME_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_WIFI_SIGNAL: ['Wifi signal', 'dBm', 'signal_strength'],
    SENSOR_HTU21D_TEMPERATURE: ['Temperature', TEMP_CELSIUS, 'temperature'],
    SENSOR_HTU21D_HUMIDITY: ['Humidity', '%', 'humidity'],
    SENSOR_SPS30_P0: ['PM1', VOLUME_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_SPS30_P2: ['PM2.5', VOLUME_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_SPS30_P4: ['PM4', VOLUME_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_SPS30_P1: ['PM10', VOLUME_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_PMS_P0: ['PM1', VOLUME_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_PMS_P1: ['PM10', VOLUME_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_PMS_P2: ['PM2.5', VOLUME_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_HECA_TEMPERATURE: ['Temperature', TEMP_CELSIUS, 'temperature'],
    SENSOR_HECA_HUMIDITY: ['Humidity', '%', 'humidity'],
    SENSOR_HPM_P1: ['PM10', VOLUME_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_HPM_P2: ['PM2.5', VOLUME_MICROGRAMS_PER_CUBIC_METER, None],
}
