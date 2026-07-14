# PRD — Acervo de Inspiracoes do Time (v2)

## CAMADA DE PRODUTO

### 1. Contexto e problema
O time de design e copy consulta constantemente landing pages de terceiros como
referencia, mas hoje o processo e informal: links soltos, prints perdidos e nenhuma
padronizacao do que foi inspirador e por que. Alem de arquivar, o time quer produzir
designs novos a partir dessas referencias, o que exige ter o HTML e os assets em maos,
nao so uma imagem. Falta uma ferramenta que capture a pagina inteira, organize o acervo
de forma pesquisavel e sirva de ponto de partida para a producao.

### 2. Objetivo
Criar um repositorio Git de uso diario que permita capturar qualquer landing page como
inspiracao estruturada, arquiva-la de forma consistente e navegavel, e usa-la como base
para novos designs, equilibrando arquivar (consulta rapida) e produzir (edicao do HTML).

### 3. Publico-alvo
Time interno de design e copy, perfil tecnico intermediario, confortavel com Git e edicao
de HTML/CSS. Uso diario e colaborativo: varios capturam e todos consultam o mesmo acervo
versionado.

### 4. As tres capacidades do produto
Captura: transforma uma URL em inspiracao estruturada em disco.
Catalogo: mantem o acervo padronizado, versionado e pesquisavel.
Producao: usa a copia editavel como base para criar designs novos.

### 5. Fluxos principais (caminho feliz)
Captura: comando unico com URL + nota + tags gera a pasta padronizada e confirma caminhos.
Consulta: gera a galeria, que le os metadados e mostra os cartoes; busca por titulo/nota/tag.
Producao: abre editavel.html no editor com preview ao vivo, edita e salva variacoes.
Colaborativo: cada um captura, commita e da push; os demais dao pull e veem na galeria.

### 6. Fora de escopo (nesta fase)
Edicao visual arrasta-e-solta; app web multiusuario hospedado; autenticacao; publicacao
externa; captura em massa/agendada; captura atras de login; contornar bloqueios/CAPTCHAs;
replica visual perfeita de sites dinamicos.

### 7. Criterios de sucesso
Adocao da captura no fluxo diario; acervo crescendo com metadados bem preenchidos; consulta
recorrente da galeria; designs novos partindo da copia editavel; capturar+catalogar em menos
de 1-2 min. Maturidade quando o fluxo justificar evoluir para app web hospedado.

## CAMADA DE IMPLEMENTACAO

### 8. Requisitos nao funcionais
Performance: captura em ate ~1-2 min; galeria abre instantanea para dezenas/centenas de itens.
Confiabilidade: tolerante a falhas parciais; ou conclui integra ou falha limpa.
Usabilidade: comando unico; mensagens claras; galeria navegavel sem instrucoes.
Compatibilidade: macOS, local, navegador moderno; galeria estatica sem servidor.
Seguranca: credenciais so em variavel de ambiente, nunca no codigo/Git; respeita bloqueios;
so conteudo publico; nao coleta dados pessoais nem imagens de rostos.
Manutenibilidade: estrutura de pastas e esquema de metadados fixos e identicos.

### 9. Dependencias e integracoes
Clone navegavel: ferramenta de espelhamento (wget). Captura estruturada (screenshot fullpage,
markdown, metadados, links): servico de extracao via API (Firecrawl) com chave em variavel de
ambiente. Versionamento: Git. Producao: editor de codigo com preview ao vivo. Leitura de
metadados: parser local. Tudo documentado no README.

### 10. Esquema de metadados
Obrigatorios: id; url; titulo; data/hora; ao menos 1 tag.
Recomendados: nota do autor; autor da captura.
Opcionais: paleta de cores; descricao; caminhos dos artefatos.
Campos opcionais ausentes nao invalidam; a galeria degrada graciosamente.
Estrutura fixa por inspiracao: site/, editavel.html, screenshot.png, conteudo.md, meta.json.

### 11. Taxonomia de tags
Portugues, minusculas, sem acento, sem espaco (hifen para compostos), preferir singular.
Categorias sugeridas: tipo (landing, checkout, pricing), estilo (dark-mode, minimalista),
destaque (depoimentos, hero-video). Lista aberta, mas com sugeridas no README.

### 12. Criterios de aceitacao por funcionalidade
Captura: gera pasta completa com clone offline, screenshot fiel, markdown e metadados
obrigatorios, no tempo alvo; site dinamico ainda produz screenshot e markdown validos.
Catalogo: estrutura identica, metadados validos, nova inspiracao versionada sem quebrar consumo.
Galeria: le tudo automaticamente, mostra cartoes, busca por titulo/nota/tag, degrada bem.
Producao: editavel abre com preview, edicoes comuns funcionam, original preservado.

### 13. Casos de falha e comportamento degradado
Clone parcial: continua, registra o que faltou, pasta integra. Site bloqueia/login/403: nao
contorna, registra e segue; pagina principal inacessivel falha limpa. Servico de extracao
indisponivel/sem chave: entrega clone e avisa que screenshot/markdown nao vieram. Metadados
opcionais ausentes: galeria mostra com marcadores. Sempre: nao corromper o acervo e comunicar.

## SECAO UX / INTERFACE

### 14. Interface e alvo visual
Galeria como interface principal: limpa, densa em informacao, escaneavel. Cada inspiracao e um
cartao com screenshot em destaque, titulo, nota e tags, com acesso ao clone e ao editavel.
Fidelidade visual e prioridade. Busca imediata; degrada bem quando faltar artefato.

## GOVERNANCA E ROADMAP

### 15. Governanca da taxonomia de tags
Define-se um dono da taxonomia, que revisa periodicamente (ex: mensal), consolida sinonimos,
aposenta redundancias e mantem a lista sugerida do README. Tags recorrentes viram sugeridas.

### 16. Roadmap / evolucao futura
v1 (atual): local, Git, comando unico, pasta padronizada, galeria estatica, edicao no editor.
v2 (condicionada): app web hospedado, formulario com URL, galeria compartilhada, chave no
servidor, busca/filtros avancados, possivel autenticacao. Reaproveita captura e metadados da v1.
