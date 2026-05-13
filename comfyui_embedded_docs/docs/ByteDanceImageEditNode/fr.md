> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/fr.md)

Le nœud ByteDance Image Edit vous permet de modifier des images à l'aide des modèles d'IA de ByteDance via une API. Vous fournissez une image d'entrée et une instruction textuelle décrivant les modifications souhaitées, puis le nœud traite l'image conformément à vos instructions. Le nœud gère automatiquement la communication avec l'API et renvoie l'image modifiée.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------------|---------------|--------|-------|-------------|
| `model` | MODEL | COMBO | seededit_3 | Options Image2ImageModelName | Nom du modèle |
| `image` | IMAGE | IMAGE | - | - | L'image de base à modifier |
| `prompt` | STRING | STRING | "" | - | Instruction pour modifier l'image |
| `seed` | INT | INT | 0 | 0-2147483647 | Graine à utiliser pour la génération |
| `guidance_scale` | FLOAT | FLOAT | 5,5 | 1,0-10,0 | Une valeur plus élevée fait que l'image suit plus fidèlement l'instruction |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Indique s'il faut ajouter un filigrane "Généré par IA" à l'image |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `IMAGE` | IMAGE | L'image modifiée renvoyée par l'API ByteDance |

---
**Source fingerprint (SHA-256):** `9dc13d89f84756b545120efb5535e08ada163d4534975809f5056bdf7d8bfb73`
