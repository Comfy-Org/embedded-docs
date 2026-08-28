# Recraft Texte en Image

Génère des images de manière synchrone en fonction du prompt et de la résolution. Ce nœud se connecte à l'API Recraft pour créer des images à partir de descriptions textuelles avec des dimensions spécifiées et des paramètres facultatifs de style et de contrôle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt pour la génération d'image. (défaut : "") | STRING | Oui | - |
| `taille` | La taille de l'image générée. (défaut : "1024x1024") | COMBO | Oui | "1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" |
| `n` | Le nombre d'images à générer. (défaut : 1) | INT | Oui | 1-6 |
| `seed` | Seed permettant de déterminer si le nœud doit se réexécuter ; les résultats réels sont non déterministes quel que soit le seed. (défaut : 0) | INT | Oui | 0-18446744073709551615 |
| `recraft_style` | Sélection facultative du style pour la génération d'image. En l'absence de sélection, le style par défaut est "realistic_image". | RECRAFT_STYLE | Non | Plusieurs options disponibles |
| `negative_prompt` | Une description textuelle facultative des éléments indésirables sur une image. (défaut : "") | STRING | Non | - |
| `recraft_controls` | Contrôles supplémentaires facultatifs sur la génération via le nœud Recraft Controls. | RECRAFT_CONTROLS | Non | Plusieurs options disponibles |

**Remarque :** Le paramètre `seed` contrôle uniquement le moment où le nœud se réexécute, mais ne rend pas la génération d'image déterministe. Les images de sortie réelles varieront même avec la même valeur de seed.

**Remarque :** Le paramètre `prompt` doit contenir entre 1 et 1000 caractères.

**Remarque :** Si vous utilisez un `style_id` provenant de l'Infinite Style Library, assurez-vous qu'il ne s'agit pas d'un style d'art vectoriel, car cela renverrait des données SVG au lieu d'une image et provoquerait une erreur.

**Remarque :** Ce nœud utilise une API payante. Le coût est de $0.04 par image générée, selon la valeur de `n`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | Image(s) générée(s) sous forme de sortie tensorielle par lots. Lorsque plusieurs images sont générées (n > 1), elles sont concaténées le long de la dimension du lot. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `d75b7dd2d8cee70c3bc1d2c64fb07ce814a3672619e8647f4c4c2cdc2635945c`
