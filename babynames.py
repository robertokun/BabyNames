
EOL = '\n'
TAB = '\t'
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
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

# build filename to equal: baby1990.html through baby2008.html
def extract_names(filename):
    names = []
    boynames = {}
    girlnames = []
    inputFile = open('html_input/' + filename, 'rU')
    fileString = inputFile.read()
    first_match = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', fileString)
    if first_match:
        print "got one"
    else:
        print('Not Found')
    print first_match

    for i in first_match:
        k = 0
        while k < 1001:
            print i[k], i[k + 1] + EOL
            boynames[i[k]] = i[k + 1]
            k += 1
        # print i[0], i[3] + EOL
        # boynames.append(i[:0] + i[:1])
        # girlnames.append(i[:0] + i[:3])
    print boynames
    return first_match


# slice the list of tuples into a dictionary for Boys and separate one for girls

    """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
    # inputFile = open('html_input/' + filename, 'rU')
    # fileString = inputFile.read()
    # popularity_variable = re.search(r'Popularity\sin\s(\d\d\d\d)', fileString)
    # popularity_variable = Find(r'Popularity\sin\s(\d\d\d\d)', fileString)
    # print 'This is the filename:', filename + EOL
    # print popularity_variable
    # print 'The Extracted Year is: ' + popularity_variable + EOL
    # names_variable = Find(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', fileString)
    # print names_variable
    # print 'The names and ranks are: ' + names_variable[0] + TAB, 'Boy names:', names_variable[1] + TAB, 'Girl names: ', names_variable[2] + EOL
    # names.append(popularity_variable)
    # # print the statement: "rank: ## for names: $$$ and @@@"
    # girlnames = {names_variable[0]: names_variable[2]}
    # boynames = {names_variable[0]: names_variable[1]}
    # print names
    # print girlnames
    # print boynames
    # inputFile.close()

#TODO as what is issue with changing variable from first_match to match re: match as built-in?

def Find(pat, text):
    first_match = re.findall(pat, text)[0]
    if first_match:
        print "got one"
    else:
        print('Not Found')
    return first_match
    # newinputFile = open('html_input/' + filename, 'rU')
    # newfileString = newinputFile.read()
    # print re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', newfileString)
    # first_match = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', newfileString)
    # if first_match:
    #     print "got one"
    # else:
    #     print('Not Found')
    # newinputFile.close()
    # return first_match



# inputFile = open('html_input/' + filename, 'rU')
# for fileString in inputFile:
# print fileString,
# f.close()

def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    """TODO: ask how to make a loop that gives every filename instead of requesting each manually?
        TODO: go over dictionary vs lists for tuple conversion?"""
    # for i in filename:
    #
    extract_names('baby1990.html')
    # extract_names('baby1992.html')
    # extract_names('baby1994.html')
    # extract_names('baby1996.html')
    # extract_names('baby1998.html')
    # extract_names('baby2000.html')
    # extract_names('baby2002.html')
    # extract_names('baby2004.html')
    # extract_names('baby2006.html')
    # extract_names('baby2008.html')

    # For each filename, get the names, then either print the text output
    # or write it to a summary file


if __name__ == '__main__':
    main()



    # Part A
    #
    # In the babynames.py file, implement the extract_names(filename) function which takes the filename of a baby1990.html file and returns the data from the file as a single list -- the year string at the start of the list followed by the name-rank strings in alphabetical order. ['2006', 'Aaliyah 91', 'Abagail 895', 'Aaron 57', ...]. Modify main() so it calls your extract_names() function and prints what it returns (main already has the code for the command line argument parsing). If you get stuck working out the regular expressions for the year and each name, solution regular expression patterns are shown at the end of this document. Note that for parsing webpages in general, regular expressions don't do a good job, but these webpages have a simple and consistent format.
    #
    # Rather than treat the boy and girl names separately, we'll just lump them all together. In some years, a name appears more than once in the html, but we'll just use one number per name. Optional: make the algorithm smart about this case and choose whichever number is smaller.
    #
    # Build the program as a series of small milestones, getting each step to run/print something before trying the next step. This is the pattern used by experienced programmers -- build a series of incremental milestones, each with some output to check, rather than building the whole program in one huge step.
    #
    # Printing the data you have at the end of one milestone helps you think about how to re-structure that data for the next milestone. Python is well suited to this style of incremental development. For example, first get it to the point where it extracts and prints the year and calls sys.exit(0). Here are some suggested milestones:
    #
    # ***Extract all the text from the file and print it
    # ***Find and extract the year and print it
    # Extract the names and rank numbers and print them
    # Get the names data into a dict and print it
    # Build the [year, 'name rank', ... ] list and print it
    # Fix main() to use the ExtractNames list
    # Earlier we have had functions just print to standard out. It's more re-usable to have the function *return* the extracted data, so then the caller has the choice to print it or do something else with it. (You can still print directly from inside your functions for your little experiments during development.)
    #
    # Have main() call extract_names() for each command line arg and print a text summary. To make the list into a reasonable looking summary text, here's a clever use of join: text = '\n'.join(mylist) + '\n'
    #
    # The summary text should look like this for each file:
    #
    # 2006
    # Aaliyah 91
    # Aaron 57
    # Abagail 895
    # Abbey 695
    # Abbie 650
    # ...
    # Part B
    #
    # Suppose instead of printing the text to standard out, we want to write files containing the text. If the flag --summaryfile is present, do the following: for each input file 'foo.html', instead of printing to standard output, write a new file 'foo.html.summary' that contains the summary text for that file.
    #
    # Once the --summaryfile feature is working, run the program on all the fiels using * like this: "./babynames.py --summaryfile baby*.html". This generates all the summaries in one step. (The standard behavior of the shell is that it expands the "baby*.html" pattern into the list of matching filenames, and then the shell runs babynames.py, passing in all those filenames in the sys.argv list.)
    #
    # With the data organized into summary files, you can see patterns over time with shell commands, like this:
    #
    # $ grep 'Trinity ' *.summary
    # $ grep 'Nick ' *.summary
    # $ grep 'Miguel ' *.summary
    # $ grep 'Emily ' *.summary
    # Regular expression hints -- year: r'Popularity\sin\s(\d\d\d\d)' names: r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>'

