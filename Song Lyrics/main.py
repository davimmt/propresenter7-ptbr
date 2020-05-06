from Lyrics import Lyrics
from PowerPoint import PowerPoint
from ProPresenter import ProPresenter

def main():
    try:
        music = Lyrics().getLyrics(input("\nURL da música (letras.mus.br): "))
    except:
        print('\nURL inválida.')
        if (int(input("\nDigite '1' para continuar: ")) == 1):
            main()

    try:
        fileTxt = ProPresenter().generateTxt(music[0], music[1], music[2])
        print("\n'" + fileTxt + "' gerado com sucesso!")
    except:
        print('\nError ao gerar txt.')

    try:
        filePptx = PowerPoint().generatePptx(music[0], music[1], music[2])
        print("\n'" + filePptx + "' gerado com sucesso!")
    except:
        print('\nError ao gerar pptx.')

    if (int(input("\nDigite '1' para continuar: ")) == 1):
        main()

main()


