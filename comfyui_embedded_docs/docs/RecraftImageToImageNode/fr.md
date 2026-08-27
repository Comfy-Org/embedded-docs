# Recraft Image vers Image

Ce nœud modifie une image existante à partir d’un prompt textuel et d’un paramètre de force. Il utilise l’API Recraft V3 pour transformer l’image d’entrée selon la description fournie, tout en conservant une certaine similarité avec l’image d’origine, contrôlée par le paramètre `strength`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L’image d’entrée à modifier | IMAGE | Oui | - |
| `invite` | Prompt pour la génération d’image (par défaut : chaîne vide, longueur maximale : 1000 caractères) | STRING | Oui | - |
| `n` | Le nombre d’images à générer (par défaut : 1) | INT | Oui | 1-6 |
| `intensité` | Définit la différence avec l’image d’origine ; doit se situer dans [0, 1], où 0 signifie presque identique et 1 signifie une similarité très faible (par défaut : 0,5) | FLOAT | Oui | 0.0-1.0 |
| `graine` | Seed pour déterminer si le nœud doit s’exécuter à nouveau ; les résultats réels sont non déterministes quel que soit le seed (par défaut : 0) | INT | Oui | 0-18446744073709551615 |
| `recraft_style` | Sélection facultative du style pour la génération d’image. Si elle n’est pas fournie, le style par défaut est `realistic_image` | STYLEV3 | Non | - |
| `invite_négative` | Description textuelle facultative des éléments indésirables sur une image (par défaut : chaîne vide) | STRING | Non | - |
| `recraft_controls` | Contrôles supplémentaires facultatifs sur la génération via le nœud Recraft Controls | CONTROLS | Non | - |

**Remarque :** Le paramètre `seed` ne déclenche que la ré-exécution du nœud, mais ne garantit pas des résultats déterministes. Le paramètre `strength` est arrondi à 2 décimales en interne. Le `prompt` est validé et ne doit pas dépasser 1000 caractères. Un `negative_prompt` vide est traité comme une absence de prompt négatif. Si `recraft_style` n’est pas fourni, le nœud utilise par défaut le style `realistic_image`. Si vous utilisez un `style_id` provenant de l’Infinite Style Library, assurez-vous qu’il ne s’agit pas d’un style Vector art, car cela pourrait amener le nœud à recevoir des données SVG au lieu d’une image, ce qui entraînerait une erreur. Lorsque l’image d’entrée `image` est un lot, chaque image du lot est traitée individuellement et tous les résultats sont renvoyés ensemble.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | Image(s) générée(s) à partir de l’image d’entrée et du prompt | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `1932e55d1dc392e6bd42a0bd29f5aaba44b65997b597648a927fba38a27c90ad`
