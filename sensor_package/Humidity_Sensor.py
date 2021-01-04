#!/usr/bin/python
# Author:Louis Ding
# import RPi.GPIO as GPIO
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
GPIO = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIO)

def getTemperature():
    if temperature is not None:
        return temperature
    else:
        return 'Temperature Error'
    # print('溫度 = {0:0.1f}*C'.format(self.temperature))

def getHumidity():
    if humidity is not None:
        return humidity
    else:
        return 'Humidity error'
    # print('濕度 = {0:0.1f}*C'.format(self.humidity))

def getTemperature_and_Humidity():
    if temperature is not None and humidity is not None:
        return '溫度 = {0:0.1f}*C 濕度 = {1:0.1f}%'.format(temperature, humidity)
    # print('溫度 = {0:0.1f}*C 濕度 = {1:0.1f}%'.format(self.temperature, self.humidity))
    else:
        return '讀取失敗，請重新嘗試!'
    # print('讀取失敗，請重新嘗試!')