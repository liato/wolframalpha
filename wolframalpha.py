#!/usr/bin/env python
import re
import urllib2

from lxml.html import document_fromstring, tostring

__version__ = '0.1.0'
baseurl = 'http://www88.wolframalpha.com/input/'


def texttable(plaintext):
    if not '\n' in plaintext:
        return plaintext
    
    copyfloppy = plaintext
    header = False
    firstrow = plaintext[:plaintext.find('\n')]
    
    if '|' not in firstrow:
        header = True
        plaintext = plaintext[plaintext.find('\n')+1:]
    
    table = [[f.strip() for f in e.split('|')] for e in plaintext.split('\n')]

    try:
        lens = [max(len(row[col]) for row in table)+2 for col in range(len(table[0]))]
    except IndexError:
        return copyfloppy
    
    ret = []
    if header:
        ret.append(center(firstrow,sum(lens) + len(table[0])-1))
    ret.extend('|'.join(center(e,lens[i]) for i,e in enumerate(row)) for row in table)
    return '\n'.join(ret)
    

def center(s, l):
    """Center a string s in a space of l characters.
       center("foo",5) -> " foo " and so on"""
    d = l-len(s)
    a,b = divmod(d,2)
    return '%s%s%s' % (a*' ', s, (a+b)*' ')
    
class WolframAlphaResult(object):
    def __init__(self, title, result, result_raw):
        self.title = title
        self.result = result
        self.result_raw = result_raw
        
    def __repr__(self):
        return '<WolframAlphaResult/%r>' % self.title
        

class WolframAlpha(object):
    def __init__(self, query, all=True):
        self.query = query
        self.results = []
        self.all = all
        self.update()
    
    def update(self):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.2) Gecko/2008091620 Firefox/3.0.2'),
                           ('Connection', 'Keep-Alive'),
                           ('Content-Type', 'application/x-www-form-urlencoded')]
        data = opener.open(baseurl+"?i="+urllib2.quote(self.query.encode('utf-8'))+"&asynchronous=%s&equal=Submit" % ('pod' if self.all else 'false')).read()
        data = data.replace('</body>', '').replace('</html>', '')
        if self.all:
            recalcurl = re.search("'(recalculate.jsp\?id=[^']*?)'", data, re.I)
            if recalcurl:
                recalcdata = opener.open(baseurl+recalcurl.group(1)).read()
            else:
                recalcdata = ""
            podurls = re.findall("'(pod.jsp\?id=[^']*?)'", data+recalcdata, re.I)
            if podurls:
                for url in podurls:
                    try:
                        poddata = str(opener.open(baseurl+str(url)).read())
                        data=data+poddata
                    except urllib2.HTTPError:
                        pass
        
        data = data + '</body></html>'
        data = document_fromstring(data)
        pods = data.cssselect('div.pod')
        for pod in pods:
            title = pod.cssselect('h2')
            if len(title) > 0:
                title = title[0].text_content()[:-1]
                text_raw = pod.cssselect('img')[0].get('alt')
                text = text_raw.replace("\\n","\n").replace("\\'s","'s")
                text = re.split(r'\n{2,}',text)
                output = []
                for p in text:
                    p = re.sub(r'(?im)(\n|^)\([^\n]+\)($|\n)', '', p)
                    p = re.sub(r'^\n+', '', p)
                    p = re.sub(r'\n+$', '', p)
                    if p:
                        output.append(texttable(p))
                if output:
                    text = '\n'.join(output)
                    self.results.append(WolframAlphaResult(title, text, text_raw))
            
            
if __name__ == "__main__":
    w = WolframAlpha("new york", True)
    from pprint import pprint
    pprint(w.results)
    for result in w.results:
        print result.title
        print repr(result.result_raw), '\n\n'