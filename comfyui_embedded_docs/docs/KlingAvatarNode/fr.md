# Kling Avatar 2.0

Voici la traduction en français de la documentation du nœud Kling Avatar 2.0, conformément à vos règles :

Ce nœud Kling Avatar 2.0 génère des vidéos d'humains numériques de type diffusion à partir d'une seule photo de référence et d'un fichier audio. Il crée une vidéo d'avatar parlant avec une invite textuelle facultative pour définir les actions, les émotions et les mouvements de caméra de l'avatar.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | Image de référence de l'avatar. La largeur et la hauteur doivent être d'au moins 300 px. Le rapport hauteur/largeur doit être compris entre 1:2,5 et 2,5:1. | IMAGE | Oui | - |
| `sound_file` | Entrée audio. La durée doit être comprise entre 2 et 300 secondes. | AUDIO | Oui | - |
| `mode` | Le mode de génération à utiliser. | COMBO | Oui | `"std"`<br>`"pro"` |
| `prompt` | Invite facultative pour définir les actions, les émotions et les mouvements de caméra de l'avatar. (par défaut : chaîne vide) | STRING | Non | - |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes, quelle que soit la graine. (par défaut : 0) | INT | Oui | 0 à 2147483647 |

**Remarque :** Les entrées `image` et `sound_file` ont des exigences de validation spécifiques. L'image doit faire au moins 300x300 pixels avec un rapport hauteur/largeur compris entre 1:2,5 et 2,5:1. Le fichier audio doit avoir une durée comprise entre 2 et 300 secondes.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo d'humain numérique générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingAvatarNode/fr.md)

---
**Source fingerprint (SHA-256):** `85793d3820a89ef98bb54cb930486847d4fd64cce5470ba34574ec319f8ea8c6`
