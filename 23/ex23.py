import sys
script, input_encoding, error = sys.argv

# pay attention to the spelling difference in errors vs error
def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) # why should we return main() from itself?

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

# input_encoding and error will be used as "encoding" and "errors" respectively
main(languages, input_encoding, error)
