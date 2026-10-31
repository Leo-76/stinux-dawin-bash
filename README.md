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

## Telechargement

Voir la [release](../../releases/latest) pour l'image ISO complete.

## Verification

```sh
sha256sum -c SHA256SUMS
```
