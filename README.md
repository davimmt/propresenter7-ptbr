### Sobre a Bíblia na versão Português do Brasil (ACF) para o ProPresenter 7

Se você quiser a Bíblia em português (ACF) para usar no ProPresenter 7 (não sei sobre a compatibilidade em outras versões), mande um email para mirandadavi.mt@gmail.com que eu te envio os arquivos da Bíblia compactados. Mais informações abaixo.

---

### Dependências

- [Python 3.8.2](https://www.python.org/downloads/release/python-382/)
- [pip3](https://pip.pypa.io/en/stable/)
  - [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  - [unidecode](https://pypi.org/project/Unidecode/)
  - [requests](https://requests.readthedocs.io/en/latest/)
  - [urllib 3](https://docs.python.org/3/library/urllib.html)
  - [python-docx](https://python-docx.readthedocs.io/en/latest/)
  - [python-pptx](https://python-pptx.readthedocs.io/en/latest/)

---

### Sobre Song Lyrics
#### O Gerador de Hinos.

Song Lyrics é um programa responsável por ~facilitar a vida de quem faz muito slide de música pra Igreja~ gerar arquivos com a letra do hino (ou qualquer música do site indicado) de sua escolha, basta você informar sua URL.

**A URL tem que ser do site letras.mus.br.**

Ele gera 3 arquivos:
  - .pptx => Apresentação de Slides em PowerPoint
  - .docx => Arquivo de importação para o ProPresenter 7
  - .txt => Arquivo de importação para o ProPresenter 6

---

### Sobre USX Bible
#### O Gerador de Bíblias.

USX Bible é responsável por gerar uma Bíblia em Portugês para o ProPresenter 7, já que não há uma de graça nesse idioma (e eu não tava afim de usar dois aplicativos de apresentação só por causa disso).

**Como eu já gerei, apenas me envie um e-mail (mirandadavi.mt@gmail.com) e eu contentemente enviá-lo-ei a Bíblia compactada.**

#### Passo a passo de como instalar a Bíblia:

  1.1 No ProPresenter 7, baixar qualquer Bíblia grátis (KJV, no meu caso) para gerar o token de validação do próprio progama (o nome da pasta em C:\ProgramData\RenewedVision\ProPresenter\Bibles e a entrada no BiblieData.proPref). Não consegui criar um.

  1.2 Para mudar o título que você seleciona no menu Bible do ProPresenter, vá no arquivo rvmetadata.xml e altere aqui: 
  
      <name>King James Version</name>

      1.2.1 Não recomendo mudar o <abbreviation>KJV</abbreviation>, pois é causa entrada dupla na seleção de versão, aparentemente. Não é ele que muda o Display Translation, nem procurei achar qual muda.

  1.3. No arquivo metadata.xml temos os nomes dos livros:
  
      <bookNames>
          <book code="GEN">
              <long>Genesis</long>
              <short>Genesis</short>
              <abbr>Genesis</abbr>
          </book>
          ...
      </bookNames>

      1.3.1 O book code é o nome do arquivo .usx que ele vai procurar na pasta USX.

      1.3.2 O long, short e abbr são o nome que aparece para selecionar no menu Bible do ProPresenter e que aparece no slide.

  1.4. Cada livro da Bíblia tem um arquivo na pasta USX, são eles que estaremos traduzindo. Esse é o formato:
  
      <?xml version="1.0" encoding="utf-8"?>
      <usx version="2.0">
          <book code="TIT" style="id">Titus</book>
          <para style="mt">Titus</para>

          <chapter number="1" style="c" />
              <para style="p">
                  <verse number="1" style="v" />...</para>
              <para style="p">
                  <verse number="2" style="v" />...</para>
                  ...
          <chapter number="2" style="c" />
              <para style="p">
                  <verse number="1" style="v" />...</para>
                  ...
      </usx>

  1.5 O arquivo generateUSXBookFile é feito para gerar o arquivo de um livro por vez e só depende dele mesmo. O arquivo generateUSXBible gera toda a Bíblia de uma vez (20min. de operação, em média, no total) e depende do arquivo Bible.
 
 ---
 
Histórico de bugs:

- Versículos começando com ',' (vírgula) faziam o ProPresenter crashar. 
  - (resolvido na formatação)

- Livros enumerados como 1CO/2CO ou 1TI/2TI têm seus versos de acordo com sua numeração, no qual o primeiro dígito da esquerda corresponde a numeração do livro e os demais da direita ao versículo, isto é:
  - 1CO: 11, 12, 13
  - 2CO: 21, 22, 23
  - (resolvido na linha 10, pegar o capitulo da url[-3:])
  
  
