# MusicBooker
Creates a lyric and a chorded songbook written in LaTeX, from a collection of files.

---

## Using MusicBooker

In the begining of the file `Music.py` is the following variable:

```python
CHORUS_INDENTIFIER = "{CHORUS}"
```

This is used to identify the chorus in the music file. Here is a example of a music file:

```
F#-                         A
Esta sede de Te encontrar em mim
C#-                                 D
de correr p’ra Ti, de estar junto de Ti.
  B-                              F#-
Guias pelos vales o decurso do meu rio,
D             E C-             F#-
única razão és Tu, único sustento, Tu,
  D                E             A
a minha vida existe porque existes Tu.

{CHORUS}
     F#-       D                 E F#-
Tudo gira à Tua volta em função de Ti;
      C#-          D           E
não importa quando, onde e o porquê.

Gira o firmamento sem nunca ter paz,
mas existe um ponto a brilhar para mim,
a Estrela Polar que fixa os meus passos,
a Estrela Polar és Tu, a estrela segura, Tu.
A minha vida existe, porque existes Tu.
```

According to the position where the chorus identifier was used, the following verse is going to be considered the chorus:

```
Tudo gira à Tua volta em função de Ti;
não importa quando, onde e o porquê.
```

---

## Runing MusicBooker
#### Windows

Install python3 and run `main.py`.

##### Linux

In order to run this script on a Linux system you just need to navigate to the folder containing `main.py` and run the following command:

    $ ./main.py

#### Console Interface

Once the application is running console will ask for the needed information, such as document title, date and music files.

    Tip: When selecting music file you can double press TAB for a list of available musics. And press TAB just once to autocomplete a music file name partially typed.

Once the application is finished it is generated a folder called `result`contains two files: `chords.tex` and `lyrics.tex`. These can be compiled to obtain the songbook, as explained next.

---

## Using the resulting files

In order to compile the resulting files of this script you need to have a [LaTeX](http://www.latex-project.org/) compiler and [LaTeX Songs package](http://songs.sourceforge.net/) installed on your computer.

#### Windows
On a Windows sytem you can use [MiKTeX](http://miktex.org/).

#### Linux
On a debian based Linux system you can use the following command line code to install the LaTeX compiler and Songs package:

    $ sudo apt-get install texlive-full
    
And this one to compile a file named `file.tex`.

    $ pdflatex file.tex

## The MIT License

The MIT License (MIT)

Copyright (c) 2015 Rafael Gil

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
