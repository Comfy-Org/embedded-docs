> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/fr.md)

Ce nœud modifie des images en fonction d'une instruction textuelle et d'un masque. Il utilise l'API Recraft pour éditer intelligemment des zones spécifiques d'une image que vous définissez avec un masque, tout en laissant le reste de l'image inchangé.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à modifier |
| `mask` | MASK | Oui | - | Le masque définissant les zones de l'image qui doivent être modifiées |
| `prompt` | STRING | Oui | - | Instruction pour la génération d'image (par défaut : chaîne vide) |
| `n` | INT | Oui | 1-6 | Le nombre d'images à générer (par défaut : 1, minimum : 1, maximum : 6) |
| `seed` | INT | Oui | 0-18446744073709551615 | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0, minimum : 0, maximum : 18446744073709551615) |
| `recraft_style` | STYLEV3 | Non | - | Paramètre de style optionnel pour l'API Recraft |
| `negative_prompt` | STRING | Non | - | Une description textuelle optionnelle des éléments indésirables sur une image (par défaut : chaîne vide) |

*Note : L'`image` et le `mask` doivent être fournis ensemble pour que l'opération d'inpainting fonctionne. Le masque sera automatiquement redimensionné pour correspondre aux dimensions de l'image.*

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image ou les images modifiées générées en fonction de l'instruction et du masque |