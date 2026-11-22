# HeyGen Decision (Yes/No)

Posez une question par oui/non sur le texte, les images, l’audio ou la vidéo que vous connectez et obtenez un booléen sur lequel effectuer un routage. Connectez `result` à un nœud If/Else Switch pour choisir entre deux chemins, et lisez `answer` et `probability` pour voir à quel point la réponse était claire.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Modèle à utiliser. `heygen-decision-1-turbo` est plus rapide et coûte moins cher que `heygen-decision-1` (par défaut : `"heygen-decision-1"`). | COMBO | Oui | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `question` | La question par oui/non sur ce qui est connecté, jusqu’à 5000 caractères. Posez-la de manière à ce que « oui » corresponde au cas sur lequel vous agissez (par défaut : `"Is there a person in the image?"`). | STRING | Oui | 1 à 5000 caractères |
| `seuil` | Probabilité de « oui » à laquelle `result` devient vrai ; les réponses claires sont proches de 0 ou 1 (par défaut : 0.5). | FLOAT | Oui | 0.01 à 0.99 (pas : 0.01) |
| `images` | Images sur lesquelles porte la question, jusqu’à 4 au total, en comptant chaque image d’un lot. Elles sont numérotées `image_1` à `image_4` dans l’ordre sur les sockets. | IMAGE | Non | Jusqu’à 4 images |
| `audio_1` | Audio sur lequel porte la question, jusqu’à 30 minutes. | AUDIO | Non | Jusqu’à 30 minutes |
| `video_1` | Vidéo sur laquelle porte la question, jusqu’à 60 secondes. | VIDEO | Non | Jusqu’à 60 secondes |
| `texte` | Texte sur lequel porte la question, comme un prompt ou une réponse de LLM, jusqu’à 20 000 caractères. | STRING | Non | Jusqu’à 20 000 caractères |

Connectez au moins l’un des éléments `text`, `images`, `audio_1` ou `video_1`, et faites-y référence par le nom du socket dans la question, par exemple « Est-ce que image_2 montre la même personne que image_1 ? ».

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `result` | Vrai lorsque la probabilité de « oui » atteint `threshold`, faux sinon. | BOOLEAN |
| `answer` | Le verdict sous forme de chaîne `"yes"` ou `"no"`, en suivant le même `threshold` que `result`. | STRING |
| `probability` | Probabilité de « oui » entre 0 et 1. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionYesNo/fr.md)

---
**Source fingerprint (SHA-256):** `5a6a606d5c6ef62eb3424bd54a0da3dc177da7d0acf4b5c235a62b78ad8d2df1`
