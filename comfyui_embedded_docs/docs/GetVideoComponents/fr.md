> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/fr.md)

Le nœud Get Video Components extrait tous les éléments principaux d'un fichier vidéo. Il sépare la vidéo en images individuelles, extrait la piste audio et fournit les informations de fréquence d'images de la vidéo. Cela vous permet de travailler avec chaque composant indépendamment pour un traitement ou une analyse ultérieure.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `vidéo` | VIDEO | Oui | - | La vidéo depuis laquelle extraire les composants. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `audio` | IMAGE | Les images individuelles extraites de la vidéo sous forme d'images séparées. |
| `ips` | AUDIO | La piste audio extraite de la vidéo. |
| `fps` | FLOAT | La fréquence d'images de la vidéo en images par seconde. |
