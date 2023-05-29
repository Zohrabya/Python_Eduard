import pygame

def play_music(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()


file_path = "path/to/your/music/file.mp3"

play_music(file_path)
pygame.time.wait(5000)

pause_music()
pygame.time.wait(2000)

resume_music()
pygame.time.wait(3000)

stop_music()
