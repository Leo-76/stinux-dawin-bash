# stinux-dawin-bash

StinuxOS (Debian 12 bookworm) avec la couche bash multiplateforme [linux-dawin-bash](https://github.com/Leo-76/linux-dawin-bash) integree.

## Pourquoi ce depot

Pivot depuis le projet [PureDarwin/XNU](https://github.com/Leo-76/BASH-BUILD-OSX) : le kernel Darwin reste bloque juste apres le handoff EFI->kernel dans QEMU. Plutot que de continuer a deboguer un noyau XNU sur du materiel generique, ce depot repart d'une base Linux qui boote de maniere fiable (StinuxOS Server v5) et y ajoute la couche bash multiplateforme.

## Contenu

- Base : StinuxOS Server v5 (Debian 12 bookworm, kernel 6.1.0-53-amd64, live-build)
- Ajout : `/opt/linux-dawin-bash/` (bash.linux-x86_64, bash.darwin-x86_64, lanceur `bash`)
- Wrapper : `/usr/local/bin/dawin-bash` accessible depuis le PATH

## Important : perimetre reel

Cette couche ne fournit **que bash** (meme source bash 5.3p9, deux binaires : ELF pour Linux, Mach-O pour Darwin/PureDarwin, choisis par un lanceur selon `uname`). Les autres commandes (`sed`, `stat`, `tar`, etc.) restent celles de Debian/GNU-Linux : ce n'est pas une couche de compatibilite complete des commandes macOS.

## Boot teste avec succes (QEMU, TCG, sans KVM)

### Login automatique + MOTD
![Login automatique](captures/01-login-boot.png)

### dawin-bash fonctionnel
![dawin-bash --version](captures/02-dawin-bash-version.png)

Non teste sur materiel reel.

## Commandes macOS/PureDarwin testees sur Stinux

Comparatif avec le tableau de [linux-dawin-bash](https://github.com/Leo-76/linux-dawin-bash) (macOS iMac / PureDarwin minimal) :

| Commande | macOS (iMac) | PureDarwin (minimal) | StinuxOS + dawin-bash |
|---|---|---|---|
| `uname -o` | echoue (BSD) | echoue (BSD) | marche (`GNU/Linux`) |
| `uname -sm` | `Darwin x86_64` | `Darwin x86_64` | `Linux x86_64` |
| `uname -a` / `-s` / `-r` | - | - | marche |
| `readlink -f /tmp` | `/private/tmp` | `/tmp` | `/tmp` |
| `file /bin/ls` | marche (Mach-O) | absent | absent |
| `sed --version` | echoue (BSD) | echoue | marche (`GNU sed 4.9`) |
| `ls --color /tmp` | marche | marche | marche |
| `df -h` | marche | marche | marche |
| `mount` | marche | marche | marche |
| `ls /` | marche | marche | marche |
| `sysctl kern.version` / `hw.*` / `machdep.cpu.*` | marche (BSD sysctl) | marche | absent (`command not found`) |
| `ifconfig` | marche (legacy) | marche | absent (remplace par `ip` sur Debian moderne) |
| `launchctl list` | marche (launchd) | marche | absent (equivalent Linux : `systemctl`) |
| `ps aux` | marche | marche | marche |
| `brew install ...` | marche (natif) | absent | absent |
| `port install ...` | marche (natif) | absent | absent |

A retenir : les commandes POSIX generiques (`uname`, `df`, `ls`, `ps`, `sed` GNU) marchent nativement sur Stinux. Les commandes **specifiques a Darwin/BSD** (`sysctl` syntaxe BSD, `launchctl`, `ifconfig` legacy, `brew`, `port`) n'existent pas sur Linux : `dawin-bash` choisit le bon binaire bash, il ne simule pas le reste de l'environnement Darwin.

![Comparatif uname/readlink/file/sed/ls](captures/03-commandes-comparaison-uname-sed.png)
![uname -a/-s/-r + sysctl absent](captures/04-uname-sysctl.png)
![df -h](captures/05-df-h.png)
![ls / + ifconfig absent](captures/06-ls-ifconfig.png)
![launchctl absent](captures/07-launchctl-absent.png)
![brew/port absents](captures/08-brew-port-absents.png)
![mount + sysctl hw.* absent](captures/09-mount-sysctl-hw.png)

## Outils de developpement

Identique sous le bash systeme Linux et sous `dawin-bash` (meme PATH, `dawin-bash` ne fait que choisir le binaire bash) :

| Outil | Present | Version |
|---|---|---|
| `git` | oui | 2.39.5 |
| `python3` | oui | 3.11.2 |
| `curl` | oui | 7.88.1 (HTTPS/SSL complet) |
| `ssh` | oui | OpenSSH |
| `gcc` | non | absent |
| `make` | non | absent |
| `node` | non | absent |

Bon jeu de base pour scripter/cloner/deployer, mais pas de compilation (`gcc`/`make`) ni Node.js de base : a installer via `apt install build-essential nodejs` si besoin.

![which gcc git python3 make curl node ssh](captures/10-outils-dev-which.png)
![versions git/python3/curl](captures/11-git-python3-curl-versions.png)

## Telechargement

Voir la [release](../../releases/latest) pour l'image ISO complete.

## Verification

```sh
sha256sum -c SHA256SUMS
```
