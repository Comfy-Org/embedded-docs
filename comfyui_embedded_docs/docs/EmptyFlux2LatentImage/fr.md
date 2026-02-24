> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/fr.md)

Le nœud EmptyFlux2LatentImage crée une représentation latente vide et vierge. Il génère un tenseur rempli de zéros, qui sert de point de départ pour le processus de débruitage du modèle Flux. Les dimensions du latent sont déterminées par la largeur et la hauteur en entrée, réduites d'un facteur 16.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Oui | 16 à 8192 | La largeur de l'image finale à générer. La largeur du latent sera cette valeur divisée par 16. La valeur par défaut est 1024. |
| `height` | INT | Oui | 16 à 8192 | La hauteur de l'image finale à générer. La hauteur du latent sera cette valeur divisée par 16. La valeur par défaut est 1024. |
| `batch_size` | INT | Non | 1 à 4096 | Le nombre d'échantillons latents à générer en un seul lot. La valeur par défaut est 1. |

**Note :** Les entrées `width` et `height` doivent être divisibles par 16, car le nœud les divise en interne par ce facteur pour créer les dimensions du latent.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `samples` | LATENT | Un tenseur latent rempli de zéros. La forme est `[batch_size, 128, height // 16, width // 16]`. |
