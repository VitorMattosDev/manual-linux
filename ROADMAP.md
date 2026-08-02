# ROADMAP — Manual de Linux e Shell Scripting

Fila autoritativa de producao. Status: `[ ]` pendente | `[~]` em andamento | `[x]` concluido.

Commit por capitulo: `cap NNN: <titulo>` com o status atualizado no mesmo commit.


## Fase 1 — Fundamentos do Linux


### Volume 1 — Primeiros Passos: Linux e Kali

- [x] **cap 001** - O que é Linux: kernel, distribuições e o modelo de software livre - `vol01/cap001-o-que-e-linux-kernel-distribuicoes-e-o-modelo.qmd`
- [x] **cap 002** - Por que Kali Linux: propósito, filosofia e quando não usá-lo - `vol01/cap002-por-que-kali-linux-proposito-filosofia-e.qmd`
- [x] **cap 003** - Instalando o Kali: máquina virtual, bare metal, WSL e live USB - `vol01/cap003-instalando-o-kali-maquina-virtual-bare-metal.qmd`
- [x] **cap 004** - Primeiro contato: sessão, ambiente Xfce e organização do sistema - `vol01/cap004-primeiro-contato-sessao-ambiente-xfce-e.qmd`
- [x] **cap 005** - A estrutura de diretórios do Linux (FHS) - `vol01/cap005-a-estrutura-de-diretorios-do-linux-fhs.qmd`
- [x] **cap 006** - Anatomia de um comando: shell, argumentos, opções e sintaxe - `vol01/cap006-anatomia-de-um-comando-shell-argumentos.qmd`
- [x] **cap 007** - Obtendo ajuda: man, info, tldr e a documentação do Kali - `vol01/cap007-obtendo-ajuda-man-info-tldr-e-a-documentacao.qmd`

### Volume 2 — O Terminal e o Shell

- [x] **cap 008** - Emulador de terminal e shell: bash, zsh e o padrão do Kali - `vol02/cap008-emulador-de-terminal-e-shell-bash-zsh-e-o.qmd`
- [x] **cap 009** - Navegação: pwd, cd, ls e caminhos absolutos e relativos - `vol02/cap009-navegacao-pwd-cd-ls-e-caminhos-absolutos-e.qmd`
- [x] **cap 010** - Manipulando arquivos e diretórios: cp, mv, rm, mkdir - `vol02/cap010-manipulando-arquivos-e-diretorios-cp-mv-rm.qmd`
- [x] **cap 011** - Visualizando conteúdo: cat, less, head, tail e more - `vol02/cap011-visualizando-conteudo-cat-less-head-tail-e.qmd`
- [x] **cap 012** - Redirecionamento e pipes: stdin, stdout e stderr - `vol02/cap012-redirecionamento-e-pipes-stdin-stdout-e-stderr.qmd`
- [x] **cap 013** - Curingas, globbing e expansão de chaves - `vol02/cap013-curingas-globbing-e-expansao-de-chaves.qmd`
- [x] **cap 014** - Histórico, atalhos de teclado e produtividade no terminal - `vol02/cap014-historico-atalhos-de-teclado-e-produtividade.qmd`

### Volume 3 — Arquivos e o Sistema de Arquivos

- [x] **cap 015** - Tipos de arquivo, inodes e a árvore de diretórios - `vol03/cap015-tipos-de-arquivo-inodes-e-a-arvore-de.qmd`
- [x] **cap 016** - Links simbólicos e hard links - `vol03/cap016-links-simbolicos-e-hard-links.qmd`
- [x] **cap 017** - Localizando arquivos: find, locate, which e type - `vol03/cap017-localizando-arquivos-find-locate-which-e-type.qmd`
- [x] **cap 018** - Compactação e arquivamento: tar, gzip, xz e zip - `vol03/cap018-compactacao-e-arquivamento-tar-gzip-xz-e-zip.qmd`
- [x] **cap 019** - Montagem de dispositivos e o comando mount - `vol03/cap019-montagem-de-dispositivos-e-o-comando-mount.qmd`
- [x] **cap 020** - Permissões de arquivo: leitura, escrita e execução - `vol03/cap020-permissoes-de-arquivo-leitura-escrita-e.qmd`

### Volume 4 — Usuários, Grupos e Permissões

- [x] **cap 021** - Usuários, grupos e o arquivo /etc/passwd - `vol04/cap021-usuarios-grupos-e-o-arquivo-etc-passwd.qmd`
- [x] **cap 022** - O root, sudo e a elevação de privilégios - `vol04/cap022-o-root-sudo-e-a-elevacao-de-privilegios.qmd`
- [x] **cap 023** - Permissões especiais: SUID, SGID e sticky bit - `vol04/cap023-permissoes-especiais-suid-sgid-e-sticky-bit.qmd`
- [x] **cap 024** - ACLs e atributos estendidos de arquivo - `vol04/cap024-acls-e-atributos-estendidos-de-arquivo.qmd`
- [x] **cap 025** - Gerenciamento de usuários, senhas e o PAM - `vol04/cap025-gerenciamento-de-usuarios-senhas-e-o-pam.qmd`
- [x] **cap 026** - Trabalhando como root no Kali com segurança - `vol04/cap026-trabalhando-como-root-no-kali-com-seguranca.qmd`

## Fase 2 — Administração do Sistema


### Volume 5 — Processos e Controle de Tarefas

- [x] **cap 027** - O que é um processo: PID, estados e a árvore de processos - `vol05/cap027-o-que-e-um-processo-pid-estados-e-a-arvore-de.qmd`
- [x] **cap 028** - Monitoramento: ps, top e htop - `vol05/cap028-monitoramento-ps-top-e-htop.qmd`
- [x] **cap 029** - Sinais e controle: kill, killall, nice e prioridades - `vol05/cap029-sinais-e-controle-kill-killall-nice-e.qmd`
- [x] **cap 030** - Jobs, primeiro e segundo plano, nohup e disown - `vol05/cap030-jobs-primeiro-e-segundo-plano-nohup-e-disown.qmd`
- [x] **cap 031** - Multiplexação de terminal: tmux e screen - `vol05/cap031-multiplexacao-de-terminal-tmux-e-screen.qmd`
- [x] **cap 032** - Recursos do sistema: memória, CPU, uptime e limites - `vol05/cap032-recursos-do-sistema-memoria-cpu-uptime-e.qmd`

### Volume 6 — Gerenciamento de Pacotes

- [x] **cap 033** - APT e o modelo Debian: repositórios e o Kali rolling - `vol06/cap033-apt-e-o-modelo-debian-repositorios-e-o-kali.qmd`
- [x] **cap 034** - Instalando, removendo e atualizando pacotes com apt - `vol06/cap034-instalando-removendo-e-atualizando-pacotes.qmd`
- [x] **cap 035** - dpkg, arquivos .deb e resolução de dependências - `vol06/cap035-dpkg-arquivos-deb-e-resolucao-de-dependencias.qmd`
- [x] **cap 036** - Repositórios do Kali, metapacotes e kali-tweaks - `vol06/cap036-repositorios-do-kali-metapacotes-e-kali-tweaks.qmd`
- [x] **cap 037** - Compilando a partir do código-fonte - `vol06/cap037-compilando-a-partir-do-codigo-fonte.qmd`
- [x] **cap 038** - Alternativas: pipx, snap, flatpak e AppImage - `vol06/cap038-alternativas-pipx-snap-flatpak-e-appimage.qmd`

### Volume 7 — Boot, systemd e Serviços

- [x] **cap 039** - O processo de inicialização: UEFI, GRUB e o kernel - `vol07/cap039-o-processo-de-inicializacao-uefi-grub-e-o.qmd`
- [x] **cap 040** - systemd: units, targets e o modelo de serviços - `vol07/cap040-systemd-units-targets-e-o-modelo-de-servicos.qmd`
- [x] **cap 041** - Gerenciando serviços com systemctl - `vol07/cap041-gerenciando-servicos-com-systemctl.qmd`
- [x] **cap 042** - Logs com journald e o syslog tradicional - `vol07/cap042-logs-com-journald-e-o-syslog-tradicional.qmd`
- [x] **cap 043** - Agendamento: cron, at e timers do systemd - `vol07/cap043-agendamento-cron-at-e-timers-do-systemd.qmd`
- [x] **cap 044** - Targets, modo de recuperação e resolução de problemas de boot - `vol07/cap044-targets-modo-de-recuperacao-e-resolucao-de.qmd`

### Volume 8 — Armazenamento e Sistemas de Arquivos

- [ ] **cap 045** - Discos, partições e a nomenclatura de dispositivos - `vol08/cap045-discos-particoes-e-a-nomenclatura-de.qmd`
- [ ] **cap 046** - Particionamento com fdisk, parted e gdisk - `vol08/cap046-particionamento-com-fdisk-parted-e-gdisk.qmd`
- [ ] **cap 047** - Sistemas de arquivos: ext4, Btrfs, XFS e formatação - `vol08/cap047-sistemas-de-arquivos-ext4-btrfs-xfs-e.qmd`
- [ ] **cap 048** - LVM: volumes lógicos flexíveis - `vol08/cap048-lvm-volumes-logicos-flexiveis.qmd`
- [ ] **cap 049** - RAID por software com mdadm - `vol08/cap049-raid-por-software-com-mdadm.qmd`
- [ ] **cap 050** - Criptografia de disco com LUKS e a persistência no Kali - `vol08/cap050-criptografia-de-disco-com-luks-e-a.qmd`

## Fase 3 — Shell Scripting


### Volume 9 — Fundamentos de Shell Scripting

- [ ] **cap 051** - Do comando ao script: o primeiro script Bash - `vol09/cap051-do-comando-ao-script-o-primeiro-script-bash.qmd`
- [ ] **cap 052** - Variáveis, o ambiente e o escopo de exportação - `vol09/cap052-variaveis-o-ambiente-e-o-escopo-de-exportacao.qmd`
- [ ] **cap 053** - Aspas, expansões e substituição de comandos - `vol09/cap053-aspas-expansoes-e-substituicao-de-comandos.qmd`
- [ ] **cap 054** - Entrada e saída: read, echo e printf - `vol09/cap054-entrada-e-saida-read-echo-e-printf.qmd`
- [ ] **cap 055** - Condicionais: test, colchetes duplos e if - `vol09/cap055-condicionais-test-colchetes-duplos-e-if.qmd`
- [ ] **cap 056** - Códigos de saída e o encadeamento de comandos - `vol09/cap056-codigos-de-saida-e-o-encadeamento-de-comandos.qmd`
- [ ] **cap 057** - Boas práticas: shebang, permissões e portabilidade - `vol09/cap057-boas-praticas-shebang-permissoes-e.qmd`

### Volume 10 — Scripting Intermediário

- [ ] **cap 058** - Laços: for, while e until - `vol10/cap058-lacos-for-while-e-until.qmd`
- [ ] **cap 059** - Funções, retorno e escopo de variáveis - `vol10/cap059-funcoes-retorno-e-escopo-de-variaveis.qmd`
- [ ] **cap 060** - Arrays indexados e associativos - `vol10/cap060-arrays-indexados-e-associativos.qmd`
- [ ] **cap 061** - Parâmetros posicionais e getopts - `vol10/cap061-parametros-posicionais-e-getopts.qmd`
- [ ] **cap 062** - Expansão de parâmetros avançada - `vol10/cap062-expansao-de-parametros-avancada.qmd`
- [ ] **cap 063** - Aritmética e manipulação de números no shell - `vol10/cap063-aritmetica-e-manipulacao-de-numeros-no-shell.qmd`

### Volume 11 — Processamento de Texto

- [ ] **cap 064** - Expressões regulares: fundamentos e os diferentes sabores - `vol11/cap064-expressoes-regulares-fundamentos-e-os.qmd`
- [ ] **cap 065** - grep e a busca de padrões - `vol11/cap065-grep-e-a-busca-de-padroes.qmd`
- [ ] **cap 066** - sed: o editor de fluxo - `vol11/cap066-sed-o-editor-de-fluxo.qmd`
- [ ] **cap 067** - awk: processamento por campos e registros - `vol11/cap067-awk-processamento-por-campos-e-registros.qmd`
- [ ] **cap 068** - cut, sort, uniq, tr e a caixa de ferramentas de texto - `vol11/cap068-cut-sort-uniq-tr-e-a-caixa-de-ferramentas-de.qmd`
- [ ] **cap 069** - Dados estruturados na linha de comando: jq, JSON e CSV - `vol11/cap069-dados-estruturados-na-linha-de-comando-jq.qmd`
- [ ] **cap 070** - Juntando tudo: pipelines de processamento de dados - `vol11/cap070-juntando-tudo-pipelines-de-processamento-de.qmd`

### Volume 12 — Scripting Avançado e Robusto

- [ ] **cap 071** - Tratamento de erros: set -euo pipefail e traps - `vol12/cap071-tratamento-de-erros-set-euo-pipefail-e-traps.qmd`
- [ ] **cap 072** - Depuração de scripts: set -x e ShellCheck - `vol12/cap072-depuracao-de-scripts-set-x-e-shellcheck.qmd`
- [ ] **cap 073** - Manipulando arquivos, descritores e processos em scripts - `vol12/cap073-manipulando-arquivos-descritores-e-processos.qmd`
- [ ] **cap 074** - Subshells, agrupamento e here-documents - `vol12/cap074-subshells-agrupamento-e-here-documents.qmd`
- [ ] **cap 075** - Sinais, processos filhos e execução em paralelo - `vol12/cap075-sinais-processos-filhos-e-execucao-em-paralelo.qmd`
- [ ] **cap 076** - Interação com o usuário: menus, cores e caixas de diálogo - `vol12/cap076-interacao-com-o-usuario-menus-cores-e-caixas.qmd`
- [ ] **cap 077** - Estruturando scripts grandes e bibliotecas de funções - `vol12/cap077-estruturando-scripts-grandes-e-bibliotecas-de.qmd`

## Fase 4 — Redes, Segurança e Automação


### Volume 13 — Redes no Linux

- [ ] **cap 078** - Fundamentos: interfaces, endereçamento IP e a pilha de rede - `vol13/cap078-fundamentos-interfaces-enderecamento-ip-e-a.qmd`
- [ ] **cap 079** - Configuração de rede: ip, NetworkManager e arquivos - `vol13/cap079-configuracao-de-rede-ip-networkmanager-e.qmd`
- [ ] **cap 080** - Diagnóstico: ping, traceroute, ss, dig e mtr - `vol13/cap080-diagnostico-ping-traceroute-ss-dig-e-mtr.qmd`
- [ ] **cap 081** - Acesso e transferência remota: SSH, scp e rsync - `vol13/cap081-acesso-e-transferencia-remota-ssh-scp-e-rsync.qmd`
- [ ] **cap 082** - HTTP na linha de comando: curl, wget e netcat - `vol13/cap082-http-na-linha-de-comando-curl-wget-e-netcat.qmd`
- [ ] **cap 083** - Firewall no Linux: nftables e iptables - `vol13/cap083-firewall-no-linux-nftables-e-iptables.qmd`
- [ ] **cap 084** - Captura e análise de tráfego: tcpdump e tshark - `vol13/cap084-captura-e-analise-de-trafego-tcpdump-e-tshark.qmd`

### Volume 14 — Segurança e o Ambiente Kali

- [ ] **cap 085** - Hardening do Linux: superfície de ataque e princípios - `vol14/cap085-hardening-do-linux-superficie-de-ataque-e.qmd`
- [ ] **cap 086** - Gerenciamento de segredos: chaves SSH e GPG - `vol14/cap086-gerenciamento-de-segredos-chaves-ssh-e-gpg.qmd`
- [ ] **cap 087** - Capabilities, isolamento e menor privilégio - `vol14/cap087-capabilities-isolamento-e-menor-privilegio.qmd`
- [ ] **cap 088** - Confinamento: AppArmor, SELinux e sandboxing - `vol14/cap088-confinamento-apparmor-selinux-e-sandboxing.qmd`
- [ ] **cap 089** - Auditoria, integridade de arquivos e detecção de alterações - `vol14/cap089-auditoria-integridade-de-arquivos-e-deteccao.qmd`
- [ ] **cap 090** - O ecossistema de ferramentas do Kali: categorias e fluxos - `vol14/cap090-o-ecossistema-de-ferramentas-do-kali.qmd`
- [ ] **cap 091** - Anonimato e privacidade: proxychains, Tor e VPN - `vol14/cap091-anonimato-e-privacidade-proxychains-tor-e-vpn.qmd`

### Volume 15 — Automação e Produtividade

- [ ] **cap 092** - Personalizando o shell: .bashrc, .zshrc, aliases e funções - `vol15/cap092-personalizando-o-shell-bashrc-zshrc-aliases-e.qmd`
- [ ] **cap 093** - Zsh, plugins e o prompt do Kali - `vol15/cap093-zsh-plugins-e-o-prompt-do-kali.qmd`
- [ ] **cap 094** - Automatizando tarefas com cron e scripts agendados - `vol15/cap094-automatizando-tarefas-com-cron-e-scripts.qmd`
- [ ] **cap 095** - Controle de versão com Git na linha de comando - `vol15/cap095-controle-de-versao-com-git-na-linha-de-comando.qmd`
- [ ] **cap 096** - Editores no terminal: vim e nano - `vol15/cap096-editores-no-terminal-vim-e-nano.qmd`
- [ ] **cap 097** - Dotfiles e ambientes reproduzíveis - `vol15/cap097-dotfiles-e-ambientes-reproduziveis.qmd`

## Fase 5 — Fronteira e Aprofundamento


### Volume 16 — Kernel, Contêineres e Virtualização

- [ ] **cap 098** - O kernel Linux: módulos, /proc e /sys - `vol16/cap098-o-kernel-linux-modulos-proc-e-sys.qmd`
- [ ] **cap 099** - Contêineres por dentro: namespaces, cgroups e Docker - `vol16/cap099-conteineres-por-dentro-namespaces-cgroups-e.qmd`
- [ ] **cap 100** - Virtualização: KVM, QEMU e o laboratório de estudos - `vol16/cap100-virtualizacao-kvm-qemu-e-o-laboratorio-de.qmd`
- [ ] **cap 101** - Compilação, toolchains e o ecossistema de desenvolvimento - `vol16/cap101-compilacao-toolchains-e-o-ecossistema-de.qmd`
- [ ] **cap 102** - Observabilidade e desempenho: strace, ltrace e perf - `vol16/cap102-observabilidade-e-desempenho-strace-ltrace-e.qmd`
- [ ] **cap 103** - Para onde ir depois: certificações, comunidade e prática contínua - `vol16/cap103-para-onde-ir-depois-certificacoes-comunidade.qmd`

---

**Total:** 103 capitulos em 16 volumes (44 concluidos).

