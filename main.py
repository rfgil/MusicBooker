#!/usr/bin/python3
# coding=utf-8

from Music import Music
import os
import i18n
import readline

# Translation function declaration
_ = i18n.language.gettext


# Sets console tab autocompletion in source/ folder
current_dir = os.getcwd()
os.chdir("source/")
readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")


document_title = input(_("Select a file title: "))
document_date = input(_("Select a file date: "))

i = 1
music_list = []

print(_("---- (press enter when finnished) ----"))
while True:
    music_file = input(str(i) + _(": Enter music file: "))

    if not music_file:
        break
    elif not os.path.isfile(music_file):
        print(_("The entered file does not exist."))
        continue

    subtitle = input(str(i) + _(": Enter music subtitle: "))

    music_list += [[subtitle, music_file]]

    print("----")
    i += 1

# Changes cosole location back to root
os.chdir(current_dir)

# -----------------
# --- User Info ---
# -----------------

# document_title = "Domingo V"
# document_date = "18-Jan-2015"

# Format:   [[subtitle, filename]]
# music_list = [["Entrada", 'caminhos para a vida'],
#               ["Ato Penitencial", 'senhor tem piedade 1'],
#               ["Aleluia", 'Aleluia 5'],
#               ["Apresentacao dos Dons", 'estrela polar'],
#               ["Santo", 'santo 6'],
#               ["Pai Nosso", ''],
#               ["Cordeiro de Deus", 'cordeiro de deus 2'],
#               ["Comunhao", 'como o pai me amou'],
#               ["Acao de Gracas", 'quero louvar-te'],
#               ["Final", 'faz o que deus espera de ti']]

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

presentation_inic = """\\documentclass[11pt, aspectratio=169]{beamer}
\\usepackage[utf8]{inputenc}

\\setbeamertemplate{navigation symbols}{} %% remove navigation symbols
\\setbeamercolor{background canvas}{bg=black}
\\setbeamercolor{normal text}{bg=yellow,fg=white}
\\setbeamercolor{title}{fg=white}
%%\\setbeamercolor{frametitle}{fg=white}

\\usepackage[scaled=1.6]{helvet}
\\renewcommand\\familydefault{\\sfdefault} 


\\title{%s}
\\subtitle{%s}
\\date{} %% optional

\\begin{document}

\\begin{frame}
  \\titlepage
\\end{frame}

\\centering
\\obeylines
"""

presentation_fim = '\\end{document}'

# --------------------------
# --- Script starts here ---
# --------------------------

if not os.path.exists("result"):
    os.makedirs("result")

lyrics_file = open('result/lyrics.tex', 'w')
chords_file = open('result/chords.tex', 'w')
presentation_file = open('result/presentation.tex', 'w')

lyrics_file.write(tex_inic % ('lyric', document_title))
chords_file.write(tex_inic % ('chorded', document_title))
presentation_file.write(presentation_inic % (document_title, document_date))

for music_item in music_list:
    subtitle = music_item[0]
    music_file = music_item[1]

    if not music_file == '':
        current_music = Music(music_file, subtitle)
        current_music.write_tex(chords_file, lyrics_file)
        current_music.write_presentation(presentation_file)

lyrics_file.write(tex_fim)
chords_file.write(tex_fim)
presentation_file.write(presentation_fim)

lyrics_file.close()
chords_file.close()
