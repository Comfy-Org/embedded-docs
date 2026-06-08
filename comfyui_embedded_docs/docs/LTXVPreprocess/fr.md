Le nœud LTXVPreprocess applique un prétraitement de compression aux images. Il prend des images en entrée et les traite avec un niveau de compression spécifié, produisant les images traitées avec les paramètres de compression appliqués.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à traiter | IMAGE | Oui | - |
| `compression_d'image` | Niveau de compression à appliquer sur l'image (par défaut : 35) | INT | Non | 0-100 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output_image` | L'image de sortie traitée avec la compression appliquée | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVPreprocess/fr.md)

---
**Source fingerprint (SHA-256):** `2c5fbde5d011bdf3313ca05508f58a13eaae0bdff12f3659fef281c0045e480d`
