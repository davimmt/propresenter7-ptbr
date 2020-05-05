from bs4 import BeautifulSoup
from Bible import Bible
import requests
import urllib
import os

class Book:
    def getInfo(self, url, author, abbr):
        ## Get Chapter
        chapter = ''.join(i for i in url if i.isdigit())

        ## Access web site
        url = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
        content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(content, 'html.parser')

        ## Get verses Text
        verseRaw = soup.find_all('p')

        verse = []
        for unformatedVerse in verseRaw:
            formatedVerse = str(unformatedVerse).replace('<p>', '').replace('</p>', '')
            verse.append(formatedVerse)

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
                '           <verse number="' + str(numVerse + 1) + '" style="v",' + verse + '</para>\n'
                )

        return fileName

def main():
    for i in range(0, 66):
        for j in range(1, int(Bible().getbooksChapterNumber(i)) + 1):
            fileName = Book().getInfo("https://biblia.blog.br/acf/livro/" + Bible().getBooksPtBRName(i) + "/" + str(j), Bible().getBooksName(i), Bible().getBooksAbbreviation(i))

        with open(Bible().getBooksAbbreviation(i) + '.usx', 'a+', encoding='utf-8') as file:
            file.write('</usx>')
        
        print("\n" + fileName + " gerada com sucesso.")

main()
