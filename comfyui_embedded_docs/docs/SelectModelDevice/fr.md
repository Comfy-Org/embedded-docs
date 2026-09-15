# Sélectionner le périphérique du modèle

Le nœud Select Model Device vous permet de choisir manuellement le périphérique (CPU ou un GPU spécifique) sur lequel un modèle de diffusion s'exécute. Il peut déplacer un modèle vers un autre périphérique et gère automatiquement les conflits avec d'autres nœuds multi-GPU. Sélectionner `"default"` restaure le périphérique d'origine choisi par le chargeur de modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion à placer sur un périphérique spécifique. | MODEL | Oui |  |
| `device` | Le périphérique cible pour le modèle. Les options sont générées dynamiquement en fonction des périphériques disponibles sur la machine actuelle. (par défaut : `"default"`) | COMBO | Oui | `"default"`<br>`"cpu"`<br>`"gpu:0"`<br>`"gpu:1"`<br>... (une entrée `"gpu:N"` par GPU détecté) |

**Détails des paramètres :**
- `"default"` : Restaure les périphériques de chargement et de déchargement attribués par le chargeur de modèle, même après un précédent appel à Select Model Device.
- `"cpu"` : Fixe à la fois le périphérique de chargement et le périphérique de déchargement sur CPU.
- `"gpu:N"` : Fixe le périphérique de chargement sur le N-ième GPU disponible (par exemple, `"gpu:0"` pour le premier GPU). Le périphérique de déchargement est restauré sur le choix d'origine du chargeur.

**Remarques importantes :**
- Si le périphérique demandé n'existe pas sur la machine actuelle (par exemple, un workflow créé sur une machine à 2 GPU est ouvert sur une machine à 1 GPU), le nœud transmet le modèle inchangé et journalise un message au lieu d'échouer. Les valeurs `gpu:N` inconnues sont autorisées lors de la validation des entrées afin que les workflows portables ne produisent pas d'erreur trop tôt.
- Si le modèle se trouve déjà sur le périphérique demandé, le nœud utilise un chemin rapide et ne recharge pas le modèle.
- Lorsque le périphérique demandé diffère de celui sur lequel se trouve déjà le modèle d'entrée, un nouveau modèle est généré à l'aide de la fabrique de rechargement du chargeur afin que le nouveau patcher possède des poids indépendants sur le nouveau périphérique.
- Si le chargeur de modèle ne prend pas en charge le multi-GPU (aucune fabrique de rechargement), le nœud transmet le modèle inchangé et journalise un avertissement.
- Lorsqu'un clone MultiGPU CFG Split occupe déjà le périphérique sélectionné, ce clone est élagué afin que deux modèles ne soient pas liés au même périphérique.
- Lorsqu'un périphérique non par défaut est sélectionné (CPU ou GPU), le nœud ajuste également le dtype de calcul du modèle vers un dtype pris en charge par ce périphérique.
- Placer ce nœud après un nœud qui a déjà consommé le modèle (par exemple, un KSampler) n'est pas recommandé, car tout état modifié par le nœud précédent sera observé si le périphérique correspond à celui d'origine.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle de diffusion, désormais placé sur le périphérique sélectionné. Si le périphérique était invalide ou indisponible, le modèle est transmis inchangé. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectModelDevice/fr.md)

---
**Source fingerprint (SHA-256):** `d02a8bd9612861cf696f03969fe693088351de5a72ccbd4c1aed405b104eb71e`
