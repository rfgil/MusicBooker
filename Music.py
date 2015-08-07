# coding=utf-8

CHORUS_INDENTIFIER = "{CHORUS}"


class Music():
    chorus = ''
    chorus_chords = ''

    verse = []
    verse_chords = []

    has_chorus = False
    verse_before_chorus = 0
    start_with_chorus = False

    name = ''
    subtitle = ''

    def n_verse(self):
        """
        Returns the ammount of verses this music has.

        @return Integer
        """
        return len(self.verse)

    def insert_in_string(self, str, substr, pos):
        """
        Inserts a substring in a string at a given position.

        @param str          String to insert substring in              
        @param substr       Substring to insert
        @param pos          Position of string where substring is going to be placed

        @return String
        """
        if pos > len(str):
            for i in range(len(str), pos):
                str += ' '
            return str + substr
        else:
            return str[:pos] + substr + str[pos:]

    def is_chords(self, line):
        """
        Verifies if a given string is chords or lyrics.

        @param line         String to analyse

        @return Boolean     
        """
        if '#' in line:
            return True
        elif '  ' in line:
            return True
        else:
            return False

    def insert_chords(self, chords_line, chords_array):
        """
        Creates a string with the chords and lyrics mixed, according to LaTeX song package.

        @param chords_line      String with lyrics
        @param chords_array     Array with chords on the positon they are supposed to appear in the lyrics. Other positions should be empty.

        @return String
        """
        for i in range(len(chords_array) - 1, -1, -1):
            if chords_array[i] != '':
                spaces = 0
                for j in range(i):
                    spaces += len(chords_array[j])
                chords_line = self.insert_in_string(chords_line, '\\[' + chords_array[i] + ']', i + spaces)

        return chords_line

    def __init__(self, name, subtitle):
        my_file = open('source/' + name, encoding="utf-8")

        self.name = name[0].upper() + name[1:]  # Transforms the name in Proper case
        self.subtitle = subtitle

        self.chorus = ''
        self.chorus_chords = ''

        self.verse = []
        self.verse_chords = []

        self.has_chorus = False
        self.verse_before_chorus = 0
        self.start_with_chorus = False

        is_chorus = False
        current_estrofe = 0
        chords_array = []

        for line in my_file:
            line = line.rstrip()
            line_chords = line

            if self.is_chords(line):
                chords_array = line.split(' ')
                continue

            elif chords_array:  # If chords_array is not empty
                line_chords = self.insert_chords(line_chords, chords_array)
                chords_array = []

            if CHORUS_INDENTIFIER in line:
                is_chorus = True
                self.has_chorus = True
                if current_estrofe == 0:
                    self.start_with_chorus = True

            elif not line.strip():  # line is empty
                if is_chorus:
                    is_chorus = False
                else:
                    current_estrofe += 1

                if not self.has_chorus:  # Hasn't reached a chorus yet
                    self.verse_before_chorus += 1

            elif is_chorus:
                self.chorus += line + '\n'
                self.chorus_chords += line_chords + '\n'

            else:

                if len(self.verse) == current_estrofe:
                    self.verse.append(line + '\n')
                    self.verse_chords.append(line_chords + '\n')

                else:
                    self.verse[current_estrofe] += line + '\n'
                    self.verse_chords[current_estrofe] += line_chords + '\n'

        my_file.close()

    def write_tex(self, chords_file, lyrics_file):
        """
        Writes the song LaTeX code to a file.

        @param chords_file  Chords file
        @param lyrics_file  Lyrics file
        """
        musica_inic = "\\beginsong{%s}[by={%s}]\n\n"
        musica_fim = "\\endsong\n\n"

        chords_file.write(musica_inic % (self.name, self.subtitle))
        lyrics_file.write(musica_inic % (self.name, self.subtitle))

        for i in range(self.verse_before_chorus):
            chords_file.write('\\beginverse\n' + self.verse_chords[i] + '\\endverse\n\n')
            lyrics_file.write('\\beginverse\n' + self.verse[i] + '\\endverse\n\n')

        if self.has_chorus:
            chords_file.write('\\beginchorus\n' + self.chorus_chords + '\\endchorus\n\n')
            lyrics_file.write('\\beginchorus\n' + self.chorus + '\\endchorus\n\n')

        for i in range(self.verse_before_chorus, self.n_verse()):
            chords_file.write('\\beginverse\n' + self.verse_chords[i] + '\\endverse\n\n')
            lyrics_file.write('\\beginverse\n' + self.verse[i] + '\\endverse\n\n')

        chords_file.write(musica_fim)
        lyrics_file.write(musica_fim)
