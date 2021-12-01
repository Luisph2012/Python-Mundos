import time
from pygame import mixer


mixer.init()
mixer.music.set_volume(0.06)
mixer.music.load("cache/Poison.mp3")
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(1)

