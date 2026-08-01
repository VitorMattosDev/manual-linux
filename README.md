# Manual de Linux e Shell Scripting

Livro técnico em português do Brasil sobre Linux e shell scripting, **do básico ao avançado**, usando o **Kali Linux** como distribuição de referência. Do primeiro comando no terminal até kernel, contêineres e virtualização, passando por administração de sistema, redes, segurança e automação com scripts.

Construído com [Quarto](https://quarto.org) (HTML + PDF), publicado no GitHub Pages via GitHub Actions.

## Estrutura

**103 capítulos, 16 volumes, 5 fases:**

1. **Fundamentos do Linux** — terminal, sistema de arquivos, usuários e permissões
2. **Administração do Sistema** — processos, pacotes, systemd, armazenamento
3. **Shell Scripting** — do primeiro script Bash ao processamento de texto e ao scripting robusto
4. **Redes, Segurança e Automação** — redes no Linux, hardening, ferramentas do Kali, automação
5. **Fronteira e Aprofundamento** — kernel, contêineres, virtualização

A fila de produção está no [`ROADMAP.md`](ROADMAP.md). A estrutura canônica (fonte única de verdade) vive em [`scripts/estrutura.py`](scripts/estrutura.py).

## Como produzir

Este repositório é escrito capítulo a capítulo com o Claude Code em modo autônomo. Para começar, abra o repositório no Claude Code e cole o conteúdo de [`PROMPT-INICIAL.md`](PROMPT-INICIAL.md). As convenções e os erros já conhecidos estão em [`CLAUDE.md`](CLAUDE.md) e [`LICOES-MANUAIS.md`](LICOES-MANUAIS.md).

## Build local

```bash
# gerar/atualizar stubs e ROADMAP a partir da estrutura canônica
python scripts/estrutura.py --tudo

# renderizar (HTML primeiro; --to pdf apaga o HTML do _book/)
quarto render --to html
quarto render --to pdf
```

Requer Quarto, TinyTeX (para o PDF e as figuras TikZ) e a extensão TikZ local em `_extensions/`. Ver [`FIGURAS.md`](FIGURAS.md).

## Licença

Conteúdo sob CC BY-SA 4.0.
