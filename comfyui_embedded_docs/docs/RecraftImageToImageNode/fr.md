> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/fr.md)

Ce nœud modifie une image existante en fonction d'une invite textuelle et d'un paramètre de force. Il utilise l'API Recraft pour transformer l'image d'entrée selon la description fournie tout en maintenant une certaine similarité avec l'image originale en fonction du paramètre de force.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à modifier |
| `prompt` | STRING | Oui | - | L'invite pour la génération d'image (par défaut : "") |
| `n` | INT | Oui | 1-6 | Le nombre d'images à générer (par défaut : 1) |
| `strength` | FLOAT | Oui | 0.0-1.0 | Définit la différence avec l'image originale, doit être comprise dans [0, 1], où 0 signifie presque identique et 1 signifie une similarité misérable (par défaut : 0.5) |
| `seed` | INT | Oui | 0-18446744073709551615 | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0) |
| `recraft_style` | STYLEV3 | Non | - | Sélection de style optionnelle pour la génération d'image |
| `negative_prompt` | STRING | Non | - | Une description textuelle optionnelle des éléments indésirables sur une image (par défaut : "") |
| `recraft_controls` | CONTROLS | Non | - | Contrôles additionnels optionnels sur la génération via le nœud Contrôles Recraft |

**Note :** Le paramètre `seed` déclenche uniquement la réexécution du nœud mais ne garantit pas des résultats déterministes. Le paramètre de force est arrondi à 2 décimales en interne.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image ou les images générées basées sur l'image d'entrée et l'invite |