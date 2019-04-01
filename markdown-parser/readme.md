## Markdown parser

I wriiten this code in to parse markdown headings in
to markdown task list.

Basically converting like below

```
## <name>    - [ ] <name>
```

It will render like this

## <name>    - [ ] <name>


### Usage

I have a keynote.txt file, it has heading as name of
keynote speaker for PyCon India 2019.

We want to create issue with all names in order send invitation for
keynote speaker.

Traversing the entire file and copy pasting all the lines I felt boring job.

parse_keynote.py will parse the entire file and convert the heading in to markdown task
list in stdout. Then we need to copy paste the console output to the github issue.

```
rengaraj@rengaraj:~/glowing-pyscripts/markdown-parser$ python parse-keynote.py
 - [ ] Wes McKinney

 - [ ] Victor Stinner

 - [ ] Luciano Ramalho

 - [ ] David Beazley

 - [ ] Adrian Holovaty

 - [ ] Roger Dingledine

  .
  .
  .
  .

till the last line having the heading start with ##


```