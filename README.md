### Sobre a Bíblia na versão Português do Brasil para o ProPresenter 7

Se você quiser a Bíblia em português para usar no ProPresenter 7 (não sei sobre a compatibilidade em outras versões), mande um email para mirandadavi.mt@gmail.com que eu te envio os arquivos da Bíblia compactados. Mais informações abaixo.

As versões de tradução podem ser:
* Almeida Corrigida Fiel (ACF)
* Almeida Revista e Atualizada (ARA)
* Almeida Revista e Corrigida (ARC)
* Nova Versão Internacional (NVI)
  * Ou qualquer uma suportada pelo site https://www.bibliaonline.com.br/
  
---

### Sumário

* Dependências
* Sobre *Song Lyrics, o Gerador de Hinos*
  * ~Como funciona (não feito ainda)~
* Sobre *USX Bible, o Gerador de Bíblias*
  * Passo a passo de como instalar a Bíblia (na tradução português do Brasil)
  * Como funciona
  * Histórico de problemas

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

1. Abra o ProPresenter e vá na aba de *Bible*, depois em *Options*, *Bible* novamente, *Free*, e, então, *Install* (de preferência na King James Version, não testei nas demais):

![](USX%20Bible/img/usxbible_00.png)

2. Uma vez instalada, você pode perceber que está, obviamente, tudo em inglês:

![](USX%20Bible/img/usxbible_01.png)

3. Feche o ProPresenter, e vá na pasta oculta do ProPresenter. No meu caso, está no disco C:.
  * C:\ProgramData\RenewedVision\ProPresenter\Bibles
  * Numa instalação limpa, a pasta Bibles está vazia, execto pelo arquivo *BibleData.proPref* com o conteúdo *InstalledBibles=[];*
  * Agora, perceba que há uma pasta com um nome estranho (provavelmente uma chave de validação) e o arquivo *BibleData.proPref* com o conteúdo *InstalledBibles=[nome_da_pasta|abreviação_da_tradução|nome_da_tradução|não_sei];*
  
![](USX%20Bible/img/usxbible_02.png)

4. Agora basta extrair o arquivo compactado que eu vos enviei/enviarei dentro da pasta gerada e substituir tudo no processo.

![](USX%20Bible/img/usxbible_03.png)

5. Abra o ProPresenter novamente e perceba que funcionou!

![](USX%20Bible/img/usxbible_04.png)

#### Como funciona

* Para mudar o título que você seleciona no menu Bible do ProPresenter, vá no arquivo rvmetadata.xml e altere aqui: 
```
<name>King James Version</name>
```
  * Não recomendo mudar o *\<abbreviation>KJV\</abbreviation>*, pois causa entrada dupla na seleção de versão, aparentemente. Não é ele que muda o texto da Display Translation, nem procurei achar qual muda.

* No arquivo metadata.xml temos os nomes dos livros:
```  
<bookNames>
    <book code="GEN">
        <long>Genesis</long>
        <short>Genesis</short>
        <abbr>Genesis</abbr>
    </book>
    ...
</bookNames>
```

  * O *book code* é o nome do arquivo .usx que ele vai procurar na pasta USX.
  * O *long*, *short* e *abbr* são o nome que aparece para selecionar no menu Bible do ProPresenter e na referência do slide.

* Cada livro da Bíblia tem um arquivo na pasta USX, são eles que estaremos traduzindo. Esse é o formato:
```
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
     ...
</usx>
```

* O arquivo *generateUSXBookFile* é feito para gerar o arquivo de um livro por vez e só depende dele mesmo. O arquivo *generateUSXBible* gera toda a Bíblia de uma vez (20min. de operação, em média, no total) e depende do arquivo *Bible*.
 
#### Histórico de problemas:
##### Não-resolvidos
* Nenhum, amém!

##### Resolvidos
* System.Exception: Error while trying to retrieve the Books for this Bible. ---> System.Xml.XmlException: Um nome não pode ser iniciado pelo caractere ',', valor hexadecimal 0x2C. Linha 8, posição 39.
  * Ou seja, versículos começando com ',' (vírgula) faziam o ProPresenter crashar. 
    * Resolvido na formatação, ao escrever no arquivo gerado.

* Livros enumerados como 1CO/2CO ou 1TI/2TI têm seus versos de acordo com sua numeração, no qual o primeiro dígito da esquerda corresponde a numeração do livro e os demais da direita ao versículo, isto é, 1CO:11, 12, 13; 2CO:21, 22, 23.
  * Resolvido na linha 10, para pegar o número do capítulo eu extraio todos os números da URL, mas isso significa extrair também os números do livro, caso tenham (1-reis, 1-corintios), então, ao pegar o capitulo da url, usar o sufixo [-3:] na string, para considerar apenas os 3 últimos caracteres.
  
 * Exemplo: [Isaías 51:6](https://biblia.blog.br/acf/livro/isaias/51/6) está com o versículo incompleto (e vários outros). É problema com o site, não com o programa em si. Aparentemente o site não percebeu que os versículos longos estão com um limite de caracteres.
  * Resolvido trocando para o site https://www.bibliaonline.com.br/.
