> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/fr.md)

Le nœud Empty Qwen Image Layered Latent crée une représentation latente vierge et multicouche destinée à être utilisée avec les modèles d'image Qwen. Il génère un tenseur rempli de zéros, structuré avec un nombre spécifié de couches, une taille de lot et des dimensions spatiales. Ce latent vide sert de point de départ pour des workflows ultérieurs de génération ou de manipulation d'image.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Oui | 16 à MAX_RESOLUTION | La largeur de l'image latente à créer. La valeur doit être divisible par 16. (par défaut : 640) |
| `height` | INT | Oui | 16 à MAX_RESOLUTION | La hauteur de l'image latente à créer. La valeur doit être divisible par 16. (par défaut : 640) |
| `layers` | INT | Oui | 0 à MAX_RESOLUTION | Le nombre de couches supplémentaires à ajouter à la structure latente. Cela définit la profondeur de la représentation latente. (par défaut : 3) |
| `batch_size` | INT | Non | 1 à 4096 | Le nombre d'échantillons latents à générer dans un lot. (par défaut : 1) |

**Note :** Les paramètres `width` et `height` sont divisés par 8 en interne pour déterminer les dimensions spatiales du tenseur latent de sortie.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `samples` | LATENT | Un tenseur latent rempli de zéros. Sa forme est `[batch_size, 16, layers + 1, height // 8, width // 8]`. |
