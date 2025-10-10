> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVirtualTryOnNode/fr.md)

Kling Virtual Try On Node. Saisissez une image humaine et une image de vêtement pour essayer le vêtement sur la personne. Vous pouvez fusionner plusieurs images d'articles vestimentaires en une seule image avec un fond blanc.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `human_image` | IMAGE | Oui | - | L'image humaine sur laquelle essayer les vêtements |
| `cloth_image` | IMAGE | Oui | - | L'image du vêtement à essayer sur la personne |
| `model_name` | STRING | Oui | `"kolors-virtual-try-on-v1"` | Le modèle d'essayage virtuel à utiliser (par défaut : "kolors-virtual-try-on-v1") |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | IMAGE | L'image résultante montrant la personne avec l'article vestimentaire essayé |