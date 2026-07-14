# Guia de Edicao / Producao

Como usar uma inspiracao do acervo para criar um design novo.

## 1. Escolha a inspiracao
Abra a galeria (`./bin/galeria`) e clique em "editavel" no cartao desejado.
O editavel.html abre com o CSS carregando (fica na mesma pasta do clone).

## 2. Abra no editor com preview ao vivo
- Abra a pasta da inspiracao no VS Code: `code inspiracoes/<pasta>/`
- Instale a extensao "Live Server"
- Abra o editavel.html (dentro de site/.../) e clique em "Go Live"
- Cada vez que salvar, o navegador atualiza sozinho

## 3. Edicoes mais comuns
- Trocar texto: procure o texto no arquivo (Cmd+F) e substitua.
- Trocar cor: procure o codigo hex (ex: #2d5a4f) no <style> ou nos .css e altere.
- Trocar imagem: mude o atributo src da <img> para o caminho da sua imagem.
- Remover secao: localize a <section> ou <div> e apague o bloco inteiro.

## 4. Salve sua variacao
Trabalhe numa copia (ex: meu-design.html) e preserve o editavel.html original
como referencia. Nunca edite o clone dentro de site/ diretamente.

## 5. Limitacao (sites dinamicos)
Sites feitos em construtores visuais (ex: Showit) tem HTML dependente de JS,
dificil de editar a mao. Nesses casos, use o screenshot.png e o conteudo.md
como referencia de layout/copy, e o HTML so como base de estrutura e estilo.

## 6. Direitos autorais
Substitua copy, imagens e marca de terceiros pelo seu proprio conteudo.
O acervo e para inspiracao e ponto de partida, nao para republicar como esta.
