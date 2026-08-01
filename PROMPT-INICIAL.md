# Prompt de abertura — primeira sessão no Claude Code

Cole o texto abaixo na primeira sessão, dentro da pasta do repositório.

---

Você vai trabalhar no **Manual de Linux e Shell Scripting**, um livro Quarto em português do Brasil. Leia `CLAUDE.md`, `LICOES-MANUAIS.md` e `FIGURAS.md` antes de qualquer coisa — eles contêm as convenções e os erros já pagos em builds vermelhos de outros manuais. Depois leia o `ROADMAP.md`, que é a fila autoritativa de produção.

A distribuição de referência é o **Kali Linux** (Debian rolling). Os comandos, pacotes e defaults devem ser os do Kali; onde o Kali diverge de um Debian/Ubuntu comum, aponte a diferença.

Modo autônomo: você está pré-aprovado para criar e editar arquivos, gerar figuras, rodar validações e fazer commits sem me consultar a cada passo. Só pare em erro real de bloqueio.

**Tarefa desta sessão, em ordem:**

1. **Bootstrap da toolchain.** Instale TinyTeX e os pacotes LaTeX e instale o `chrome-headless-shell`. Localize o `tlmgr` com `find` sem `-type f` se ele não estiver no PATH, e rode `tlmgr update --self` antes de qualquer `install`. Faça o prepend do bin do TinyTeX no PATH da sessão — sem isso as figuras TikZ falham em silêncio.

2. **CSL da ABNT.** O arquivo `associacao-brasileira-de-normas-tecnicas.csl` já está na raiz (copiado dos outros manuais). Confirme que começa com `<?xml` e que tem um `<style`. Se estiver corrompido, rebaixe de:

   ```bash
   curl -fsSL -o associacao-brasileira-de-normas-tecnicas.csl \
     https://raw.githubusercontent.com/citation-style-language/styles/master/associacao-brasileira-de-normas-tecnicas.csl
   ```

3. **Extensão TikZ.** A pasta `_extensions/danmackinlay/tikz/` já está no repositório com os patches locais. **Não** rode `quarto add` nem `quarto update` nessa extensão em hipótese alguma.

4. **Stubs.** Rode `python scripts/estrutura.py --tudo` e confirme que os 103 stubs existem em disco. Renderizar sem eles falha com "Book chapter not found". Confira a contagem de `concluidos preservados` que o script imprime.

5. **Smoke test.** Antes de escrever qualquer conteúdo, crie uma figura TikZ mínima em `vol01/cap001-*.qmd` e rode `quarto render --to html`. Confirme que ela virou `<svg` no HTML gerado. Se não virou, o problema é PATH — resolva antes de seguir. Depois rode `quarto render --to pdf` e confirme que o PDF sai.

6. **Bootstrap do gh-pages.** Crie o branch vazio no remoto antes do primeiro publish:

   ```bash
   git push origin $(git commit-tree $(git hash-object -t tree /dev/null) -m 'init gh-pages'):refs/heads/gh-pages
   ```

7. **Primeiro capítulo.** Escreva o **cap 001 — "O que é Linux: kernel, distribuições e o modelo de software livre"** por inteiro, seguindo a anatomia do `CLAUDE.md`: abertura por problema concreto, corpo denso de 2.500 a 4.000 palavras, e as duas seções obrigatórias — `🐉 No Kali` e `🧪 Laboratório`. Sem crossref para capítulo que ainda não existe: referência a volume futuro é menção textual.

8. **Validação e commit.** Render HTML e PDF, `grep -rhoE '\?@[a-z-]+' _book/**/*.html` retornando zero, contagem de `<svg` batendo com os blocos `{.tikz}`. Commit como `cap 001: O que é Linux`, com o status atualizado no `ROADMAP.md` no mesmo commit. Push e `gh run watch <id> --exit-status`.

**Contexto para os exemplos:** trabalho em um provedor de internet (fibra e rádio) atendendo zona rural, então analogias e casos de administração de servidores, redes e Linux em produção são bem-vindos. O manual é geral, não um manual de ISP — mas os exemplos podem beber dessa realidade. E como uso Kali no dia a dia, os exemplos de ferramenta e fluxo devem assumir o Kali como ambiente.

**Lembrete importante sobre comandos destrutivos:** este manual tem muitos comandos que mexem em disco (`fdisk`, `mkfs`, `dd`, `cryptsetup`, `lvremove`). Todo comando destrutivo vem com aviso na linha anterior e, quando dá, com um ensaio seguro (arquivo-imagem via `losetup`, VM descartável, `--dry-run`). Nunca mostre um `dd of=/dev/sdX` sem sinalizar o risco.
