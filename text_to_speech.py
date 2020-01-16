#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gtts import gTTS
import os

# define variables
# sentence  = " Have a good day!" you could input english sentence here.
sentence = u"大家恭喜" # 中文內容可以在這裏輸入.
file = "file.mp3"

# initialize tts, create mp3 and play
# tts = gTTS(sentence, lang='en')
tts = gTTS(sentence, lang='zh-tw')
tts.save(file)
os.system("mpg123 " + file)