from Bible import Bible
from Book import Book

def inputChoices(i):
    versionChoice = "\n[1] Almeida Corrigida e Fiel (ACF)\n[2] Nova Versão Internacional (NVI)\n[3] Almeida Revista e Atualizada (ARA)\n[4] Nova Almeida Atualizada (NAA)\n[5] Outra\n\nEscolha a versão (padrão = 1): "
    rangeChoice = "\n[1] Toda Bíblia\n[2] Velho Testamento\n[3] Novo Testamento\n[4] Pentateuco\n[5] Profetas Maiores\n[6] Evangelhos\n[7] Epístolas de Paulo\n[8] Salmos e Provérbios\n[9] Outro\n\nVocê quer gerar (padrão = 1): "

    if i == 0: return versionChoice
    if i == 1: return rangeChoice

def inputMain():
    try:
        inputVersion = int(input(inputChoices(0)))
        if inputVersion == 1: returnVersion = "acf"
        if inputVersion == 2: returnVersion = "nvi"
        if inputVersion == 3: returnVersion = "ara"
        if inputVersion == 4: returnVersion = "naa"
        if inputVersion == 5: returnVersion = input("Digite: ")
    except:
       returnVersion = "acf"
    
    try:
        inputRange = int(input(inputChoices(1)))
        if inputRange == 1: returnRange = 0, 66
        if inputRange == 2: returnRange = 0, 39
        if inputRange == 3: returnRange = 39, 66
        if inputRange == 4: returnRange = 0, 5
        if inputRange == 5: returnRange = 22, 27
        if inputRange == 6: returnRange = 39, 43
        if inputRange == 7: returnRange = 44, 57
        if inputRange == 8: returnRange = 18, 20
        if inputRange == 9: returnRange = input("Digite: ").split(",")
    except:
        returnRange = 0, 66

    return main(returnRange, returnVersion)

def main(forRange, version):
    for i in range(int(forRange[0]), int(forRange[1])):
        numChapters = int(Bible().getbooksChapterNumber(i))
        bookName = Bible().getBooksName(i)
        bookAbbreviation = Bible().getBooksAbbreviation(i)
        bookNamePtBR = Bible().getBooksPtBRName(i)

        print("\nGerando: " + bookAbbreviation)
        for j in range(1, numChapters + 1):
            chapter = str(j)
            url = "https://www.bibliaonline.com.br/" + version + "/" + bookAbbreviation  + "/" + chapter
            fileName = Book().getInfo(url, bookName, bookAbbreviation)

        with open(bookAbbreviation + '.usx', 'a+', encoding='utf-8') as file:
            file.write('</usx>')
        
        print(fileName + " gerada com sucesso.")

inputMain()
