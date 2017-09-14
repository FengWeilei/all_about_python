##from urllib.request import urlopen
##from bs4 import BeautifulSoup
##import re
##html = urlopen("http://www.pythonscraping.com/pages/page3.html")
##bsObj = BeautifulSoup(html,"html.parser")
##images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
##for image in images:
##    print(image["src"])


##from urllib.request import urlopen
##from bs4 import BeautifulSoup
##
##user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER0"
##headers = {'User-Agent':user_agent}
##
##req = urlopen("https://www.qiushibaike.com/8hr/page/2/")


from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdfFile)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    return content
pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()
