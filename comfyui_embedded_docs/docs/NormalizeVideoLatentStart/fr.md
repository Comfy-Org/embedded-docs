> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/fr.md)

Ce nœud ajuste les premières images d'un latent vidéo pour qu'elles ressemblent davantage aux images qui suivent. Il calcule la moyenne et la variation à partir d'un ensemble d'images de référence situées plus loin dans la vidéo et applique ces mêmes caractéristiques aux images de départ. Cela permet de créer une transition visuelle plus fluide et cohérente au début d'une vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `latent` | LATENT | Oui | - | La représentation latente vidéo à traiter. |
| `start_frame_count` | INT | Non | 1 à 16384 | Nombre d'images latentes à normaliser, en comptant depuis le début (par défaut : 4). |
| `reference_frame_count` | INT | Non | 1 à 16384 | Nombre d'images latentes après les images de départ à utiliser comme référence (par défaut : 5). |

**Note :** Le paramètre `reference_frame_count` est automatiquement limité au nombre d'images disponibles après les images de départ. Si le latent vidéo ne contient qu'une seule image, aucune normalisation n'est effectuée et le latent original est renvoyé inchangé.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `latent` | LATENT | Le latent vidéo traité avec les images de départ normalisées. |
