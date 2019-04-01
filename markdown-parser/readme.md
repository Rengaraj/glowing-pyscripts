## Markdown parser

I wriiten this code to parse markdown headings in
to markdown task list.

Basically converting like below

```
## <name>    - [ ] <name>
```

It will render like this when we put in github issue

- [ ] <name>


### Usage

I have a keynote.txt file, it has heading as name of
keynote speaker for PyCon India 2019.

We want to create issue with all names in order to send invitation to
keynote speaker for PyCon India 2019.

Traversing the entire file and copy pasting all the lines I felt boring job.

parse_keynote.py will parse the entire file and convert the heading in to markdown task
list in stdout. Then we need to copy paste the console output to the github issue.

```
rengaraj@rengaraj:~/glowing-pyscripts/markdown-parser$ python parse-keynote.py
- [ ] <Name1>

till the last line having the heading start with ##


```


