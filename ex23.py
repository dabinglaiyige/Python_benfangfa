import sys
# use sys.argv to get encoding and error through command line
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    # read one line with file.readline()
    line = language_file.readline()

    if line:
        # call function print_line
        print_line(line, encoding, errors)
        # call self loop to handle the rest of line in the file 
        return main(language_file, encoding, errors)

# strip the given string and print the raw data and cooked data
def print_line(line, encoding, errors):
    # rip the line's blank
    next_lang = line.strip()
    # encode one line with the selected encoding, here is 'utf-8'
    raw_bytes = next_lang.encode(encoding, errors = errors)
    # decode one line which have been encode
    cooked_string = raw_bytes.decode(encoding, errors = errors)
    
    # parint the raw data compare with the cooked data
    print(raw_bytes, "<===>", cooked_string)


# open the file with encoding 'utf-8'
languages = open("languages.txt", encoding = "utf-8")

# call the function main
main(languages, encoding, error)
