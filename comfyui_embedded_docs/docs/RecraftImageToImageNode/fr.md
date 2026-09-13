# Recraft Image vers Image

Ce nœud modifie une image existante en fonction d'un prompt textuel et d'un réglage de force. Il envoie l'image à l'API Recraft V3 et renvoie une nouvelle image qui suit le prompt tout en restant plus ou moins similaire à l'originale, selon la valeur de force.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à modifier. Lorsqu'un lot d'images est fourni, chaque image est traitée individuellement. | IMAGE | Oui | - |
| `prompt` | Prompt pour la génération d'image. Valeur par défaut : chaîne vide. Longueur maximale : 1000 caractères. | STRING | Oui | - |
| `n` | Le nombre d'images à générer. Valeur par défaut : 1. | INT | Oui | 1-6 |
| `strength` | Définit la différence avec l'image originale ; doit se situer dans [0, 1], où 0 signifie presque identique et 1 signifie une similarité très faible. Valeur par défaut : 0.5. | FLOAT | Oui | 0.0-1.0 (pas de 0.01) |
| `seed` | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine. Valeur par défaut : 0. | INT | Oui | 0-18446744073709551615 |
| `recraft_style` | Sélection de style optionnelle pour la génération d'image. Si elle n'est pas fournie, la valeur par défaut est `realistic_image`. | STYLEV3 | Non | - |
| `negative_prompt` | Description textuelle optionnelle des éléments indésirables sur une image. Valeur par défaut : chaîne vide. Fournie en tant que socket d'entrée. | STRING | Non | - |
| `recraft_controls` | Contrôles supplémentaires optionnels sur la génération via le nœud Recraft Controls. | CONTROLS | Non | - |

**Remarque :** Le paramètre `seed` déclenche uniquement la réexécution du nœud mais ne garantit pas des résultats déterministes. Le paramètre `strength` est arrondi à 2 décimales en interne. Le `prompt` est validé et ne doit pas dépasser 1000 caractères. Un `negative_prompt` vide est traité comme l'absence de prompt négatif. Si `recraft_style` n'est pas fourni, le nœud utilise par défaut le style `realistic_image`. Si vous utilisez un `style_id` de la bibliothèque Infinite Style Library, assurez-vous qu'il ne s'agit pas d'un style Vector art, car cela peut entraîner la réception de données SVG au lieu d'une image par le nœud, provoquant une erreur. Lorsque l'`image` d'entrée est un lot, chaque image du lot est traitée individuellement et tous les résultats sont renvoyés ensemble.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | La ou les images générées à partir de l'image d'entrée, du prompt et de la force. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `1932e55d1dc392e6bd42a0bd29f5aaba44b65997b597648a927fba38a27c90ad`
