#!/usr/bin/python
# Author:Louis Ding
# import RPi.GPIO as GPIO
import Adafruit_DHT


class Humidity_Sensor():
    def __init__(self):
        sensor = Adafruit_DHT.DHT11
        GPIO = 4
        self.humidity, self.temperature = Adafruit_DHT.read_retry(sensor, GPIO)

    def getTemperature(self):
        if self.temperature is not None:
            return self.temperature
        else:
            return 'Temperature Error'
            # print('溫度 = {0:0.1f}*C'.format(self.temperature))

    def getHumidity(self):
        if self.humidity is not None:
            return self.humidity
        else:
            return 'Humidity error'
            # print('濕度 = {0:0.1f}*C'.format(self.humidity))

    def getTemperature_and_Humidity(self):
        if self.temperature is not None and self.humidity is not None:
            return '溫度 = {0:0.1f}*C 濕度 = {1:0.1f}%'.format(self.temperature, self.humidity)
            # print('溫度 = {0:0.1f}*C 濕度 = {1:0.1f}%'.format(self.temperature, self.humidity))
        else:
            return '讀取失敗，請重新嘗試!'
            # print('讀取失敗，請重新嘗試!')


"""
測試區域
sensor1 = Humidity_Sensor()
a = str(sensor1.getTemperature())
b = str(sensor1.getHumidity())
c = sensor1.getTemperature_and_Humidity()
print(type(a))
print(type(b))
print(type(c))
print(a)
print(b)
print(c)
"""