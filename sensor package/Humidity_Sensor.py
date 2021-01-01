#!/usr/bin/python
# Author:Louis Ding
#import RPi.GPIO as GPIO

import Adafruit_DHT

class Humidity_Sensor():
    def __init__(self):
        sensor = Adafruit_DHT.DHT11
        pin = 4
        self.humidity, self.temperature = Adafruit_DHT.read_retry(sensor, pin)

    def getTemperature(self):
        if self.temperature is not None:
            print('溫度 = {0:0.1f}*C'.format(self.temperature))

    def getHumidity(self):
        if self.humidity is not None:
            print('濕度 = {0:0.1f}*C'.format(self.humidity))

    def getTemperature_and_Humidity(self):
        if self.temperature is not None and self.humidity is not None:
            print('溫度 = {0:0.1f}*C 濕度 = {1:0.1f}%'.format(self.temperature, self.humidity))
        else:
            print('讀取失敗，請重新嘗試!')


"""
測試區域
sensor1=Humidity_Sensor()
sensor1.getTemperature()
sensor1.getHumidity()
sensor1.getTemperature_and_Humidity()
"""

