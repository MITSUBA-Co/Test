import pygame
import time

def play_sound(file_path):
    # pygameの初期化
    pygame.mixer.init()
    
    # 音声ファイルのロード
    pygame.mixer.music.load(file_path)
    
    # 音声の再生
    pygame.mixer.music.play()
    
    # 再生が終了するまで待機
    while pygame.mixer.music.get_busy():
        time.sleep(1)

if __name__ == "__main__":
    # 再生したい音声ファイルのパスを指定
    file_path = 'C://Users//mcj-ishizuka-ryota//Desktop//haizen_voice_playback.mp3'
    
    play_sound(file_path)
