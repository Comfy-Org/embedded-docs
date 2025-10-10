> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProUltraImageNode/fr.md)

Génère des images en utilisant Flux Pro 1.1 Ultra via une API basée sur un prompt et une résolution. Ce nœud se connecte à un service externe pour créer des images selon votre description textuelle et les dimensions spécifiées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Prompt pour la génération d'image (par défaut : chaîne vide) |
| `prompt_upsampling` | BOOLEAN | Non | - | Indique s'il faut effectuer un suréchantillonnage sur le prompt. S'il est actif, modifie automatiquement le prompt pour une génération plus créative, mais les résultats sont non déterministes (la même graîne ne produira pas exactement le même résultat). (par défaut : Faux) |
| `seed` | INT | Non | 0 à 18446744073709551615 | La graîne aléatoire utilisée pour créer le bruit. (par défaut : 0) |
| `aspect_ratio` | STRING | Non | - | Ratio d'aspect de l'image ; doit être compris entre 1:4 et 4:1. (par défaut : "16:9") |
| `raw` | BOOLEAN | Non | - | Lorsque True, génère des images moins traitées et d'apparence plus naturelle. (par défaut : Faux) |
| `image_prompt` | IMAGE | Non | - | Image de référence optionnelle pour guider la génération |
| `image_prompt_strength` | FLOAT | Non | 0.0 à 1.0 | Mélange entre le prompt et le prompt d'image. (par défaut : 0.1) |

**Note :** Le paramètre `aspect_ratio` doit être compris entre 1:4 et 4:1. Lorsque `image_prompt` est fourni, `image_prompt_strength` devient actif et contrôle l'influence de l'image de référence sur le résultat final.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output_image` | IMAGE | L'image générée par Flux Pro 1.1 Ultra |