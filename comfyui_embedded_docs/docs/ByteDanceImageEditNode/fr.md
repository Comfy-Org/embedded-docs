> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/fr.md)

Le nœud ByteDance Image Edit vous permet de modifier des images en utilisant les modèles d'IA de ByteDance via une API. Vous fournissez une image d'entrée et une instruction textuelle décrivant les modifications souhaitées, et le nœud traite l'image selon vos instructions. Le nœud gère automatiquement la communication avec l'API et renvoie l'image modifiée.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seededit_3 | Options Image2ImageModelName | Nom du modèle |
| `image` | IMAGE | IMAGE | - | - | L'image de base à modifier |
| `prompt` | STRING | STRING | "" | - | Instruction pour modifier l'image |
| `seed` | INT | INT | 0 | 0-2147483647 | Graine à utiliser pour la génération |
| `guidance_scale` | FLOAT | FLOAT | 5.5 | 1.0-10.0 | Une valeur plus élevée fait que l'image suit plus fidèlement l'instruction |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Indique s'il faut ajouter un filigrane "Généré par IA" sur l'image |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | L'image modifiée renvoyée par l'API ByteDance |
