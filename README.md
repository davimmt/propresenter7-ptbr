### Sobre a Bíblia na versão Português do Brasil para o ProPresenter 7

Se você quiser a Bíblia em português para usar no ProPresenter 7 (não sei sobre a compatibilidade em outras versões) e não souber usar o programa que eu fiz, mande um email para mirandadavi.mt@gmail.com que eu te envio os arquivos da Bíblia compactados. Mais informações abaixo.

As versões de tradução podem ser:
* Almeida Corrigida Fiel (ACF)
* Nova Versão Internacional (NVI)
* Almeida Revista e Atualizada (ARA)
* Almeida Revista e Corrigida (ARC)
* Nova Almeida Atualizada (NAA)
  * Para gerar a Bíblia, eu uso o site https://www.bibliaonline.com.br/, qualquer tradução de lá é passível de ser usada, mas essas 4 são a mainstream.
  
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
    * Caso você tenha gerado por si mesmo usando meu programa, é só copiar e substituir os arquivos gerados para a pasta USX.

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
        <abbr>Gen</abbr>
    </book>
    ...
</bookNames>
```

  * O *book code* é o nome do arquivo .usx que ele vai procurar na pasta USX.
  * O *short* é o nome que aparece para selecionar no menu Bible do ProPresenter e na referência do slide.
  * O *long* e o *abbr* eu não faço ideia.
  * Basta substituir a tag \<bookNames> com isso:
```
<bookNames>
    <book code="GEN">
        <short>Gênesis</short>
    </book>
    <book code="EXO">
        <short>Êxodo</short>
    </book>
    <book code="LEV">
        <short>Levítico</short>
    </book>
    <book code="NUM">
        <short>Números</short>
    </book>
    <book code="DEU">
        <short>Deuteronômio</short>
    </book>
    <book code="JOS">
        <short>Josué</short>
    </book>
    <book code="JDG">
        <short>Juízes</short>
    </book>
    <book code="RUT">
        <short>Rute</short>
    </book>
    <book code="1SA">
        <short>1 Samuel</short>
    </book>
    <book code="2SA">
        <short>2 Samuel</short>
    </book>
    <book code="1KI">
        <short>1 Reis</short>
    </book>
    <book code="2KI">
        <short>2 Reis</short>
    </book>
    <book code="1CH">
        <short>1 Crônicas</short>
    </book>
    <book code="2CH">
        <short>2 Crônicas</short>
    </book>
    <book code="EZR">
        <short>Esdras</short>
    </book>
    <book code="NEH">
        <short>Neemias</short>
    </book>
    <book code="EST">
        <short>Ester</short>
    </book>
    <book code="JOB">
        <short>Jó</short>
    </book>
    <book code="PSA">
        <short>Salmos</short>
    </book>
    <book code="PRO">
        <short>Provérbios</short>
    </book>
    <book code="ECC">
        <short>Eclesiastes</short>
    </book>
    <book code="SNG">
        <short>Cântico dos Cânticos</short>
    </book>
    <book code="ISA">
        <short>Isaías</short>
    </book>
    <book code="JER">
        <short>Jeremias</short>
    </book>
    <book code="LAM">
        <short>Lamentações</short>
    </book>
    <book code="EZK">
        <short>Ezequiel</short>
    </book>
    <book code="DAN">
        <short>Daniel</short>
    </book>
    <book code="HOS">
        <short>Oséias</short>
    </book>
    <book code="JOL">
        <short>Joel</short>
    </book>
    <book code="AMO">
        <short>Amós</short>
    </book>
    <book code="OBA">
        <short>Abdias</short>
    </book>
    <book code="JON">
        <short>Jonas</short>
    </book>
    <book code="MIC">
        <short>Miquéias</short>
    </book>
    <book code="NAM">
        <short>Naum</short>
    </book>
    <book code="HAB">
        <short>Habacuc</short>
    </book>
    <book code="ZEP">
        <short>Sofonias</short>
    </book>
    <book code="HAG">
        <short>Ageu</short>
    </book>
    <book code="ZEC">
        <short>Zacarias</short>
    </book>
    <book code="MAL">
        <short>Malaquias</short>
    </book>
    <book code="MAT">
        <short>Mateus</short>
    </book>
    <book code="MRK">
        <short>Marcos</short>
    </book>
    <book code="LUK">
        <short>Lucas</short>
    </book>
    <book code="JHN">
        <short>João</short>
    </book>
    <book code="ACT">
        <short>Atos</short>
    </book>
    <book code="ROM">
        <short>Romanos</short>
    </book>
    <book code="1CO">
        <short>1 Coríntios</short>
    </book>
    <book code="2CO">
        <short>2 Coríntios</short>
    </book>
    <book code="GAL">
        <short>Gálatas</short>
    </book>
    <book code="EPH">
        <short>Efésios</short>
    </book>
    <book code="PHP">
        <short>Filipenses</short>
    </book>
    <book code="COL">
        <short>Colossenses</short>
    </book>
    <book code="1TH">
        <short>1 Tessalonicenses</short>
    </book>
    <book code="2TH">
        <short>2 Tessalonicenses</short>
    </book>
    <book code="1TI">
        <short>1 Timóteo</short>
    </book>
    <book code="2TI">
        <short>2 Timóteo</short>
    </book>
    <book code="TIT">
        <short>Tito</short>
    </book>
    <book code="PHM">
        <short>Filemon</short>
    </book>
    <book code="HEB">
        <short>Hebreus</short>
    </book>
    <book code="JAS">
        <short>Tiago</short>
    </book>
    <book code="1PE">
        <short>1 Pedro</short>
    </book>
    <book code="2PE">
        <short>2 Pedro</short>
    </book>
    <book code="1JN">
        <short>1 João</short>
    </book>
    <book code="2JN">
        <short>2 João</short>
    </book>
    <book code="3JN">
        <short>3 João</short>
    </book>
    <book code="JUD">
        <short>Judas</short>
    </book>
    <book code="REV">
        <short>Apocalipse</short>
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

* File "C:\Users\Davi Miranda\AppData\Local\Programs\Python\Python38-32\lib\urllib\request.py", line 1322, in do_open raise URLError(err) urllib.error.URLError: \<urlopen error [WinError 10054] Foi forçado o cancelamento de uma conexão existente pelo host remoto>
  * É erro de conexão, reinicie o programa que deve funcionar, é problema da biblioteca requets urllib.

*  File "c:\Users\Davi Miranda\Downloads\multimidia_igreja\USX Bible\main\Book.py", line 31, in getInfo unwantedTag.extract() AttributeError: 'NoneType' object has no attribute 'extract'
    * Para gerar a Bíblia, eu uso o site https://www.bibliaonline.com.br/, mas a estrutura da página muda por cada versão, então as traduções riscadas estão *indisponíveis* no momento.
    * A estrutura que muda é o copyright no final dos versos, que misturava e dava erro ao extrair algo que não existia (linha 30-31 do arquivo *Book*), apenas fiz uma condição (linhas 21-27 do arquivo *Book*) para ver se ele existe e a compatibilidade aumentou.
