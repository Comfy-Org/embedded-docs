# Recraft Image vers Image

Ce nœud modifie une image existante en fonction d’un prompt texte et d’un paramètre de force. Il utilise l’API Recraft pour transformer l’image d’entrée selon la description fournie tout en conservant une certaine similarité avec l’image originale en fonction du réglage de force.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L’image d’entrée à modifier | IMAGE | Oui | - |
| `prompt` | Prompt pour la génération d’image (par défaut : "", longueur maximale : 1000 caractères) | STRING | Oui | - |
| `n` | Le nombre d’images à générer (par défaut : 1) | INT | Oui | 1-6 |
| `strength` | Définit la différence avec l’image originale ; doit se situer dans [0, 1], où 0 signifie presque identique et 1 signifie une similarité très faible (par défaut : 0,5) | FLOAT | Oui | 0.0-1.0 |
| `seed` | Graine pour déterminer si le nœud doit se réexécuter ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0) | INT | Oui | 0-18446744073709551615 |
| `recraft_style` | Sélection facultative du style pour la génération d’images. Si non fournie, la valeur par défaut est `realistic_image` | STYLEV3 | Non | - |
| `negative_prompt` | Description textuelle facultative des éléments indésirables sur une image (par défaut : "") | STRING | Non | - |
| `recraft_controls` | Contrôles supplémentaires facultatifs sur la génération via le nœud Recraft Controls | CONTROLS | Non | - |

**Remarque :** Le paramètre `seed` déclenche uniquement la ré-exécution du nœud mais ne garantit pas des résultats déterministes. Le paramètre de force est arrondi à 2 décimales en interne. Le prompt est validé et ne doit pas dépasser 1000 caractères. Si `recraft_style` n’est pas fourni, le nœud utilise par défaut le style `realistic_image`. Si vous utilisez un `style_id` provenant de la Infinite Style Library, assurez-vous qu’il ne s’agit pas d’un style d’art vectoriel, car cela pourrait amener le nœud à recevoir des données SVG au lieu d’une image, entraînant une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | Les images générées à partir de l’image d’entrée et du prompt. Pour chaque image d’entrée, `n` images sont générées, donc le nombre total de sorties est égal au nombre d’entrées multiplié par `n`. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `1932e55d1dc392e6bd42a0bd29f5aaba44b65997b597648a927fba38a27c90ad`
