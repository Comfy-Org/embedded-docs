# ByteDanceImageEditNode

Le nœud ByteDance Image Edit vous permet de modifier des images à l'aide des modèles d'IA de ByteDance via une API. Vous fournissez une image d'entrée et une instruction textuelle décrivant les modifications souhaitées, puis le nœud traite l'image conformément à vos instructions. Le nœud gère automatiquement la communication avec l'API et renvoie l'image modifiée.

## Entrées

| Paramètre | Description | Type de données | Type d'entrée | Défaut | Plage |
| --- | --- | --- | --- | --- | --- |
| `model` | Nom du modèle | MODEL | COMBO | seededit_3 | Options Image2ImageModelName |
| `image` | L'image de base à modifier | IMAGE | IMAGE | - | - |
| `prompt` | Instruction pour modifier l'image | STRING | STRING | "" | - |
| `seed` | Graine à utiliser pour la génération | INT | INT | 0 | 0-2147483647 |
| `guidance_scale` | Une valeur plus élevée fait que l'image suit plus fidèlement l'instruction | FLOAT | FLOAT | 5,5 | 1,0-10,0 |
| `watermark` | Indique s'il faut ajouter un filigrane "Généré par IA" à l'image | BOOLEAN | BOOLEAN | True | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | L'image modifiée renvoyée par l'API ByteDance | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/fr.md)

---
**Source fingerprint (SHA-256):** `9dc13d89f84756b545120efb5535e08ada163d4534975809f5056bdf7d8bfb73`
