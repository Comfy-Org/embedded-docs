> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageToVideoNode/fr.md)

Génère des vidéos de manière synchrone en fonction de l'invite, des images d'entrée et de la taille de sortie. Ce nœud crée des vidéos en utilisant l'API Luma en fournissant des invites textuelles et des images de début/fin optionnelles pour définir le contenu et la structure de la vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Invite pour la génération de la vidéo (par défaut : "") |
| `modèle` | COMBO | Oui | Plusieurs options disponibles | Sélectionne le modèle de génération vidéo parmi les modèles Luma disponibles |
| `résolution` | COMBO | Oui | Plusieurs options disponibles | Résolution de sortie pour la vidéo générée (par défaut : 540p) |
| `durée` | COMBO | Oui | Plusieurs options disponibles | Durée de la vidéo générée |
| `boucle` | BOOLEAN | Oui | - | Détermine si la vidéo générée doit être en boucle (par défaut : False) |
| `seed` | INT | Oui | 0 à 18446744073709551615 | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine. (par défaut : 0) |
| `première_image` | IMAGE | Non | - | Première image de la vidéo générée. (optionnel) |
| `dernière_image` | IMAGE | Non | - | Dernière image de la vidéo générée. (optionnel) |
| `luma_concepts` | CUSTOM | Non | - | Concepts de caméra optionnels pour dicter le mouvement de la caméra via le nœud Luma Concepts. (optionnel) |

**Note :** Au moins l'un des paramètres `first_image` ou `last_image` doit être fourni. Le nœud générera une exception si les deux sont manquants.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré |
