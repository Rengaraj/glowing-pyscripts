def parse_line(lines, delimiter):
    stripped = []
    for line in lines:
        if line[0:2] == delimiter:
            stripped.append(line.strip(delimiter + " "))
    return stripped


if __name__ == "__main__":
    with open("keynote.txt", "r") as key_file:
        lines = key_file.readlines()

    parsed = parse_line(lines, "##")
    for line in parsed:
        print " - [ ] " + line
    
