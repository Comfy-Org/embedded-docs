# Google Gemini Decision (Score)

Évaluez de 1 à 10 le texte, les images, l’audio ou la vidéo que vous connectez, et obtenez le score ainsi qu’un booléen qui bascule au seuil que vous définissez. Utilisez-le pour filtrer ou trier les sorties, par exemple pour ne conserver que les images dont le score est d’au moins 7, et connectez `result` à un nœud If/Else Switch pour agir en conséquence. Une exécution évalue l’ensemble de ce que vous connectez ; pour filtrer des images individuellement, il faut donc les évaluer une par une.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser (par défaut : `"gemini-decision-1"`). | COMBO | Oui | `"gemini-decision-1"` |
| `question` | Ce qu’il faut évaluer, en précisant ce que signifient 1 et 10 (par défaut : « Rate the technical quality of the image from 1 (worst) to 10 (best). »). | STRING | Oui | 1 à 5000 caractères |
| `threshold` | `result` vaut True lorsque le score est au moins égal à cette valeur. Des images nettes et bien définies obtiennent environ 7 à 8, des images fortement endommagées environ 3 à 5 (par défaut : 6.0). | FLOAT | Oui | 1.0 à 10.0 (pas : 0.1) |
| `images` | Images à évaluer, jusqu’à 16 réparties entre les emplacements extensibles (`image_1` ... `image_16`). Une image faisant partie d’un lot compte une fois par image. | IMAGE | Non | Jusqu’à 16 images |
| `audio` | Clip audio à évaluer. | AUDIO | Non | - |
| `video` | Clip vidéo à évaluer. | VIDEO | Non | - |
| `text` | Texte sur lequel porte la question, comme un prompt ou une réponse de LLM, jusqu’à 20000 caractères. | STRING | Non | Jusqu’à 20000 caractères |

Connectez au moins l’un des éléments `text`, `images`, `audio` ou `video` ; le nœud lève une erreur lorsqu’il n’y a rien à évaluer. Avec plusieurs images, nommez-les `image_1`, `image_2`, etc. dans la question.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `result` | True lorsque le score est au moins égal à `threshold`, sinon False. | BOOLEAN |
| `score` | La note de 1 à 10. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionScore/fr.md)

---
**Source fingerprint (SHA-256):** `9b0a68cc7f29b1d4d23e23e051a008f34932aac6d1fe1a16e45a0e70b4df412f`
