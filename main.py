#!/usr/bin/python3
# coding=utf-8

from Music import Music
import os

# -----------------
# --- User Info ---
# -----------------

document_title = "Domingo V"
document_date = "18-Jan-2015"

# Format:   [[subtitle, filename]]
music_list = [["Entrada", 'caminhos para a vida'],
              ["Ato Penitencial", 'senhor tem piedade 1'],
              ["Aleluia", 'Aleluia 5'],
              ["Apresentacao dos Dons", 'estrela polar'],
              ["Santo", 'santo 6'],
              ["Pai Nosso", ''],
              ["Cordeiro de Deus", 'cordeiro de deus 2'],
              ["Comunhao", 'como o pai me amou'],
              ["Acao de Gracas", 'quero louvar-te'],
              ["Final", 'faz o que deus espera de ti']]

# -----------------------
# --- LaTeX Constants ---
# -----------------------

tex_inic = """\\documentclass[11pt]{article}

\\usepackage[cm]{fullpage}
\\usepackage[utf8]{inputenc}
\\usepackage[%s]{songs}

\\noversenumbers
\\obeyspaces

\\setlength\\baselineadj{-\\baselineskip}
\\renewcommand{\\chorusfont}{\\bfseries}

\\begin{document}

\\songsection{%s}
\\begin{songs}{}\n\n"""

tex_fim = """\\end{songs}

\\end{document}"""

# --------------------------
# --- Script starts here ---
# --------------------------

if not os.path.exists("result"):
    os.makedirs("result")

lyrics_file = open('result/lyrics.tex', 'w')
chords_file = open('result/chords.tex', 'w')

lyrics_file.write(tex_inic % ('lyric', document_title))
chords_file.write(tex_inic % ('chorded', document_title))

for music_item in music_list:
    subtitle = music_item[0]
    music_file = music_item[1]

    if not music_file == '':
        current_music = Music(music_file, subtitle)
        current_music.write_tex(chords_file, lyrics_file)

lyrics_file.write(tex_fim)
chords_file.write(tex_fim)

lyrics_file.close()
chords_file.close()
