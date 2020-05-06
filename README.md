### Sobre a Bíblia na versão Português do Brasil para o ProPresenter 7

Se você quiser a Bíblia em português para usar no ProPresenter 7 (não sei sobre a compatibilidade em outras versões), mande um email para mirandadavi.mt@gmail.com que eu te envio os arquivos da Bíblia compactados. Mais informações abaixo.

As versões de tradução podem ser:
* Almeida Corrigida Fiel (ACF)
* Nova Versão Internacional (NVI)
* ~Almeida Revista e Atualizada (ARA)~
* ~Almeida Revista e Corrigida (ARC)~
* ~Nova Almeida Atualizada (NAA)~
  * Para gerar a Bíblia, eu uso o site https://www.bibliaonline.com.br/, mas a estrutura da página muda por cada versão, então as traduções riscadas estão *indisponíveis* no momento.
  
---

### Sumário

* Dependências
* Sobre *Song Lyrics, o Gerador de Hinos*
  * ~Como funciona (não feito ainda)~
  * ~Histórico de problemas (não feito ainda)~
* Sobre *USX Bible, o Gerador de Bíblias*
  * Passo a passo de como instalar a Bíblia (na tradução português do Brasil)
  * Como funciona (incompleto)
  * O que fazer depois da instalação (opcional)
  * Histórico de problemas

---

### Dependências

- [Python 3.8.2](https://www.python.org/downloads/release/python-382/)
- [pip3](https://pip.pypa.io/en/stable/)
  - [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  - [unidecode](https://pypi.org/project/Unidecode/)
  - [requests](https://requests.readthedocs.io/en/latest/)
  - [urllib 3](https://docs.python.org/3/library/urllib.html)
  - [re](https://docs.python.org/3/library/re.html)
  - [python-docx](https://python-docx.readthedocs.io/en/latest/) (somente para *Song Lyrics*)
  - [python-pptx](https://python-pptx.readthedocs.io/en/latest/) (somente para *Song Lyrics*)

---

### Sobre Song Lyrics
#### O Gerador de Hinos.

Song Lyrics é um programa responsável por ~facilitar a vida de quem faz muito slide de música pra Igreja~ gerar arquivos com a letra do hino (ou qualquer música do site indicado) de sua escolha, basta você informar sua URL.

**A URL tem que ser do site letras.mus.br.**

Ele gera 2 arquivos:
  - .pptx => Apresentação de Slides em PowerPoint
  - .txt => Arquivo de importação para o ProPresenter 7

---

### Sobre USX Bible
#### O Gerador de Bíblias.

USX Bible é responsável por gerar uma Bíblia em Portugês para o ProPresenter 7 (o processo gira em torno de 20min.), já que não há uma de graça nesse idioma (e eu não tava afim de usar dois aplicativos de apresentação só por causa disso).

**Como eu já gerei, apenas me envie um e-mail (mirandadavi.mt@gmail.com) e eu contentemente enviá-lo-ei a Bíblia compactada.**

#### Passo a passo de como instalar a Bíblia:

1. Abra o ProPresenter e vá na aba de *Bible*, depois em *Options*, *Bible* novamente, *Free*, e, então, *Install* (de preferência na King James Version, pode ser qualquer uma que tenha o formato USX):

![](USX%20Bible/img/usxbible_00.png)

2. Uma vez instalada, você pode perceber que está, obviamente, tudo em inglês:

![](USX%20Bible/img/usxbible_01.png)

3. Feche o ProPresenter, e vá na pasta oculta do ProPresenter. No meu caso, está no disco C:.
  * C:\ProgramData\RenewedVision\ProPresenter\Bibles
  * Numa instalação limpa, a pasta Bibles está vazia, execto pelo arquivo *BibleData.proPref* com o conteúdo *InstalledBibles=[];*
  * Agora, perceba que há uma pasta com um nome estranho (provavelmente uma chave de validação) e o arquivo *BibleData.proPref* com o conteúdo *InstalledBibles=[nome_da_pasta|abreviação_da_tradução|nome_da_tradução|não_sei];*
  
![](USX%20Bible/img/usxbible_02.png)

4. Agora basta extrair o arquivo compactado que eu vos enviei/enviarei, ou os que você mesmo gerou, dentro da pasta gerada e substituir tudo no processo.
    * **Apenas envio a pasta USX com um arquivo de texto, extraia e substitua apenas a pasta e leia o arquivo para mais intruções!**

![](USX%20Bible/img/usxbible_03.png)

5. Abra o ProPresenter novamente e perceba que funcionou!

![](USX%20Bible/img/usxbible_04.png)

#### O que fazer depois da instalação (opcional)

**Esse tópico foi criado porque há um bug caso você queira usar 2 traduções em português diferente e, consequentemente, ter que baixar duas Bíblias grátis em outra língua diferente. Não se pode usar o mesmo *rvmetadata* ou causará um bug visual de entrada dupla na seleção.**

**Não encontrei problemas em usar o mesmo *metadata* (ele serve pra tradução do nome dos livros na seleção), mas por questão de organização e boa prática, não estarei botando ele nos arquivos que estarei enviando a partir de agora. Abaixo ensino como traduzir esses nomes.**

* Para mudar o título que você seleciona no menu Bible do ProPresenter, vá no arquivo rvmetadata.xml e altere aqui: 
```
<name>King James Version</name>
```

* Para mudar a abreviação que aparece no slide (com a opção Display Translation ativada), vá no arquivo rvmetadata.xml e altere aqui:
  * Se essa linha não existir, apenas adicione ela após a linha do \<name>\</name> (mencionada no item acima).
```
<displayAbbreviation>KJV</displayAbbreviation>
```

* No arquivo *metadata.xml* temos os nomes dos livros:
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
  * Basta substituir a tag \<bookNames> com isso:
```
<bookNames>
    <book code="GEN">
        <long>Gênesis</long>
        <short>Gênesis</short>
        <abbr>Gênesis</abbr>
    </book>
    <book code="EXO">
        <long>Êxodo</long>
        <short>Êxodo</short>
        <abbr>Êxodo</abbr>
    </book>
    <book code="LEV">
        <long>Levítico</long>
        <short>Levítico</short>
        <abbr>Levítico</abbr>
    </book>
    <book code="NUM">
        <long>Números</long>
        <short>Números</short>
        <abbr>Números</abbr>
    </book>
    <book code="DEU">
        <long>Deuteronômio</long>
        <short>Deuteronômio</short>
        <abbr>Deuteronômio</abbr>
    </book>
    <book code="JOS">
        <long>Josué</long>
        <short>Josué</short>
        <abbr>Josué</abbr>
    </book>
    <book code="JDG">
        <long>Juízes</long>
        <short>Juízes</short>
        <abbr>Juízes</abbr>
    </book>
    <book code="RUT">
        <long>Rute</long>
        <short>Rute</short>
        <abbr>Rute</abbr>
    </book>
    <book code="1SA">
        <long>1 Samuel</long>
        <short>1 Samuel</short>
        <abbr>1 Samuel</abbr>
    </book>
    <book code="2SA">
        <long>2 Samuel</long>
        <short>2 Samuel</short>
        <abbr>2 Samuel</abbr>
    </book>
    <book code="1KI">
        <long>1 Reis</long>
        <short>1 Reis</short>
        <abbr>1 Reis</abbr>
    </book>
    <book code="2KI">
        <long>2 Reis</long>
        <short>2 Reis</short>
        <abbr>2 Reis</abbr>
    </book>
    <book code="1CH">
        <long>1 Crônicas</long>
        <short>1 Crônicas</short>
        <abbr>1 Crônicas</abbr>
    </book>
    <book code="2CH">
        <long>2 Crônicas</long>
        <short>2 Crônicas</short>
        <abbr>2 Crônicas</abbr>
    </book>
    <book code="EZR">
        <long>Esdras</long>
        <short>Esdras</short>
        <abbr>Esdras</abbr>
    </book>
    <book code="NEH">
        <long>Neemias</long>
        <short>Neemias</short>
        <abbr>Neemias</abbr>
    </book>
    <book code="EST">
        <long>Ester</long>
        <short>Ester</short>
        <abbr>Ester</abbr>
    </book>
    <book code="JOB">
        <long>Jó</long>
        <short>Jó</short>
        <abbr>Jó</abbr>
    </book>
    <book code="PSA">
        <long>Salmos</long>
        <short>Salmos</short>
        <abbr>Salmos</abbr>
    </book>
    <book code="PRO">
        <long>Provérbios</long>
        <short>Provérbios</short>
        <abbr>Provérbios</abbr>
    </book>
    <book code="ECC">
        <long>Eclesiastes</long>
        <short>Eclesiastes</short>
        <abbr>Eclesiastes</abbr>
    </book>
    <book code="SNG">
        <long>Cântico dos Cânticos</long>
        <short>Cântico dos Cânticos</short>
        <abbr>Cântico dos Cânticos</abbr>
    </book>
    <book code="ISA">
        <long>Isaías</long>
        <short>Isaías</short>
        <abbr>Isaías</abbr>
    </book>
    <book code="JER">
        <long>Jeremias</long>
        <short>Jeremias</short>
        <abbr>Jeremias</abbr>
    </book>
    <book code="LAM">
        <long>Lamentações</long>
        <short>Lamentações</short>
        <abbr>Lamentações</abbr>
    </book>
    <book code="EZK">
        <long>Ezequiel</long>
        <short>Ezequiel</short>
        <abbr>Ezequiel</abbr>
    </book>
    <book code="DAN">
        <long>Daniel</long>
        <short>Daniel</short>
        <abbr>Daniel</abbr>
    </book>
    <book code="HOS">
        <long>Oséias</long>
        <short>Oséias</short>
        <abbr>Oséias</abbr>
    </book>
    <book code="JOL">
        <long>Joel</long>
        <short>Joel</short>
        <abbr>Joel</abbr>
    </book>
    <book code="AMO">
        <long>Amós</long>
        <short>Amós</short>
        <abbr>Amós</abbr>
    </book>
    <book code="OBA">
        <long>Abdias</long>
        <short>Abdias</short>
        <abbr>Abdias</abbr>
    </book>
    <book code="JON">
        <long>Jonas</long>
        <short>Jonas</short>
        <abbr>Jonas</abbr>
    </book>
    <book code="MIC">
        <long>Miquéias</long>
        <short>Miquéias</short>
        <abbr>Miquéias</abbr>
    </book>
    <book code="NAM">
        <long>Naum</long>
        <short>Naum</short>
        <abbr>Naum</abbr>
    </book>
    <book code="HAB">
        <long>Habacuc</long>
        <short>Habacuc</short>
        <abbr>Habacuc</abbr>
    </book>
    <book code="ZEP">
        <long>Sofonias</long>
        <short>Sofonias</short>
        <abbr>Sofonias</abbr>
    </book>
    <book code="HAG">
        <long>Ageu</long>
        <short>Ageu</short>
        <abbr>Ageu</abbr>
    </book>
    <book code="ZEC">
        <long>Zacarias</long>
        <short>Zacarias</short>
        <abbr>Zacarias</abbr>
    </book>
    <book code="MAL">
        <long>Malaquias</long>
        <short>Malaquias</short>
        <abbr>Malaquias</abbr>
    </book>
    <book code="MAT">
        <long>Mateus</long>
        <short>Mateus</short>
        <abbr>Mateus</abbr>
    </book>
    <book code="MRK">
        <long>Marcos</long>
        <short>Marcos</short>
        <abbr>Marcos</abbr>
    </book>
    <book code="LUK">
        <long>Lucas</long>
        <short>Lucas</short>
        <abbr>Lucas</abbr>
    </book>
    <book code="JHN">
        <long>João</long>
        <short>João</short>
        <abbr>João</abbr>
    </book>
    <book code="ACT">
        <long>Atos</long>
        <short>Atos</short>
        <abbr>Atos</abbr>
    </book>
    <book code="ROM">
        <long>Romanos</long>
        <short>Romanos</short>
        <abbr>Romanos</abbr>
    </book>
    <book code="1CO">
        <long>1 Coríntios</long>
        <short>1 Coríntios</short>
        <abbr>1 Coríntios</abbr>
    </book>
    <book code="2CO">
        <long>2 Coríntios</long>
        <short>2 Coríntios</short>
        <abbr>2 Coríntios</abbr>
    </book>
    <book code="GAL">
        <long>Gálatas</long>
        <short>Gálatas</short>
        <abbr>Gálatas</abbr>
    </book>
    <book code="EPH">
        <long>Efésios</long>
        <short>Efésios</short>
        <abbr>Efésios</abbr>
    </book>
    <book code="PHP">
        <long>Filipenses</long>
        <short>Filipenses</short>
        <abbr>Filipenses</abbr>
    </book>
    <book code="COL">
        <long>Colossenses</long>
        <short>Colossenses</short>
        <abbr>Colossenses</abbr>
    </book>
    <book code="1TH">
        <long>1 Tessalonicenses</long>
        <short>1 Tessalonicenses</short>
        <abbr>1 Tessalonicenses</abbr>
    </book>
    <book code="2TH">
        <long>2 Tessalonicenses</long>
        <short>2 Tessalonicenses</short>
        <abbr>2 Tessalonicenses</abbr>
    </book>
    <book code="1TI">
        <long>1 Timóteo</long>
        <short>1 Timóteo</short>
        <abbr>1 Timóteo</abbr>
    </book>
    <book code="2TI">
        <long>2 Timóteo</long>
        <short>2 Timóteo</short>
        <abbr>2 Timóteo</abbr>
    </book>
    <book code="TIT">
        <long>Tito</long>
        <short>Tito</short>
        <abbr>Tito</abbr>
    </book>
    <book code="PHM">
        <long>Filemon</long>
        <short>Filemon</short>
        <abbr>Filemon</abbr>
    </book>
    <book code="HEB">
        <long>Hebreus</long>
        <short>Hebreus</short>
        <abbr>Hebreus</abbr>
    </book>
    <book code="JAS">
        <long>Tiago</long>
        <short>Tiago</short>
        <abbr>Tiago</abbr>
    </book>
    <book code="1PE">
        <long>1 Pedro</long>
        <short>1 Pedro</short>
        <abbr>1 Pedro</abbr>
    </book>
    <book code="2PE">
        <long>2 Pedro</long>
        <short>2 Pedro</short>
        <abbr>2 Pedro</abbr>
    </book>
    <book code="1JN">
        <long>1 João</long>
        <short>1 João</short>
        <abbr>1 João</abbr>
    </book>
    <book code="2JN">
        <long>2 João</long>
        <short>2 João</short>
        <abbr>2 João</abbr>
    </book>
    <book code="3JN">
        <long>3 João</long>
        <short>3 João</short>
        <abbr>3 João</abbr>
    </book>
    <book code="JUD">
        <long>Judas</long>
        <short>Judas</short>
        <abbr>Judas</abbr>
    </book>
    <book code="REV">
        <long>Apocalipse</long>
        <short>Apocalipse</short>
        <abbr>Apocalipse</abbr>
    </book>
</bookNames>
```

#### Como funciona

* Cada livro da Bíblia tem um arquivo na pasta USX, são eles que estaremos traduzindo (extraindo do site mencionado, na verdade). Esse é o formato:
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
  
* File "C:\Users\Davi Miranda\AppData\Local\Programs\Python\Python38-32\lib\http\client.py", line 1183, in _validate_ path raise InvalidURL(f"URL can't contain control characters. {url!r} " http.client.InvalidURL: URL can't contain control characters. '/acf/1 samuel/1' (found at least ' ')
  * Resolvido ao retornar com *.replace(' ', '')* na linha 218 do arquivo Bible.

* File "C:\Users\Davi Miranda\AppData\Local\Programs\Python\Python38-32\lib\urllib\request.py", line 649, in http_error_default raise HTTPError(req.full_url, code, msg, hdrs, fp) urllib.error.HTTPError: HTTP Error 404: Not Found
  * O site entende o retorno de Jó do array como jo (João). Mudei de Jó para Jób.
  * O site entende o retorno de Daniel do array como danth (bug, provavelmente). Mudei de Daniel para Dn.
  * Filemon não existe para o site, mudei para Filemom.

* File "C:\Users\Davi Miranda\AppData\Local\Programs\Python\Python38-32\lib\urllib\request.py", line 1322, in do_open raise URLError(err) urllib.error.URLError: <urlopen error [WinError 10054] Foi forçado o cancelamento de uma conexão existente pelo host remoto>
  * É erro de conexão, reinicie o programa que deve funcionar, é problema da biblioteca requets urllib.
