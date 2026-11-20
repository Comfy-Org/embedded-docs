# Google Gemini Decision (Score)

Évaluez de 1 à 10 le texte, les images, l’audio ou la vidéo que vous connectez, et obtenez le score ainsi qu’un booléen qui bascule à un seuil que vous définissez. Utilisez-le pour filtrer ou trier les sorties, par exemple pour ne conserver que les images ayant un score d’au moins 7, et connectez `result` à un nœud If/Else Switch pour agir en conséquence.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser (par défaut : `"gemini-decision-1"`). | COMBO | Oui | `"gemini-decision-1"` |
| `question` | Ce qu’il faut évaluer, en indiquant ce que signifient 1 et 10 (par défaut : "Rate the technical quality of the image from 1 (worst) to 10 (best)."). | STRING | Oui | 1 à 5000 caractères |
| `threshold` | `result` est vrai lorsque le score est au moins égal à cette valeur. Les images nettes et propres obtiennent environ 7 à 8, les images fortement endommagées environ 3 à 5 (par défaut : 6.0). | FLOAT | Oui | 1.0 à 10.0 (pas : 0.1) |
| `images` | Images à évaluer, jusqu’à 16 réparties sur les emplacements extensibles (`image_1` ... `image_16`). Un lot d’images compte une fois par image. | IMAGE | Non | Jusqu’à 16 images |
| `audio` | Clip audio à évaluer. | AUDIO | Non | - |
| `video` | Clip vidéo à évaluer. | VIDEO | Non | - |
| `text` | Texte auquel la question se rapporte, comme un prompt ou une réponse de LLM, jusqu’à 20000 caractères. | STRING | Non | Jusqu’à 20000 caractères |

Connectez au moins l’un des éléments `text`, `images`, `audio` ou `video` ; le nœud lève une erreur lorsqu’il n’y a rien à évaluer. Avec plusieurs images, nommez-les `image_1`, `image_2`, etc. dans la question.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `result` | Vrai lorsque le score est au moins égal à `threshold`, sinon faux. | BOOLEAN |
| `score` | La note de 1 à 10. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionScore/fr.md)

---
**Source fingerprint (SHA-256):** `9b0a68cc7f29b1d4d23e23e051a008f34932aac6d1fe1a16e45a0e70b4df412f`
