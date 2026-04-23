> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingAvatarNode/fr.md)

Le nœud Kling Avatar 2.0 génère des vidéos d'humains numériques de style diffusion. Il utilise une seule photo de référence et un fichier audio pour créer une vidéo d'avatar parlant. Une invite de texte optionnelle peut être utilisée pour définir les actions, les émotions et les mouvements de caméra de l'avatar.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | Image de référence pour l'avatar. La largeur et la hauteur doivent être d'au moins 300px. Le rapport d'aspect doit être compris entre 1:2,5 et 2,5:1. |
| `sound_file` | AUDIO | Oui | - | Entrée audio. La durée doit être comprise entre 2 et 300 secondes. |
| `mode` | COMBO | Oui | `"std"`<br>`"pro"` | Le mode de génération à utiliser. |
| `prompt` | STRING | Non | - | Invite optionnelle pour définir les actions, les émotions et les mouvements de caméra de l'avatar. (par défaut : chaîne vide) |
| `seed` | INT | Oui | 0 à 2147483647 | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. (par défaut : 0) |

**Note :** Les entrées `image` et `sound_file` ont des exigences de validation spécifiques. L'image doit faire au moins 300x300 pixels avec un rapport d'aspect compris entre 1:2,5 et 2,5:1. Le fichier audio doit avoir une durée comprise entre 2 et 300 secondes.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo de l'humain numérique générée. |