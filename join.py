#!/usr/bin/python
import markdown

f = open('Januar 31, 2020.md', 'r')
html_markdown = markdown.markdown(f.read())
print(html_markdown)
