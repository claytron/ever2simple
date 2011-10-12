Introduction
============

Evernote_ and Simplenote_ are two online based note taking apps. Evernote
focuses more on giving the end user rich text and the ability to upload
voice clips and images for OCR. Simplenote on the other hand, as seen by
its name, is a much simpler approach. It just stores your plain text
notes, and that is it.

This package installs a script to help you migrate from Evernote into
Simplenote using the standard Simplenote import options. The script
will take an Evernote ``enex`` export and turn it into a ``json`` or
``csv`` file compatible with Simplenote.

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

Usage
-----

Once it is installed, you will have a new executable available to you.
Before you can run the conversion, you will need to export your notes.
This can be done from the desktop client. You can select the notes you
want to export, then ``Export Notes to Archive...``, and select the
``enex`` format.

Once you have that, you can run the script on the file::

    $ ever2simple my_evernote.enex > simplenote.json

Right now it just outputs the data to ``stdout``, so you can just output
directly to the file of your choosing (in this case ``simplenote.json``).

Now you can go to the Simplenote website and import the newly created
``json`` file.

Notes and Caveats
-----------------

There are some issues that you should be aware of when importing your
notes.

- There is already an Evernote importer on the Simplenote website, why
  did you write this? A: The current enex importer is very badly broken
  and duplicates your notes over and over. It is not recommended.

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
- Finish out the command line options
  - Output file
  - stdout option
  - csv output
- Unicode for ``DictWriter``
- Test on Python 3
