# Captures de test

Tests de bash 3.2.48 (sources Darwin 10) dans PureDarwin 17.4 sous QEMU.

- `02-puredarwin-bash-version.png` : version de bash dans PureDarwin (capture de la VM).
- `03-puredarwin-commandes.png` : résultats de commandes courantes (capture de la VM).
- `01-sources-darwin10-rendu-texte.png` : liste des sources, image générée à partir d'un texte (pas une capture d'écran).

Limites : le noyau reste Darwin 17.4, pas un vrai Darwin 10. Seul bash est remplacé ; les autres outils sont BSD.

## Autres captures (toutes issues de VM, via le moniteur QEMU ou le bureau de test)

- `vm-p1` à `vm-p3` : bureau de test (XFCE).
- `vm-pd1` à `vm-pd4` : essais de démarrage (chargeur, blocages).
- `vm-pe1` à `vm-pe7` : démarrage de PureDarwin 17.4, console bash, transfert et vérification du binaire.
