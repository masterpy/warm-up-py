import html

print('Content-type: text/html\n')
print('<title>Reply Page</title>')

test = '<i>test italic</i>'
print(html.escape(test, quote=True))
