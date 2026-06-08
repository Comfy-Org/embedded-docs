Le nœud ImageScaleToMaxDimension redimensionne les images pour qu'elles s'adaptent à une dimension maximale spécifiée tout en conservant le rapport hauteur/largeur d'origine. Il détermine si l'image est orientée portrait ou paysage, puis met à l'échelle la plus grande dimension pour qu'elle corresponde à la taille cible tout en ajustant proportionnellement la plus petite dimension. Le nœud prend en charge plusieurs méthodes de mise à l'échelle pour différents besoins de qualité et de performance.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à redimensionner | IMAGE | Oui | - |
| `méthode_d'agrandissement` | La méthode d'interpolation utilisée pour redimensionner l'image (par défaut : "area") | STRING | Oui | "area"<br>"lanczos"<br>"bilinear"<br>"nearest-exact"<br>"bilinear"<br>"bicubic" |
| `taille_maximale` | La dimension maximale pour l'image redimensionnée (par défaut : 512) | INT | Oui | 0 à 16384 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image redimensionnée dont la plus grande dimension correspond à la taille spécifiée | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToMaxDimension/fr.md)

---
**Source fingerprint (SHA-256):** `be113c1a98ab9d884b2c728b790c41fb236857d59af567e43e2be0ef0362cc5e`
