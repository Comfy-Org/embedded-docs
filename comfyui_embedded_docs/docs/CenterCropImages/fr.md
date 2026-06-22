# Rogner les images au centre

Le nœud Center Crop Images découpe une image à partir de son centre selon une largeur et une hauteur spécifiées. Il calcule la région centrale de l'image d'entrée et extrait une zone rectangulaire aux dimensions définies. Si la taille de découpe demandée est plus grande que l'image, le découpage sera limité aux bords de l'image.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à découper. | IMAGE | Oui | - |
| `largeur` | La largeur de la zone de découpe (par défaut : 512). | INT | Oui | 1 à 8192 |
| `hauteur` | La hauteur de la zone de découpe (par défaut : 512). | INT | Oui | 1 à 8192 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image résultante après l'opération de découpage centré. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CenterCropImages/fr.md)

---
**Source fingerprint (SHA-256):** `4361b6630ab1833e035d6ab04a130fb36fff33cddc36b54ff5a2d8e04534a555`
