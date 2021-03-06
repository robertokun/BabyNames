EOL = '\n'
TAB = '\t'

RANK_INDEX = 0
BOY_INDEX = 1
GIRL_INDEX = 2
PATH_TO_HTML_FILES = ''  # html_input/'
#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it (** DONE **)
 -Extract the names and rank numbers and just print them (** Done **)
 -Get the names data into a dict and print it (** DONE **)
 -Build the [year, 'name rank', ... ] list and print it (** DONE **)
 -Fix main() to use the extract_names list (** DONE **)
"""

def extract_names(filename, summary):
    boynames = {}
    girlnames = {}
    inputFile = open(PATH_TO_HTML_FILES + filename, 'rU')
    fileString = inputFile.read()
    matched_names = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', fileString)

    for name_tuple in matched_names:
        boynames[name_tuple[BOY_INDEX]] = name_tuple[RANK_INDEX]
        girlnames[name_tuple[GIRL_INDEX]] = name_tuple[RANK_INDEX]

    baby_names = []
    for name in boynames:
        baby_names.append(name + ' ' + boynames[name])
    for name, rank in girlnames.iteritems(): # for name in boynames: or for name, rank in girlnames.iteritems(): can be used!
        baby_names.append(name + ' ' + rank)
    baby_names.sort()
    popularity_variable = Find(r'Popularity\sin\s(\d\d\d\d)', fileString)
    print popularity_variable
    print EOL.join(baby_names)
    output_list = [popularity_variable] + baby_names
    if summary:
        with open(filename + '.summary', 'w') as output_file:
            output_file.write(EOL.join(output_list))
            output_file.close()
    return output_list

    """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """

def Find(pat, text):
    first_match = re.findall(pat, text)[0]
    return first_match


def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)

    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    filenames = args[0:]
    for name_of_file in filenames:
        extract_names(name_of_file, summary)

if __name__ == '__main__':
    main()

    # Part B
    #
    # Suppose instead of printing the text to standard out, we want to write files containing the text.
    # If the flag --summaryfile is present, do the following: for each input file 'foo.html', instead
    # of printing to standard output, write a new file 'foo.html.summary' that contains the summary
    # text for that file.
    #
    # Once the --summaryfile feature is working, run the program on all the fiels using * like this:
    # "./babynames.py --summaryfile baby*.html". This generates all the summaries in one step.
    # (The standard behavior of the shell is that it expands the "baby*.html" pattern into the list
    # of matching filenames, and then the shell runs babynames.py, passing in all those filenames
    # in the sys.argv list.)
    #
    # With the data organized into summary files, you can see patterns over time with shell commands, like this:
    #
    # $ grep 'Trinity ' *.summary
    # $ grep 'Nick ' *.summary
    # $ grep 'Miguel ' *.summary
    # $ grep 'Emily ' *.summary
    # Regular expression hints -- year: r'Popularity\sin\s(\d\d\d\d)' names: r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>'

