from docx import Document

class ProPresenter:
    def generateTxt(self, title, author, lyrics):
        fileName = (title + " - " + author + ".txt")
        with open(fileName, 'x', encoding='utf-8') as file:
            file.write(title + "\n")
            file.write(author + "\n\n")
            for p in range(len(lyrics)):
                file.write(lyrics[p])

        return fileName