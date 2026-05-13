> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToImageNode/fr.md)

Génère des images de manière synchrone en fonction d'un prompt et d'une résolution. Ce nœud se connecte à l'API Recraft pour créer des images à partir de descriptions textuelles avec des dimensions spécifiées et des paramètres facultatifs de style et de contrôle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | - | Prompt pour la génération d'image. (par défaut : "") |
| `size` | COMBO | Oui | "1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | La taille de l'image générée. (par défaut : "1024x1024") |
| `n` | INT | Oui | 1-6 | Le nombre d'images à générer. (par défaut : 1) |
| `seed` | INT | Oui | 0-18446744073709551615 | Graine pour déterminer si le nœud doit se réexécuter ; les résultats réels sont non déterministes quelle que soit la graine. (par défaut : 0) |
| `recraft_style` | RECRAFT_STYLE | Non | Plusieurs options disponibles | Sélection facultative du style pour la génération d'image. Lorsqu'il n'est pas fourni, le style par défaut est "realistic_image". |
| `negative_prompt` | STRING | Non | - | Une description textuelle facultative des éléments indésirables sur une image. (par défaut : "") |
| `recraft_controls` | RECRAFT_CONTROLS | Non | Plusieurs options disponibles | Contrôles supplémentaires facultatifs sur la génération via le nœud Recraft Controls. |

**Remarque :** Le paramètre `seed` contrôle uniquement le moment où le nœud se réexécute mais ne rend pas la génération d'image déterministe. Les images de sortie réelles varieront même avec la même valeur de graine.

**Remarque :** Le paramètre `prompt` doit avoir une longueur comprise entre 1 et 1000 caractères.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `IMAGE` | IMAGE | La ou les images générées sous forme de sortie tensorielle par lots. Lorsque plusieurs images sont générées (n > 1), elles sont concaténées le long de la dimension du lot. |

---
**Source fingerprint (SHA-256):** `28c510ccfad13ddb50700b465af14deaa3c7c1f8597fef048d89094fd24fcd7d`
