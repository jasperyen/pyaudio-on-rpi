# pyaudio-on-rpi

### 透过miniconda安装python

```
pi@raspberrypi:~ $ wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
...
pi@raspberrypi:~ $ bash Miniconda3-latest-Linux-armv7l.sh
...
Do you wish the installer to prepend the Miniconda3 install location
to PATH in your /home/pi/.bashrc ? [yes|no]
[no] >>> yes

Prepending PATH=/home/pi/miniconda3/bin to PATH in /home/pi/.bashrc
A backup will be made to: /home/pi/.bashrc-miniconda3.bak


For this change to become active, you have to open a new terminal.

Thank you for installing Miniconda3!
pi@raspberrypi:~ $ source ~/.bashrc
pi@raspberrypi:~ $ conda config --add channels rpi
...
pi@raspberrypi:~ $ conda install python=3.6
...
pi@raspberrypi:~ $ python
Python 3.6.6 | packaged by rpi | (default, Sep  6 2018, 10:56:14)
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
此时python会预设使用conda安装的版本, 如果没有安装成功就会如下显示仍为内建的python2
```
pi@raspberrypi:~ $ python
Python 2.7.16 (default, Oct 10 2019, 22:02:15)
[GCC 8.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### 安装pyaudio
```
pi@raspberrypi:~ $ sudo apt-get install portaudio19-dev
...
pi@raspberrypi:~ $ pip install pyaudio
...
```

### 测试录音和播放
```
pi@raspberrypi:~ $ git clone https://github.com/jasperyen/pyaudio-on-rpi.git
...
pi@raspberrypi:~ $ cd pyaudio-on-rpi/
...
pi@raspberrypi:~ $ python play.py
...
pi@raspberrypi:~ $ python record.py
...
```
