# Guia de Publicacao — Acervo de Inspiracoes

App no ar: https://1bertogit.github.io/inspiracoes-time/
Repositorio: https://github.com/1bertogit/inspiracoes-time

## Ciclo diario (curador)

1. Capturar uma inspiracao nova (roda LOCAL, usa sua API key):
       ./bin/capturar https://site-de-referencia.com

2. Gerar o indice do app:
       ./bin/galeria
   (isso atualiza o dados.json)

3. Publicar para o time:
       git add -A
       git commit -m "add: inspiracao <nome do site>"
       git push

4. Em 1-2 minutos o GitHub Pages atualiza sozinho.
   Confira em https://1bertogit.github.io/inspiracoes-time/

## Ver localmente antes de publicar

O app usa fetch(dados.json), entao NAO funciona abrindo com "open".
Precisa de servidor:
       cd ~/inspiracoes-time
       python3 -m http.server 8000
Depois abra http://localhost:8000

## Regras importantes

- A API key do Firecrawl NUNCA vai para o repositorio. Fica so na
  variavel de ambiente da sua maquina. O resultado.json (resposta bruta)
  esta no .gitignore de proposito.
- Todos os caminhos do app sao relativos, para funcionar no subcaminho
  do GitHub Pages. Nao use caminhos absolutos.
- O repositorio e PUBLICO: qualquer pessoa com o link ve o acervo.
  As inspiracoes contem imagens, textos e marcas de terceiros. Use como
  referencia/esqueleto para criar peca propria, nao republique como seu.

## Atencao ao peso do repositorio

Cada screenshot full-page pesa ~2 MB e cada clone (site/) tambem soma.
Com muitas inspiracoes o repo cresce rapido. Se ficar pesado, opcoes:
- otimizar/comprimir os PNGs de screenshot
- manter os clones site/ apenas locais e publicar so screenshot + texto
Decidir quando chegar perto de limites (repos GitHub: aviso em ~1 GB).

## Tags (padrao)

Portugues, minusculas, sem acento, sem espaco (use hifen para compostos,
ex: email-marketing). Prefira singular.
