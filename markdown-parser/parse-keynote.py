def parse_line(lines, delimiter):
    """This will take lines as list collected from a markdown file and 
return list with removed markdown headings
    
    Arguments:
       lines: list - containing all the linese parsed from a file
       delimiter: string - markdown to be stripped from each line in the list
    
    Returns:
       list - function will return stripped lines of all headings
    """
    stripped = []
    level = len(delimiter)
    for line in lines:
        if line[0:level] == delimiter:
            stripped.append(line.strip(delimiter + " "))
    return stripped


if __name__ == "__main__":
    with open("keynote.md", "r") as key_file:
        lines = key_file.readlines()

    parsed = parse_line(lines, "##")
    for line in parsed:
        print " - [ ] " + line
    
