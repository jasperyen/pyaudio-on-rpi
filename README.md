# pyaudio-on-rpi

### 透过miniconda安装python
https://gist.github.com/jasperyen/237717b0890fc958360d517eb10f9530#file-install-miniconda-on-pi-md

### 安装pyaudio
```
pi@raspberrypi:~ $ sudo apt-get install portaudio19-dev

pi@raspberrypi:~ $ pip install pyaudio
```

### 测试录音和播放
```
pi@raspberrypi:~ $ git clone https://github.com/jasperyen/pyaudio-on-rpi.git

pi@raspberrypi:~ $ cd pyaudio-on-rpi/

pi@raspberrypi:~/pyaudio-on-rpi $ python play.py

pi@raspberrypi:~/pyaudio-on-rpi $ python record.py
```

### 叁考
 - https://raspberrypi.stackexchange.com/questions/84666/problem-on-installing-pyaudio-on-raspberry-pi
 - https://dolby.io/blog/capturing-high-quality-audio-with-python-and-pyaudio
