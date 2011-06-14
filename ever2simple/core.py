import os
import sys
from csv import DictWriter
from cStringIO import StringIO
from dateutil.parser import parse
from html2text import _html2text
from lxml import etree

FIELDNAMES = ['created', 'updated', 'content', 'tags']
SIMPLENOTE_DATE_FMT = '%h %d %Y %H:%M:%S'


class EverConverter(object):
    """Evernote conversion runner
    """

    def __init__(self, enex_file, simple_file=None):
        self.enex_file = enex_file
        self.stdout = False
        if simple_file is None:
            self.stdout = True
            simple_file = StringIO()
        self.simple_file = simple_file

    def _load_xml(self):
        try:
            xml_tree = etree.parse(self.enex_file)
        except (etree.XMLSyntaxError, ), e:
            print 'Could not parse XML'
            print e
            sys.exit(1)
        return xml_tree

    def prepare_notes(self):
        notes = []
        xml_tree = self._load_xml()
        # get all the notes nodes
        raw_notes = xml_tree.xpath('//note')
        for note in raw_notes:
            note_dict = {}
            title = note.xpath('title')[0].text
            # Use dateutil to figure out these dates
            # 20110610T182917Z
            created_string = note.xpath('created')[0].text
            updated_string = note.xpath('updated')[0].text
            note_dict['created'] = parse(created_string).strftime(
                SIMPLENOTE_DATE_FMT)
            note_dict['updated'] = parse(updated_string).strftime(
                SIMPLENOTE_DATE_FMT)
            tags = [tag.text for tag in note.xpath('tag')]
            note_dict['tags'] = " ".join(tags)
            note_dict['content'] = ''
            content = note.xpath('content')
            if content:
                html2plain = _html2text(None, "")
                html2plain.feed("<h1>%s</h1>" % title)
                html2plain.feed(content[0].text)
                # XXX: dict writer can't handle unicode in python 2
                note_dict['content'] = html2plain.close().encode(
                    'ascii', 'ignore')
            notes.append(note_dict)
        return notes

    def convert(self):
        notes = self.prepare_notes()
        # XXX: have an option to export as JSON here as well
        writer = DictWriter(self.simple_file, FIELDNAMES)
        writer.writerows(notes)
        if self.stdout:
            self.simple_file.seek(0)
            print self.simple_file.getvalue()


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print 'Usage: ever2simple <enex_file>'
        sys.exit(1)
    filepath = os.path.expanduser(args[0])
    if not os.path.exists(filepath):
        print 'File does not exist: %s' % filepath
        sys.exit(1)
    with open(filepath, 'rw') as enex_file:
        converter = EverConverter(enex_file)
        converter.convert()
    sys.exit()


if __name__ == '__main__':
    main()
