# Faça um programa em python que abra
# e reproduza um arquivo mp3.

import mp3play

filename = r'C:\Users\mateus\Downloads\musicao.mp3'
clip = mp3play.load(filename)
clip.play()
