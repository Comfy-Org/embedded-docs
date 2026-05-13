> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/fr.md)

Le nœud EmptyFlux2LatentImage crée une représentation latente vide. Il génère un tenseur rempli de zéros, qui sert de point de départ pour le processus de débruitage du modèle Flux. Les dimensions de l'espace latent sont déterminées par la largeur et la hauteur d'entrée, réduites d'un facteur 16.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `largeur` | INT | Oui | 16 à 8192 | La largeur de l'image finale à générer. La largeur latente sera cette valeur divisée par 16. La valeur par défaut est 1024. |
| `hauteur` | INT | Oui | 16 à 8192 | La hauteur de l'image finale à générer. La hauteur latente sera cette valeur divisée par 16. La valeur par défaut est 1024. |
| `taille_lot` | INT | Non | 1 à 4096 | Le nombre d'échantillons latents à générer en un seul lot. La valeur par défaut est 1. |

**Remarque :** Les entrées `width` et `height` doivent être divisibles par 16, car le nœud les divise en interne par ce facteur pour créer les dimensions latentes.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `samples` | LATENT | Un tenseur latent rempli de zéros. La forme est `[batch_size, 128, height // 16, width // 16]`. |

---
**Source fingerprint (SHA-256):** `e3616ad0e283a318bbe441d84f687883e59ab311e72c5e5edd16ddabde10988e`
