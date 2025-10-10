> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVPreprocess/fr.md)

Le nœud LTXVPreprocess applique un prétraitement de compression aux images. Il prend des images en entrée et les traite avec un niveau de compression spécifié, produisant en sortie les images traitées avec les paramètres de compression appliqués.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à traiter |
| `img_compression` | INT | Non | 0-100 | Quantité de compression à appliquer sur l'image (par défaut : 35) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output_image` | IMAGE | L'image de sortie traitée avec la compression appliquée |