import time
t = time.time()

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_for_filename

def hl(code,pl,font=None):
    lexer = get_lexer_by_name(pl)
    formatter = get_formatter_for_filename('.html',linenos=True)
    result = highlight(code,lexer,formatter)
    if font:
        result = '<span style="font-size:'+str(font)+'px;">'+result+'</span>'
    css = get_formatter_for_filename('.html',style='emacs').get_style_defs('.highlight')
    print css
    return result

code = """
import xmltodict, json, requests
from pprint import pprint

website_url = 'http://radiusofcircle.blogspot.com/sitemap.xml'

content = requests.get(website_url)

#Read all the data from the content
website_text = content.text

#Using the xmltodict to get the dict as string
webJson = json.dumps(xmltodict.parse(website_text))

urlset = json.loads(webJson)


urls = urlset['urlset']['url']

print(len(urls))
for element in urls:
    url = element['loc']
    r = requests.get(url)
    for line in r.iter_lines():
        if '<title>' in line:
            line = line.strip()
            print '<a href="'+url+'" >'+line[7:-8]+'</a><br /><br />\n'

"""

pl = 'python'

print hl(code,pl,30)
print time.time()-t
    
