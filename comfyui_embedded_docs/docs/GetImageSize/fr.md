Le nœud GetImageSize extrait les dimensions et les informations de lot d'une image d'entrée. Il renvoie la largeur, la hauteur et la taille du lot de l'image tout en affichant ces informations sous forme de texte de progression sur l'interface du nœud. Les données de l'image d'origine sont transmises sans modification.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à partir de laquelle extraire les informations de taille | IMAGE | Oui | - |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `hauteur` | La largeur de l'image d'entrée en pixels | INT |
| `taille du lot` | La hauteur de l'image d'entrée en pixels | INT |
| `batch_size` | Le nombre d'images dans le lot | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetImageSize/fr.md)

---
**Source fingerprint (SHA-256):** `5cd19ae762d2403c6c5d0740cd5f8c17913daea737fddcff8f0d9da2210e82ab`
