from bs4 import BeautifulSoup
import requests
import urllib

class Lyrics:
    def getLyrics(self, url): # Pegar as informações da música escolhida do site letra.mus.br
        request = urllib.request.urlopen(url)
        content = request.read()
        soup = BeautifulSoup(content, 'html.parser')

        div = soup.find('div', attrs={"class":"cnt-letra"})

        title = soup.find_all('h1')[1].text
        author = soup.find_all('h2')[0].text
        author = author.replace('  ', '')

        lyrics = []

        for p in div:
            lyrics.append(str(p))

        return title, author, self.FormatLyrics(lyrics), self.FormatLyricsPropresenter7(lyrics)
    
    def FormatLyricsPropresenter7(self, lyrics): # Formatar a letra da música para gerar o arquivo pro ProPresenter 7
        processedLyrics = []

        for p in lyrics:
            openTag = p.replace('<p>', '')
            closeTag = openTag.replace('</p>', '')
            brTag = closeTag.replace('<br>', 'LB')
            uniqueBrTag = brTag.replace('<br/>', 'LB')
            closeBrTag = uniqueBrTag.replace('</br>', '')
            processedLyrics.append(closeBrTag)
        processedLyrics = processedLyrics[1:-1]
        lastParagraph = processedLyrics[-1].replace('\n\n', '')
        processedLyrics.pop()
        processedLyrics.append(lastParagraph)

        formatedLyrics = []

        for item in processedLyrics: # Dividir o array em parágrafos e quebras de linha
            splitted = item.split('LB')
            formatedLyrics.append(splitted)

        return formatedLyrics
    
    def FormatLyrics(self, lyrics): # Formatar a letra da música para gerar o arquivo pro ProPresenter 6 e pro PowerPoint
        formatedLyrics = []

        for p in lyrics:
            openTag = p.replace('<p>', '')
            closeTag = openTag.replace('</p>', '\n\n')
            brTag = closeTag.replace('<br>', '\n')
            uniqueBrTag = brTag.replace('<br/>', '\n')
            closeBrTag = uniqueBrTag.replace('</br>', '')
            formatedLyrics.append(closeBrTag)
        formatedLyrics = formatedLyrics[1:-1]
        lastParagraph = formatedLyrics[-1].replace('\n\n', '')
        formatedLyrics.pop()
        formatedLyrics.append(lastParagraph)
        
        return formatedLyrics
