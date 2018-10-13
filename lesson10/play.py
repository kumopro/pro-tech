import pygame.mixer
import time

def play(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(1)
    pygame.mixer.music.stop()
    pygame.mixer.quit()

play("speech_result.mp3")
