# Recraft Image vers Image

Ce nœud modifie une image existante en fonction d'un prompt textuel et d'un paramètre de force. Il utilise l'API Recraft pour transformer l'image d'entrée selon la description fournie, tout en conservant une certaine similarité avec l'image originale en fonction du réglage de force.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à modifier | IMAGE | Oui | - |
| `invite` | Prompt pour la génération d'image (par défaut : "", longueur maximale : 1000 caractères) | STRING | Oui | - |
| `n` | Le nombre d'images à générer (par défaut : 1) | INT | Oui | 1-6 |
| `intensité` | Définit la différence avec l'image originale, doit se situer dans [0, 1], où 0 signifie presque identique et 1 signifie une similarité très faible (par défaut : 0.5) | FLOAT | Oui | 0.0-1.0 |
| `graine` | Graine pour déterminer si le nœud doit se réexécuter ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0) | INT | Oui | 0-18446744073709551615 |
| `recraft_style` | Sélection facultative du style pour la génération d'image. Si non fourni, la valeur par défaut est `realistic_image` | STYLEV3 | Non | - |
| `invite_négative` | Une description textuelle facultative des éléments indésirables sur une image (par défaut : "") | STRING | Non | - |
| `recraft_controls` | Contrôles supplémentaires facultatifs sur la génération via le nœud Contrôles Recraft | CONTROLS | Non | - |

**Remarque :** Le paramètre `seed` déclenche uniquement la réexécution du nœud mais ne garantit pas des résultats déterministes. Le paramètre de force est arrondi à 2 décimales en interne. Le prompt est validé et ne doit pas dépasser 1000 caractères. Si `recraft_style` n'est pas fourni, le nœud utilise par défaut le style `realistic_image`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | La ou les images générées à partir de l'image d'entrée et du prompt | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `e47ab70e77186e62c253c976cdd7942cfb949ba6461914d2b4341f3eca8e14aa`
