import sys
from Data import Bible
from PowerPoint import PowerPoint

bible = Bible().getCompleteNAA() if str(sys.argv[1].lower()) == 'naa' else Bible().getCompleteACF()
_input = str(sys.argv[2].lower())

def chapter(_input):
    """Printar todo o capítulo.
       Print whole chapter.
    """
    for book in bible:
        name, sep, abbr = book.partition("/")
        input_name, sep, input_chapter = _input.partition("/")

        if (name.lower() == input_name or abbr.lower().replace(" ", "") == input_name):
            for chapter in bible[book]:
                if (chapter == input_chapter):
                    reference = [name + " " + chapter]
                    for verse in bible[book][chapter]:
                        reference.append(verse + " " + bible[book][chapter][verse])

    return reference

def verses(_input):
    """Printar a referência de versículos.
       Print the versicle's reference.
    """
    for book in bible:
        name, sep, abbr = book.partition("/")
        input_name, sep, input_info = _input.partition("/")
        input_chapter, sep, input_verses = input_info.partition(":")
        beggining, sep, end = input_verses.partition("-")

        if (name.lower() == input_name or abbr.lower().replace(" ", "") == input_name):
            for chapter in bible[book]:
                if (chapter == input_chapter):
                    reference = ["{} {}:{}-{}\n". format(name, chapter, beggining, end)]
                    for verse in bible[book][chapter]:
                        if (int(verse) >= int(beggining) and int(verse) <= int(end)):
                            reference.append(verse + " " + bible[book][chapter][verse])
                            
    return reference

def verse(_input):
    """Printar o versículo específico.
       Print the specific versicle.
    """
    for book in bible:
        name, sep, abbr = book.partition("/")
        input_name, sep, input_info = _input.partition("/")
        input_chapter, sep, input_verse = input_info.partition(":")

        if (name.lower() == input_name or abbr.lower().replace(" ", "") == input_name):
            for chapter in bible[book]:
                if (chapter == input_chapter):
                    reference = ['']
                    for verse in bible[book][chapter]:
                        if (verse == input_verse):
                            reference.append('"{}" \n\n— {} {}:{}'.format(bible[book][chapter][verse], name, chapter, verse))

    return reference

if '/' in _input and ':' in _input and '-' in _input: # Caso (3)
    reference = verses(_input)
elif '/' in _input and ':' in _input: # Caso (2)
    reference = verse(_input)
elif '/' in _input: # Caso (1)
    reference = chapter(_input)

try:
    filePptx = PowerPoint().generatePptx(reference)
    print("\nArquivo atualizado com sucesso!\n")
except:
    print('\nError ao atualizar arquivo.')