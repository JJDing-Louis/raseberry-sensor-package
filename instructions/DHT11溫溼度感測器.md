# DHT11溫溼度感測器
---
## 1.裝置介紹
![[DHT11溫溼度感測器.jpg]]

---
## 2.接線
![[DHT11溫溼度感測器(接線).png]]
### 說明:
5V 接 5V
GND 接 GND
Data 接 GPIO4 (pin7)

---
## 3. 使用說明
### 封包安裝:
在raseberry pi4 進入 command line
<pre><code>sudo pip3 install Adafruit_DHT<code></pre>
### 程式碼:
<pre><code>
#!/usr/bin/python  
# Author:Louis Ding  
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
            # print('溫度 = {0:0.1f}*C 濕度 = {1:0.1f}%'.format(self.temperature, self.humidity)) else:  
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
<code></pre>
### 方法說明:
getTemperature() => 回傳浮點數型別的"溫度"  
getHumidity() => 回傳浮點數型別的"濕度"  
getTemperature_and_Humidity() => 回傳文字型別的"溫度"與"濕度"  
---

## 4. 參考資料
1.[Raspberry Pi 3使用DHT11進行溫度與濕度監測](https://sites.google.com/site/zsgititit/home/raspberry-shu-mei-pai/raspberry-shi-yongdht11jin-xing-wen-du-yu-shi-du-jian-ce)  <br />
2.[[筆記]Arduino實驗十一:DHT11數字溫濕度傳感器](https://a091234765.pixnet.net/blog/post/400005313-%5b%e7%ad%86%e8%a8%98%5darduino%e5%af%a6%e9%a9%97%e5%8d%81%e4%b8%80%3adht11%e6%95%b8%e5%ad%97%e6%ba%ab%e6%bf%95%e5%ba%a6%e5%82%b3%e6%84%9f%e5%99%a8)  <br />
3.[RASPBERRY PI 3 MODEL B 與 DHT11 溫溼度感應器之應用](https://blog.everlearn.tw/%E7%95%B6-python-%E9%81%87%E4%B8%8A-raspberry-pi/raspberry-pi-3-model-b-%E8%88%87-dht11-%E6%BA%AB%E6%BA%BC%E5%BA%A6%E6%84%9F%E6%87%89%E5%99%A8%E4%B9%8B%E6%87%89%E7%94%A8)  </br>
4.[樹莓派連接DHT22偵測溫濕度](https://ithelp.ithome.com.tw/articles/10238029)
5.[樹莓派使用DHT11溫濕度傳感器](https://kknews.cc/zh-tw/digital/ea26b4q.html)  <br />

