> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimVideoLatent/fr.md)

Le nœud TrimVideoLatent supprime des images au début d'une représentation latente vidéo. Il prend un échantillon vidéo latent et supprime un nombre spécifié d'images depuis le début, renvoyant la portion restante de la vidéo. Cela vous permet de raccourcir les séquences vidéo en supprimant les images initiales.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `échantillons` | LATENT | Oui | - | La représentation vidéo latente d'entrée contenant les images vidéo à tronquer |
| `quantité de découpe` | INT | Non | 0 à 99999 | Le nombre d'images à supprimer du début de la vidéo (par défaut : 0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | LATENT | La représentation vidéo latente tronquée avec le nombre spécifié d'images supprimées depuis le début |