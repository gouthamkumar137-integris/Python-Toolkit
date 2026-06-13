import markdown

with open('markdown-to-html/sample.md','r',encoding='utf-8') as file:
    markdown_text=file.read()

html_text=markdown.markdown(markdown_text)

with open('markdown-to-html/output.html','w',encoding='utf-8') as file:
    file.write(html_text)

print("Conversion Successfull! written to output.html")