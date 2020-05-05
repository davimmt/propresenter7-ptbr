from docx import Document

class ProPresenter:
    def generateDocx(self, title, author, lyrics):
        fileName = (title + " - " + author + ".docx")
        document = Document()
        document.add_paragraph(title)
        document.add_paragraph(author)
        document.add_paragraph()
        for paragraph in lyrics:
            for line in paragraph:
                document.add_paragraph(line)
            document.add_paragraph()
        document.save(fileName)
        return fileName

    def generateTxt(self, title, author, lyrics):
        fileName = (title + " - " + author + ".txt")
        with open(fileName, 'x', encoding='latin-1') as file:
            file.write(title + "\n")
            file.write(author + "\n\n")
            for p in range(len(lyrics)):
                file.write(lyrics[p])

        return fileName