# Sélectionner le périphérique du modèle

Voici la traduction en français de la documentation du nœud SelectModelDevice :

## Aperçu

Le nœud SelectModelDevice vous permet de choisir manuellement sur quel périphérique (CPU ou GPU spécifique) un modèle de diffusion s'exécute. Il peut déplacer un modèle vers un autre périphérique et gère automatiquement les conflits avec les autres nœuds multi-GPU.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion à placer sur un périphérique spécifique. | MODEL | Oui |  |
| `device` | Le périphérique cible pour le modèle. Les options sont générées dynamiquement en fonction des GPU disponibles. (par défaut : "default") | COMBO | Oui | `"default"`<br>`"cpu"`<br>`"gpu:0"`<br>`"gpu:1"`<br>`"gpu:2"`<br>`"gpu:3"`<br>`"gpu:4"`<br>`"gpu:5"`<br>`"gpu:6"`<br>`"gpu:7"` |

**Détails des paramètres :**
- `"default"` : Restaure le périphérique attribué par le chargeur de modèle, même si un nœud SelectModelDevice précédent l'a modifié.
- `"cpu"` : Verrouille à la fois le périphérique de chargement et de déchargement sur le CPU.
- `"gpu:N"` : Verrouille le périphérique de chargement sur le N-ième GPU disponible (par exemple, `"gpu:0"` pour le premier GPU). Le périphérique de déchargement est restauré au choix d'origine du chargeur.

**Remarques importantes :**
- Si le périphérique demandé n'existe pas sur la machine actuelle (par exemple, un workflow créé sur une machine à 2 GPU est ouvert sur une machine à 1 GPU), le nœud transmettra le modèle sans modification et enregistrera un message au lieu d'échouer.
- Si le modèle se trouve déjà sur le périphérique demandé, le nœud emprunte un chemin rapide et ne recharge pas le modèle.
- Il n'est pas recommandé de placer ce nœud *après* un nœud qui a déjà consommé le modèle (par exemple, un KSampler), car tout état modifié par le nœud précédent sera observé si le périphérique correspond à l'original.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle de diffusion, désormais placé sur le périphérique sélectionné. Si le périphérique était invalide ou indisponible, le modèle est transmis sans modification. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectModelDevice/fr.md)

---
**Source fingerprint (SHA-256):** `02841975f123cc8ae8152ea86f1798e0e7e68255ecd11e04271da886b75eb0fd`
