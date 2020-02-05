#!/usr/bin/python
from markdown import markdown
import pdfkit
import codecs
from markdown2 import Markdown
from os import listdir

def build_html_file(content, title="German Lessons"):
    output_content = """
    <!DOCTYPE html>
    <html>

    <head>
      <meta charset="UTF-8">
      <title>{title}</title>
    </head>
    <body>
    {content}
    </body>

    </html>
    """.format(title=title,content=content)
    return output_content

# our target
all_lessons_html_file = 'all_lessons.html'
all_lessons_pdf_file = 'german_lessons.pdf'

all_markdown_content = ''
lesson_files = [f for f in listdir('./lessons') if f.endswith('.md')]

for lesson_file in lesson_files:
    input_file = codecs.open('./lessons/' + lesson_file, mode='r', encoding='utf-8')
    markdown_text = input_file.read()
    all_markdown_content += markdown(markdown_text)

markdown_content_to_html_content = Markdown().convert(all_markdown_content)
all_lessons_html_content = build_html_file(markdown_content_to_html_content)
all_lessons_html = open(all_lessons_html_file, 'w', encoding='utf-8')
all_lessons_html.write(all_lessons_html_content)
all_lessons_html.close()

# all lessons html to pdf
pdfkit.from_file(all_lessons_html_file, all_lessons_pdf_file)
