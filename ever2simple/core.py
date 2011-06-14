class EverConverter(object):
    """Evernote conversion runner
    """

    def __init__(self, exen_file, simple_file=None):
        self.exen_file = exen_file
        self.simple_file = simple_file

    def convert(self):
        print "oh hai"


def main():
    converter = EverConverter("fake file")
    converter.convert()


if __name__ == '__main__':
    main()
