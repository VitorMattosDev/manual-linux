"""
Fonte unica de verdade da estrutura do Manual de Linux e Shell Scripting.

Gera:
  - o bloco `chapters:` do _quarto.yml
  - todos os stubs .qmd (regra stub-first)
  - o ROADMAP.md

Uso:
    python scripts/estrutura.py --stubs      # cria stubs faltantes
    python scripts/estrutura.py --quarto     # imprime o bloco chapters:
    python scripts/estrutura.py --roadmap    # regrava ROADMAP.md
    python scripts/estrutura.py --tudo
"""

import argparse
import os
import re
import unicodedata

# (fase, [(volume, titulo_volume, [titulos_capitulos])])
ESTRUTURA = [
    ("Fase 1 — Fundamentos do Linux", [
        ("Primeiros Passos: Linux e Kali", [
            "O que é Linux: kernel, distribuições e o modelo de software livre",
            "Por que Kali Linux: propósito, filosofia e quando não usá-lo",
            "Instalando o Kali: máquina virtual, bare metal, WSL e live USB",
            "Primeiro contato: sessão, ambiente Xfce e organização do sistema",
            "A estrutura de diretórios do Linux (FHS)",
            "Anatomia de um comando: shell, argumentos, opções e sintaxe",
            "Obtendo ajuda: man, info, tldr e a documentação do Kali",
        ]),
        ("O Terminal e o Shell", [
            "Emulador de terminal e shell: bash, zsh e o padrão do Kali",
            "Navegação: pwd, cd, ls e caminhos absolutos e relativos",
            "Manipulando arquivos e diretórios: cp, mv, rm, mkdir",
            "Visualizando conteúdo: cat, less, head, tail e more",
            "Redirecionamento e pipes: stdin, stdout e stderr",
            "Curingas, globbing e expansão de chaves",
            "Histórico, atalhos de teclado e produtividade no terminal",
        ]),
        ("Arquivos e o Sistema de Arquivos", [
            "Tipos de arquivo, inodes e a árvore de diretórios",
            "Links simbólicos e hard links",
            "Localizando arquivos: find, locate, which e type",
            "Compactação e arquivamento: tar, gzip, xz e zip",
            "Montagem de dispositivos e o comando mount",
            "Permissões de arquivo: leitura, escrita e execução",
        ]),
        ("Usuários, Grupos e Permissões", [
            "Usuários, grupos e o arquivo /etc/passwd",
            "O root, sudo e a elevação de privilégios",
            "Permissões especiais: SUID, SGID e sticky bit",
            "ACLs e atributos estendidos de arquivo",
            "Gerenciamento de usuários, senhas e o PAM",
            "Trabalhando como root no Kali com segurança",
        ]),
    ]),
    ("Fase 2 — Administração do Sistema", [
        ("Processos e Controle de Tarefas", [
            "O que é um processo: PID, estados e a árvore de processos",
            "Monitoramento: ps, top e htop",
            "Sinais e controle: kill, killall, nice e prioridades",
            "Jobs, primeiro e segundo plano, nohup e disown",
            "Multiplexação de terminal: tmux e screen",
            "Recursos do sistema: memória, CPU, uptime e limites",
        ]),
        ("Gerenciamento de Pacotes", [
            "APT e o modelo Debian: repositórios e o Kali rolling",
            "Instalando, removendo e atualizando pacotes com apt",
            "dpkg, arquivos .deb e resolução de dependências",
            "Repositórios do Kali, metapacotes e kali-tweaks",
            "Compilando a partir do código-fonte",
            "Alternativas: pipx, snap, flatpak e AppImage",
        ]),
        ("Boot, systemd e Serviços", [
            "O processo de inicialização: UEFI, GRUB e o kernel",
            "systemd: units, targets e o modelo de serviços",
            "Gerenciando serviços com systemctl",
            "Logs com journald e o syslog tradicional",
            "Agendamento: cron, at e timers do systemd",
            "Targets, modo de recuperação e resolução de problemas de boot",
        ]),
        ("Armazenamento e Sistemas de Arquivos", [
            "Discos, partições e a nomenclatura de dispositivos",
            "Particionamento com fdisk, parted e gdisk",
            "Sistemas de arquivos: ext4, Btrfs, XFS e formatação",
            "LVM: volumes lógicos flexíveis",
            "RAID por software com mdadm",
            "Criptografia de disco com LUKS e a persistência no Kali",
        ]),
    ]),
    ("Fase 3 — Shell Scripting", [
        ("Fundamentos de Shell Scripting", [
            "Do comando ao script: o primeiro script Bash",
            "Variáveis, o ambiente e o escopo de exportação",
            "Aspas, expansões e substituição de comandos",
            "Entrada e saída: read, echo e printf",
            "Condicionais: test, colchetes duplos e if",
            "Códigos de saída e o encadeamento de comandos",
            "Boas práticas: shebang, permissões e portabilidade",
        ]),
        ("Scripting Intermediário", [
            "Laços: for, while e until",
            "Funções, retorno e escopo de variáveis",
            "Arrays indexados e associativos",
            "Parâmetros posicionais e getopts",
            "Expansão de parâmetros avançada",
            "Aritmética e manipulação de números no shell",
        ]),
        ("Processamento de Texto", [
            "Expressões regulares: fundamentos e os diferentes sabores",
            "grep e a busca de padrões",
            "sed: o editor de fluxo",
            "awk: processamento por campos e registros",
            "cut, sort, uniq, tr e a caixa de ferramentas de texto",
            "Dados estruturados na linha de comando: jq, JSON e CSV",
            "Juntando tudo: pipelines de processamento de dados",
        ]),
        ("Scripting Avançado e Robusto", [
            "Tratamento de erros: set -euo pipefail e traps",
            "Depuração de scripts: set -x e ShellCheck",
            "Manipulando arquivos, descritores e processos em scripts",
            "Subshells, agrupamento e here-documents",
            "Sinais, processos filhos e execução em paralelo",
            "Interação com o usuário: menus, cores e caixas de diálogo",
            "Estruturando scripts grandes e bibliotecas de funções",
        ]),
    ]),
    ("Fase 4 — Redes, Segurança e Automação", [
        ("Redes no Linux", [
            "Fundamentos: interfaces, endereçamento IP e a pilha de rede",
            "Configuração de rede: ip, NetworkManager e arquivos",
            "Diagnóstico: ping, traceroute, ss, dig e mtr",
            "Acesso e transferência remota: SSH, scp e rsync",
            "HTTP na linha de comando: curl, wget e netcat",
            "Firewall no Linux: nftables e iptables",
            "Captura e análise de tráfego: tcpdump e tshark",
        ]),
        ("Segurança e o Ambiente Kali", [
            "Hardening do Linux: superfície de ataque e princípios",
            "Gerenciamento de segredos: chaves SSH e GPG",
            "Capabilities, isolamento e menor privilégio",
            "Confinamento: AppArmor, SELinux e sandboxing",
            "Auditoria, integridade de arquivos e detecção de alterações",
            "O ecossistema de ferramentas do Kali: categorias e fluxos",
            "Anonimato e privacidade: proxychains, Tor e VPN",
        ]),
        ("Automação e Produtividade", [
            "Personalizando o shell: .bashrc, .zshrc, aliases e funções",
            "Zsh, plugins e o prompt do Kali",
            "Automatizando tarefas com cron e scripts agendados",
            "Controle de versão com Git na linha de comando",
            "Editores no terminal: vim e nano",
            "Dotfiles e ambientes reproduzíveis",
        ]),
    ]),
    ("Fase 5 — Fronteira e Aprofundamento", [
        ("Kernel, Contêineres e Virtualização", [
            "O kernel Linux: módulos, /proc e /sys",
            "Contêineres por dentro: namespaces, cgroups e Docker",
            "Virtualização: KVM, QEMU e o laboratório de estudos",
            "Compilação, toolchains e o ecossistema de desenvolvimento",
            "Observabilidade e desempenho: strace, ltrace e perf",
            "Para onde ir depois: certificações, comunidade e prática contínua",
        ]),
    ]),
]


def slug(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", "-", t)
    t = re.sub(r"-+", "-", t).strip("-")
    if len(t) > 46:
        t = t[:46].rsplit("-", 1)[0]
    return t


def caminhos():
    """Retorna lista de (fase, num_vol, titulo_vol, num_cap, titulo_cap, path)."""
    out = []
    nvol = 0
    ncap = 0
    for fase, volumes in ESTRUTURA:
        for titulo_vol, capitulos in volumes:
            nvol += 1
            for titulo_cap in capitulos:
                ncap += 1
                path = f"vol{nvol:02d}/cap{ncap:03d}-{slug(titulo_cap)}.qmd"
                out.append((fase, nvol, titulo_vol, ncap, titulo_cap, path))
    return out


def gerar_stubs(raiz="."):
    criados = 0
    for _, _, _, ncap, titulo, path in caminhos():
        destino = os.path.join(raiz, path)
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        if os.path.exists(destino):
            continue
        with open(destino, "w", encoding="utf-8") as f:
            f.write(f"# {titulo} {{#sec-cap{ncap:03d}}}\n\n*(em elaboracao)*\n")
        criados += 1
    print(f"stubs criados: {criados}")


def bloco_quarto():
    linhas = ["  chapters:", "    - index.qmd"]
    fase_atual = None
    nvol = 0
    for fase, vol, titulo_vol, _, _, path in caminhos():
        if fase != fase_atual:
            fase_atual = fase
            linhas.append(f"    # ===== {fase} =====")
        if vol != nvol:
            nvol = vol
            linhas.append("    - part: |")
            linhas.append(f"        Volume {vol} — {titulo_vol}")
            linhas.append("      chapters:")
        linhas.append(f"        - {path}")
    linhas.append("    - referencias.qmd")
    return "\n".join(linhas)


def status_atuais(raiz="."):
    """Le o ROADMAP.md existente e devolve {num_cap: marcador}.

    Sem isso, regravar o ROADMAP zeraria todo capitulo ja concluido -- o
    arquivo e a fila autoritativa de producao, nao um artefato descartavel.
    """
    destino = os.path.join(raiz, "ROADMAP.md")
    if not os.path.exists(destino):
        return {}
    with open(destino, encoding="utf-8") as f:
        conteudo = f.read()
    achados = re.findall(r"^- \[([ x~])\] \*\*cap (\d{3})\*\*", conteudo, re.M)
    return {int(num): marca for marca, num in achados}


def gerar_roadmap(raiz="."):
    status = status_atuais(raiz)
    L = ["# ROADMAP — Manual de Linux e Shell Scripting", "",
         "Fila autoritativa de producao. Status: `[ ]` pendente | `[~]` em andamento | `[x]` concluido.",
         "", "Commit por capitulo: `cap NNN: <titulo>` com o status atualizado no mesmo commit.", ""]
    fase_atual = None
    nvol = 0
    for fase, vol, titulo_vol, ncap, titulo, path in caminhos():
        if fase != fase_atual:
            fase_atual = fase
            L += ["", f"## {fase}", ""]
        if vol != nvol:
            nvol = vol
            L += ["", f"### Volume {vol} — {titulo_vol}", ""]
        marca = status.get(ncap, " ")
        L.append(f"- [{marca}] **cap {ncap:03d}** - {titulo} - `{path}`")
    total = len(caminhos())
    concluidos = sum(1 for m in status.values() if m == "x")
    L += ["", "---", "",
          f"**Total:** {total} capitulos em {nvol} volumes "
          f"({concluidos} concluidos).", ""]
    with open(os.path.join(raiz, "ROADMAP.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"ROADMAP.md gravado ({total} capitulos, "
          f"{concluidos} concluidos preservados)")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--stubs", action="store_true")
    p.add_argument("--quarto", action="store_true")
    p.add_argument("--roadmap", action="store_true")
    p.add_argument("--tudo", action="store_true")
    a = p.parse_args()
    if a.tudo or a.stubs:
        gerar_stubs()
    if a.tudo or a.roadmap:
        gerar_roadmap()
    if a.quarto:
        print(bloco_quarto())
    if not any([a.stubs, a.quarto, a.roadmap, a.tudo]):
        c = caminhos()
        print(f"{len(c)} capitulos, {c[-1][1]} volumes")
