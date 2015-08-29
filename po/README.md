# Translation

These files are used to create the binary files in `i18n` folder, and those are used to translate the strings printed to the user by the application.

----

## How to use

First of all, all strings in python code that need translation must be wrapped inside the `_()` function.

Then it is time to generate `MusicBooker.po` file.

    $ xgettext --language=Python --keyword=_ --output=po/MusicBooker.pot `find . -name "*.py"`
    
With this file, each language translation file can be created, by changing `--locale`. For a portuguese translation file `--locale` should be `pt_PT`.

    $ msginit --input=MusicBooker.pot --locale=en_US

Inside each language translation file all strings must be translated. Then it is necessary to create the binary files.

    $ msgfmt --output-file=/i18n/en_CA/LC_MESSAGES/MusicBooker.mo en_US.po

----

## Detailed info

* [https://wiki.maemo.org/Internationalize_a_Python_application](https://wiki.maemo.org/Internationalize_a_Python_application)
* [http://www.learningpython.com/2006/12/03/translating-your-pythonpygtk-application/](http://www.learningpython.com/2006/12/03/translating-your-pythonpygtk-application/)
