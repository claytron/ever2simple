Introduction
============

Evernote_ and Simplenote_ are two online based note taking apps. Evernote
focuses more on giving the end user rich text and the ability to upload
voice clips and images for OCR. Simplenote on the other hand, as seen by
its name, is a much simpler approach. It just stores your plain text
notes, and that is it.

This package installs a script to help you migrate from Evernote into
Simplenote by exporting the notes as files. The script
will take an Evernote ``enex`` export and turn it into a ``json``, ``csv`` or
directory of ``*.txt`` files.

The html that is provided by Evernote is processed by the html2text_
library. This transforms the html into Markdown_. The Simplenote web UI
supports previewing notes in Markdown, so this works out nicely.

.. _Evernote: http://www.evernote.com
.. _Simplenote: http://simplenoteapp.com
.. _html2text: http://pypi.python.org/pypi/html2text/
.. _Markdown: http://daringfireball.net/projects/markdown/

Installation
------------

You can easily install this package using ``easy_install`` or ``pip`` as
follows (preferably in a virtualenv)::

    $ pip install -U ever2simple

Development Installation
------------------------

Clone this repository with ``git``::

    $ git clone https://github...

Enter the code directory::

    $ cd ever2simple

Install live preserving local changes to the code::

    $ pip install -e .

Usage
-----

Once it is installed, you will have a new executable available to you.
Before you can run the conversion, you will need to export your notes.
This can be done from the desktop client. You can select the notes you
want to export, then ``Export Notes to Archive...``, and select the
``enex`` format.

Once you have that, you can run the script on the file setting the ``--output``
to a directory and using ``dir`` as the parameter to ``--format``::

    $ ever2simple my_evernote.enex --output simplenote_dir --format dir

That will output each note in a ``*.txt`` file named by a number to the
``simplenote_dir`` directory (creating it if it doesn't exist).

You can now request Simplenote's support to enable Dropbox synchronization
to your account here: https://simplenote.com/contact-us/

Once they enable Dropbox synchronization for you, go to
https://app.simplenote.com/settings and configure it (in the last section).

After that, copy your converted ``*.txt`` note files to your Simplenote
directory inside your Dropbox and synchronize them from
https://app.simplenote.com/settings.


If you want to export to CSV you can pass ``csv`` to the ``--format``
parameter::

    $ ever2simple my_evernote.enex --output simplenote.csv --format csv

If you want to export to JSON you can pass ``json`` to the ``--format``
parameter (or just don't use that parameter as ``json`` is the default)::

    $ ever2simple my_evernote.enex --output simplenote.json --format json

Command Line Help
-----------------

The help given by running ``ever2simple -h``::


    usage: ever2simple [-h] [-o OUTPUT] [-f {json,csv,dir}] enex-file

    Convert Evernote.enex files to Markdown

    positional arguments:
      enex-file             the path to the Evernote.enex file

    optional arguments:
      -h, --help            show this help message and exit
      -o OUTPUT, --output OUTPUT
                            the path to the output file or directory, leave black
                            to output to the terminal (stdout) (default: None)
      -f {json,csv,dir}, --format {json,csv,dir}
                            the output format, json, csv or a directory (default:
                            json)


Notes and Caveats
-----------------

- Simplenote no longer supports JSON and CSV imports, only text files via
  Dropbox.

- Exporting to a directory will not preserve tags in the notes.

- This does not handle any attachments since simplenote doesn't support
  them. This script does not ignore the note that has attachments. This
  may make for some strange notes being imported with little to no text.

- Evernote's export looks like those horrific Microsoft Word html
  exports. You may want to cleanse the ``content`` data a bit before
  running the script. This is left as an exercise for the user.

- The notes in Evernote randomly contain unicode characters that aren't
  really harmful to you today, but may bite you in the rear later. This
  script just passes the buck, no extra cleansing of the text is done.
  The oddest character is a unicode space, why on earth do we need
  unicode spaces in our notes?1?!

Links
-----

PyPi
  http://pypi.python.org/pypi/ever2simple
Github
  http://github.com/claytron/ever2simple
Bug Reports
  http://github.com/claytron/ever2simple/issues

TODO
----

- Write some basic tests
- Unicode for ``DictWriter``
- Test on Python 3
