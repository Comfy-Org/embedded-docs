# HeyGen Decision (Score)

Évaluez de 1 à 10 le texte, les images, l’audio ou la vidéo que vous connectez, et obtenez le score ainsi qu’un booléen qui bascule à un seuil que vous définissez. Utilisez-le pour filtrer ou trier les sorties, et connectez `result` à un nœud If/Else Switch pour agir en fonction du score.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Modèle à utiliser. `heygen-decision-1-turbo` est plus rapide et coûte moins cher que `heygen-decision-1` (par défaut : `"heygen-decision-1"`). | COMBO | Oui | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `question` | Ce qu’il faut évaluer, en précisant ce que signifient 1 et 10 (par défaut : « Rate the technical quality of the image from 1 (worst) to 10 (best). »). | STRING | Oui | 1 à 5000 caractères |
| `seuil` | `result` est vrai lorsque le score est au moins égal à cette valeur. Des images propres et nettes obtiennent environ 7, des images fortement endommagées environ 3 à 5 (par défaut : 6.0). | FLOAT | Oui | 1.0 à 10.0 (pas : 0.1) |
| `images` | Images à évaluer, jusqu’à 4 au total, en comptant chaque image d’un lot. Elles sont numérotées de `image_1` à `image_4` dans l’ordre sur l’ensemble des connecteurs. | IMAGE | Non | Jusqu’à 4 images |
| `audio_1` | Audio à évaluer, jusqu’à 30 minutes. | AUDIO | Non | Jusqu’à 30 minutes |
| `video_1` | Vidéo à évaluer, jusqu’à 60 secondes. | VIDEO | Non | Jusqu’à 60 secondes |
| `texte` | Texte auquel la question se rapporte, comme un prompt ou une réponse de LLM, jusqu’à 20000 caractères. | STRING | Non | Jusqu’à 20000 caractères |

Connectez au moins une entrée à évaluer et nommez-les par leur socket dans la question, par exemple « Quelle est la netteté de image_1 ? ».

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `result` | Vrai lorsque le score est au moins égal à `threshold`, sinon faux. | BOOLEAN |
| `score` | La note de 1 à 10. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionScore/fr.md)

---
**Source fingerprint (SHA-256):** `47f7aeab15292a2156b8da23c9911f4155c5b05c9ea9c0c502c30221aa522b58`
