Se você quiser a Bíblia em português (ACF) para usar no ProPresenter 7 (não sei sobre a compatibilidade em outras versões), mande um email para mirandadavi.mt@gmail.com que eu te envio o .zip. Extraia dentro da pasta da Bíblia grátis gerada pelo aplicativo, substituindo tudo.

- Para usar os códigos, você precisa:

  - Python 3.8.2+

- Dentro do Python, você precisa usar o pip3 install para ter os seguintes pacotes:
  - BeautifulSoup
  - unidecode
  - requests
  - python-docx
  - python-pptx

---

- Song Lyrics gera .pptx e .docx + .txt (ambos para importar pro ProPresenter).
  - .docx => ProPresenter 7
  - .txt => ProPresenter 6

1. Generate USX Bible é para gerar uma Bíblia em Portugês para o ProPresenter 7, já que não há uma de graça.

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
  
  
