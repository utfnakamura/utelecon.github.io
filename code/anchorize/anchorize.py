#!/usr/bin/python3

import re

# Just an one-liner. Reinventing the wheel.
texturl = re.compile(r"(https?://[0-9A-Za-z/:%#\$&\?\(\)~\.=\+\-@]+)",re.MULTILINE)                                                                             
def anchorize(s):                                                                                                                                                        
    return texturl.sub('<a href="\\1" target="_blank rel=noopener">\\1</a>',s).replace("\n","<br />\n") 

def anchorize_file(in_file, out_file):
    rp = open(in_file)
    s = rp.read()
    rp.close()
    t = anchorize(s)
    wp = open(out_file, "w")
    wp.write(r"""
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf8">
</head>
<body>
%s
</body>
</html>
""" % t)
    wp.close()

def make_index(txts, htmls, out_file):
    wp = open(out_file, "w")
    wp.write("""
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf8">
</head>
<body>
<table border=1>
""")
    for txt,html in zip(txts, htmls):
        wp.write('<tr><td><a href="%s">%s</td><td><a href="%s">%s</td></tr>\n'
                 % (txt, txt, html, html))
    wp.write("""
</table>
</body>
</html>
""")
        
    
def main():
    n = 6
    txts = [ "p%d.txt" % i for i in range(n) ]
    htmls = [ "p%d.html" % i for i in range(n) ]
    for txt,html in zip(txts, htmls):
        anchorize_file(txt, html)
    make_index(txts, htmls, "index.html")

main()

