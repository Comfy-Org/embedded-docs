# Sélectionner le périphérique du modèle

## Vue d'ensemble

Le nœud SelectModelDevice vous permet de choisir manuellement sur quel périphérique (CPU ou un GPU spécifique) un modèle de diffusion s’exécute. Il peut déplacer un modèle vers un autre périphérique et gère automatiquement les conflits avec les autres nœuds multi-GPU.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion à placer sur un périphérique spécifique. | MODEL | Oui |  |
| `device` | Le périphérique cible pour le modèle. Les options sont générées dynamiquement en fonction des GPU disponibles. (par défaut : `"default"`) | COMBO | Oui | `"default"`<br>`"cpu"`<br>`"gpu:0"`<br>`"gpu:1"`<br>... (une entrée `"gpu:N"` par GPU détecté) |

**Détails des paramètres :**
- `"default"` : Rétablit le périphérique assigné par le chargeur de modèle, même si un précédent nœud SelectModelDevice l’a modifié.
- `"cpu"` : Fixe à la fois le périphérique de chargement et celui de déchargement sur le CPU.
- `"gpu:N"` : Fixe le périphérique de chargement sur le N-ième GPU disponible (par ex. `"gpu:0"` pour le premier GPU). Le périphérique de déchargement est restauré au choix d’origine du chargeur.

**Remarques importantes :**
- Si le périphérique demandé n’existe pas sur la machine actuelle (par ex. un workflow créé sur une machine à 2 GPU est ouvert sur une machine à 1 GPU), le nœud transmet le modèle tel quel et consigne un message au lieu d’échouer.
- Si le modèle se trouve déjà sur le périphérique demandé, le nœud emprunte un chemin rapide et ne recharge pas le modèle.
- Si le chargeur de modèle ne prend pas en charge le multi-GPU (aucune fabrique de rechargement), le nœud transmet le modèle tel quel et consigne un avertissement.
- Lorsqu’un clone MultiGPU CFG Split occupe déjà le périphérique sélectionné, ce clone est supprimé afin que deux modèles ne soient pas liés au même périphérique.
- Lorsqu’un périphérique spécifique est sélectionné, le nœud ajuste également le dtype de calcul du modèle vers un dtype pris en charge par ce périphérique.
- Il n’est pas recommandé de placer ce nœud *après* un nœud qui a déjà consommé le modèle (par ex. un KSampler), car tout état modifié par le nœud précédent sera observé si le périphérique correspond à celui d’origine.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle de diffusion, désormais placé sur le périphérique sélectionné. Si le périphérique est invalide ou indisponible, le modèle est transmis tel quel. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectModelDevice/fr.md)

---
**Source fingerprint (SHA-256):** `d02a8bd9612861cf696f03969fe693088351de5a72ccbd4c1aed405b104eb71e`
