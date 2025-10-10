> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToMaxDimension/fr.md)

Le nœud ImageScaleToMaxDimension redimensionne les images pour qu'elles s'adaptent à une dimension maximale spécifiée tout en conservant le ratio d'aspect original. Il détermine si l'image est en orientation portrait ou paysage, puis met à l'échelle la plus grande dimension pour correspondre à la taille cible tout en ajustant proportionnellement la plus petite dimension. Le nœud prend en charge plusieurs méthodes de suréchantillonnage pour répondre à différents besoins de qualité et de performance.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à redimensionner |
| `upscale_method` | STRING | Oui | "area"<br>"lanczos"<br>"bilinear"<br>"nearest-exact"<br>"bicubic" | La méthode d'interpolation utilisée pour le redimensionnement de l'image |
| `largest_size` | INT | Oui | 0 à 16384 | La dimension maximale pour l'image redimensionnée (par défaut : 512) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image redimensionnée dont la plus grande dimension correspond à la taille spécifiée |