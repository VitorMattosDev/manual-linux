# Figuras — TikZ

## Instalação da extensão (com patches)

A pasta `_extensions/danmackinlay/tikz/` deve ser copiada de `figuras-tikz-kit.zip`, que contém a versão **com os patches locais**.

> **Nunca** rodar `quarto add danmackinlay/tikz` nem `quarto update`. Ambos baixam o upstream sem os patches e quebram a renderização.

## Configuração no `_quarto.yml`

```yaml
filters:
  - tikz      # precisa vir ANTES de quarto
  - quarto

tikz:
  svg-engine: dvisvgm
  cache: true
```

## Sintaxe padrão

````markdown
::: {#fig-nome-da-figura}
```{.tikz}
%%| filename: nome-da-figura
%%| alt: Descrição textual da figura para acessibilidade
\begin{tikzpicture}
  \draw[curva] (0,0) -- (3,2);
  \node[ponto] at (3,2) {};
\end{tikzpicture}
```
Legenda da figura, antes do fechamento do div.
:::
````

Referência no texto: `@fig-nome-da-figura`.

## Estilos disponíveis (do template — não redefinir)

- Linhas: `curva`, `destaque`, `auxiliar`, `eixo`
- Nós: `ponto`, `vetor`
- Cores: `manualblue`, `manualred`, `manualgreen`, `manualyellow`, `manualgray`

## Diagramas típicos deste manual

| Tema | Tipo de figura |
|---|---|
| Hierarquia do FHS, árvore de diretórios | Árvore |
| Árvore de processos (init/PID 1) | Árvore |
| Pilha de rede, encapsulamento TCP/IP | Diagrama de blocos em camadas |
| Fluxo do boot (UEFI → GRUB → kernel → systemd) | Linha de fases |
| Redirecionamento, pipes e descritores de arquivo | Diagrama de fluxo |
| Máquina de estados de um processo | Máquina de estados |
| Camadas de um contêiner, namespaces e cgroups | Diagrama de blocos |
| LVM (PV → VG → LV), RAID, LUKS | Diagrama de blocos empilhados |

## Checagem obrigatória

Após o render, contar `<svg` no HTML gerado e comparar com o número de blocos `{.tikz}` no `.qmd`. Divergência significa figura que falhou em silêncio — quase sempre PATH do TinyTeX.
