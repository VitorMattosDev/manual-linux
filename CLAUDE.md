# CLAUDE.md — Manual de Linux e Shell Scripting

Instruções de trabalho para o Claude Code neste repositório.

## O que é este projeto

Livro Quarto (HTML + PDF) em português do Brasil, publicado no GitHub Pages via GitHub Actions. **103 capítulos, 16 volumes, 5 fases.** A distribuição de referência é o **Kali Linux** (Debian rolling). A fila autoritativa está no `ROADMAP.md`. A estrutura canônica vive em `scripts/estrutura.py` — qualquer mudança de capítulos começa por lá.

## Modo de execução

Execução autônoma. Você está pré-aprovado para criar e editar arquivos, gerar figuras, rodar comandos de validação e fazer commits sem pedir confirmação a cada passo. **Única condição de parada:** erro real de bloqueio.

Um capítulo por sessão. `/clear` entre capítulos, `/compact` perto de 80% de contexto.

## Bootstrap da toolchain (rodar se ainda não foi rodado)

Faça isso antes do primeiro `quarto preview`, sem esperar ser pedido:

```bash
quarto install tinytex
# tlmgr pode não estar no PATH — localizar sem -type f (são symlinks)
TLMGR="$(command -v tlmgr || find "$HOME" -name tlmgr | head -n1)"
"$TLMGR" update --self
"$TLMGR" install standalone pgf pgfplots dvisvgm xcolor amsmath amsfonts fvextra koma-script
```

E **prepend do bin do TinyTeX no PATH da sessão** — este é o motivo mais comum de figura TikZ não renderizar (falha em `tikz.lua`, `imgdata nil`, ~linha 587). Não é pacote faltando, é PATH:

- Windows: `$HOME/AppData/Roaming/TinyTeX/bin/windows`
- Linux/macOS: `~/.TinyTeX/bin/<plataforma>`

## Anatomia de um capítulo

````markdown
# Título do capítulo {#sec-capNNN}

Parágrafo de abertura situando um problema concreto — nunca começar com definição de dicionário. De preferência, um cenário real de quem administra um sistema Linux.

## Seções de conteúdo

Texto explicativo, exemplos executáveis, diagramas TikZ, blocos de comando comentados. Todo comando é para ser digitado: mostrar o comando, a saída esperada (quando ajuda) e o que interpretar nela.

## 🐉 No Kali

O que muda especificamente no Kali Linux: repositório rolling, usuário padrão,
metapacotes de ferramentas, `kali-tweaks`, persistência, defaults diferentes de
um Debian/Ubuntu comum. Onde a família RHEL (dnf, firewalld, SELinux) diverge
de forma relevante, uma nota curta. OBRIGATÓRIA em todo capítulo.

## 🧪 Laboratório

Roteiro prático reproduzível: passos numerados que o leitor executa no próprio
ambiente (VM do Kali, de preferência), com o resultado esperado de cada passo.
OBRIGATÓRIA em todo capítulo.

## Resumo

3 a 6 bullets com o essencial.
````

Alvo: 2.500–4.000 palavras por capítulo. Densidade acima de volume.

## Política editorial

Manual técnico, prático e correto. Ensinar fazendo: cada conceito vem com o comando que o exercita.

**Comandos destrutivos** (`rm -rf`, `dd`, `mkfs`, `fdisk`, `cryptsetup luksFormat`) sempre acompanhados de aviso claro e, quando possível, de um ensaio seguro (usar arquivo-imagem via `losetup`, VM descartável, ou `--dry-run`). Nunca mostrar um comando que apaga disco sem sinalizar o risco na linha anterior.

**Conteúdo de segurança/ofensivo** (Volume 14, ferramentas do Kali): caráter educacional e defensivo, igual à política do Manual de Segurança. Pode explicar mecanismos e usar ferramentas públicas em contexto de laboratório; não pode dar passo a passo contra alvos reais nem encurtar o caminho de um ataque não autorizado. Toda ferramenta ofensiva vem com o contexto de uso legítimo (teste autorizado, laboratório próprio) e a menção de que uso não autorizado é crime (Lei 12.737/2012).

## Figuras

TikZ para diagramas esquemáticos e didáticos (árvore de processos, pilha de rede, hierarquia do FHS, fluxo do boot, camadas de um contêiner, máquina de estados de um processo). SVG/PNG embutido para o que depender de captura de tela de terminal ou de interface.

- Extensão: `_extensions/danmackinlay/tikz/` com **patches locais**
- **NUNCA rodar `quarto add` ou `quarto update`** nessa extensão — baixa o upstream sem os patches e quebra tudo
- Filtro `tikz` vem **antes** de `quarto` na lista de filters
- O template sempre chama `\usepackage{pgfplots}` — toda figura precisa dele, mesmo uma seta simples
- Estilos predefinidos (`curva`, `destaque`, `auxiliar`, `eixo`, `ponto`, `vetor`; cores `manualblue`, `manualred`, `manualgreen`, `manualyellow`, `manualgray`) vêm do template: **usar direto, nunca redefinir**

Sintaxe:

````markdown
::: {#fig-arvore-processos}
```{.tikz}
%%| filename: arvore-processos
%%| alt: Árvore de processos a partir do init, com PIDs
\begin{tikzpicture}
  ...
\end{tikzpicture}
```
Árvore de processos enraizada no PID 1.
:::
````

Referência no texto via `@fig-arvore-processos`.

## Regras que já custaram build vermelho

Ver `LICOES-MANUAIS.md` para o compilado completo. Os pontos que mais mordem:

- **Stub-first**: em projeto `book`, renderizar um `.qmd` isolado falha com "Book chapter not found" se qualquer capítulo listado no `_quarto.yml` não existir em disco. Rodar `python scripts/estrutura.py --stubs` após qualquer mudança de estrutura.
- **`--roadmap` e `--tudo` regravam o `ROADMAP.md` inteiro.** O `scripts/estrutura.py` **preserva** os marcadores `[x]` e `[~]` (função `status_atuais`, que relê o arquivo antes de reescrever) — mas a proteção é frágil: se o formato da linha (`- [x] **cap NNN**`) mudar, o regex para de casar e todo capítulo concluído volta a `[ ]` sem aviso. Não alterar esse formato, e conferir a contagem que o script imprime (`N concluidos preservados`). Na dúvida, usar só `--stubs`.
- **`quarto render --to pdf` limpa o `_book/`** e deixa apenas o PDF. As checagens de `?@`, de `<svg` e de `[?]` são feitas no HTML, então a ordem é sempre: render HTML → validar → render PDF. Invertido, o grep não acha os arquivos e o silêncio parece aprovação.
- **`execute: echo: true` vaza o fonte das células de diagrama.** Toda célula `{mermaid}` precisa de `%%| echo: false`. Blocos cercados estáticos (```` ```bash ````) não são células e não sofrem disso — e são o padrão aqui, já que o manual é cheio de comandos de shell exibidos como texto, não executados.
- **Blocos de comando são estáticos, não células executáveis.** Comandos de shell no manual usam cerca estática ```` ```bash ````, nunca ```` ```{bash} ````. Não queremos que o Quarto execute `rm`, `apt install` ou `mkfs` no runner. Célula executável só para algo comprovadamente inócuo e com propósito.
- **Nome de estilo TikZ próprio não pode colidir com chave do pgf.** `cap/.style` e `id/.style` derrubam o build com `The key '/tikz/cap' requires a value` — e o erro pode não aparecer no render isolado do capítulo, só no do livro inteiro. Usar `leg`, `ident`, `nd`, `bx`, `lb`, `nt`, `fl`, `seg`; evitar `cap`, `id`, `pos`, `at`, `to`, `mark`, `name`, `label`, `text`, `shape`.
- **Variável de `\foreach` no TikZ nunca pode ter nome de macro de acento do LaTeX** (`\c`, `\d`, `\t`, `\i`, `\u`, `\v`, `\r`, `\b`, `\k`, `\l`, `\o`, `\a`). Redefini-las num laço com texto acentuado dentro causa `TeX capacity exceeded`. Usar nomes de duas letras ou mais (`\idx`, `\tit`, `\cor`).
- **Crossrefs**: `@sec-`, `@fig-` e `@tbl-` **só** para o que já foi escrito. Referência a capítulo futuro é menção textual ("tema do Volume 12"), nunca link. Label não resolvido vira `?@sec-x` em vermelho.
- **`lang: pt`** fica na raiz do `_quarto.yml`, não sob `book:`.
- **`styles.css`** precisa de `/*-- scss:rules --*/` na primeira linha (está em `theme:`). Evitar `*/` logo após o marcador.
- **Notação LaTeX**: usar `^{*}` e não `^\*` — quebra o PDF.
- **Cuidado com caracteres shell em prosa e legendas**: `$`, `\`, `{`, `}`, `~`, `^`, `&`, `_`, `#`, `%` são especiais no LaTeX. Em bloco de código não há problema; em texto corrido e legendas de figura, escapar (`\$`, `\&`, `\_`, `\#`, `\%`, `\~{}`, `\^{}`) ou usar `code` inline (crase). O til de `~/.bashrc` em prosa fora de crase vira acento no PDF.
- **Substituição em massa** de notação: usar `str.replace` do Python. Nunca `sed` nem `grep -c`.
- **Commits**: apenas `-m "..."` simples. Nada de here-string do PowerShell dentro do Bash.
- **Emoji em `print()`** de script Python quebra no console do Windows. Em conteúdo de arquivo UTF-8 é seguro.
- **Write após heredoc**: se um arquivo foi modificado por bash/heredoc, a ferramenta Write exige um Read antes.
- **Avisos inofensivos**: `LF will be replaced by CRLF` e "Node.js 20 is deprecated" — ignorar.

## Validação antes de cada commit

Ordem obrigatória: **HTML primeiro, validar, PDF por último** — `--to pdf` apaga o HTML do `_book/`.

```bash
quarto render --to html
# 1. figuras: contar <svg no HTML gerado vs {.tikz} no .qmd
# 2. crossrefs quebrados — precisa retornar zero:
grep -rhoE '\?@[a-z-]+' _book/**/*.html
# 3. citações órfãs: procurar [?] no HTML
# 4. fonte de diagrama vazado: nenhum <pre class="sourceCode"> com o corpo
#    de um bloco {mermaid} (sintoma de célula sem `%%| echo: false`)
# 5. PDF local antes de qualquer push (LaTeX quebra no que o HTML aceita).
#    Este passo destrói o HTML acima, então roda só depois de 1–4:
quarto render --to pdf
```

Para conferir se uma figura TikZ entrou no PDF, contar Form XObjects por página com `pypdf` — `pdftotext` não recupera texto acentuado dos rótulos e dá falso negativo.

Commit no formato `cap NNN: <título>`, com o status do `ROADMAP.md` atualizado no mesmo commit.

## Validação antes do push

1. Render HTML completo do livro
2. Zero `?@` no grep
3. Todas as figuras TikZ produziram SVG
4. Nenhuma citação `@chave` crua sobrando no HTML
5. Após o push: `gh run watch <id> --exit-status` e depois `curl -I` na URL do Pages esperando 200

## Estratégia de produção

Fatia vertical: fechar um volume inteiro antes de abrir o próximo; fechar a Fase 1 antes da Fase 2. Em volume novo, o primeiro passo é o smoke test — validar que **uma** figura TikZ renderiza para SVG no HTML antes de escrever capítulo a capítulo.

`/model opus` para escrever capítulo. `/model sonnet` para tarefa mecânica (atualizar `_quarto.yml`, mover arquivo, ajustar ROADMAP).
