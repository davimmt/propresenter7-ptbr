from bs4 import BeautifulSoup
import requests
import urllib
import re

class Lyrics:
    def getLyrics(self, url): # Pegar as informações da música escolhida do site letra.mus.br
        request = urllib.request.urlopen(url)
        content = request.read()
        soup = BeautifulSoup(content, 'html.parser')

        head = soup.find('div', attrs={"class":"cnt-head_title"})
        body = soup.find('div', attrs={"class":"cnt-letra"})

        title = head.find('h1').text
        author = head.find('h2').text.strip()
        lyric = body.find_all('p')

        lyrics = []
        for p in lyric:
            lyrics.append(str(p)) 
        
        return title, author, self.formatLyrics(lyrics)
    
    def formatLyrics(self, lyrics): # O código do site impossibilita a formatação com o próprio BS4
        formatedLyrics = []
        for tags in lyrics:
            whiteSpace = re.sub('<p>|</br>', '', tags)
            lineBreak = re.sub('<br>|<br/>', '\n', whiteSpace)
            paragraphBreak = lineBreak.replace('</p>', '\n\n')
            formatedLyrics.append(paragraphBreak)
        lastParagraph = formatedLyrics[-1] # Guardar último parágrafo na variável
        formatedLyrics.pop() # Remover último parágrafo do array
        formatedLyrics.append(lastParagraph.replace('\n\n', '')) # Inserir último parágrafo no array, agora, sem a quebra de parágrafo (\n\n) no final
        
        return formatedLyrics
