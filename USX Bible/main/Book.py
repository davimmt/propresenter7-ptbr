from bs4 import BeautifulSoup
from Bible import Bible
import requests
import urllib
import os

class Book:
    def getInfo(self, url, author, abbr):
        ## Get Chapter
        chapter = ''.join(i for i in url[-3:] if i.isdigit())

        ## Access web site
        url = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
        content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(content, 'html.parser')

        ## Get verses Text
        verseRaw = soup.find('article').find('div').find('div').find_all('p')

        for i in range(0, len(verseRaw)):
            unwantedTag = verseRaw[i].find('sup')
            unwantedTag.extract()

        verse = []
        for i in range(0, len(verseRaw)):
            verse.append(verseRaw[i].text.lstrip())

        return self.generateUSX(chapter, verse, author, abbr)

    def generateUSX(self, chapter, verses, author, abbr):
        fileName = abbr + ".usx"

        with open(fileName, 'a+', encoding='utf-8') as file:
            filesize = os.path.getsize(fileName)
            if filesize == 0:
                file.write('<?xml version="1.0" encoding="utf-8"?>\n'
                '<usx version="2.0">\n'
                '    <book code="' + abbr + '" style="id">' + author + '</book>\n'
                '    <para style="mt">' + author + '</para>\n')

            file.write('\n    <chapter number="' + chapter + '" style="c" />\n')

            for numVerse, verse in enumerate(verses):
                file.write(
                '       <para style="p">\n'
                '           <verse number="' + str(numVerse + 1) + '" style="v" />' + verse + '</para>\n'
                )

        return fileName