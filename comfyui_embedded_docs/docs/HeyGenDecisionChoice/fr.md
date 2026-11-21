# HeyGen Decision (Choice)

Choisissez l’une de vos propres options pour le texte, les images, l’audio ou la vidéo que vous connectez, et récupérez l’option choisie, sa position et un indice de confiance. Connectez `choice` à un nœud Branch dont les entrées portent les mêmes noms d’options, ou effectuez le routage sur `option_index`. Un nœud Branch accepte au maximum 32 entrées ; pour des ensembles d’options plus grands, effectuez le routage avec `option_index`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser. `heygen-decision-1-turbo` est plus rapide et coûte moins cher que `heygen-decision-1` (par défaut : `"heygen-decision-1"`). | COMBO | Oui | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `question` | La question à laquelle les options répondent, jusqu’à 5000 caractères (par défaut : "What style is the image?"). | STRING | Oui | 1 à 5000 caractères |
| `options` | Une option par ligne, utilisée exactement telle que saisie, jusqu’à 128 caractères chacune. Ajoutez une option telle que `other` pour les entrées qui ne correspondent à aucune d’entre elles (par défaut : `photo`, `illustration`, `3d render`, `anime`, `sketch`, `other`). | STRING | Oui | 2 à 255 options |
| `images` | Images à classifier, jusqu’à 4 au total, en comptant chaque image d’un lot. Elles sont numérotées `image_1` à `image_4` dans l’ordre sur les sockets. | IMAGE | Non | Jusqu’à 4 images |
| `audio_1` | Audio à classifier, jusqu’à 30 minutes. | AUDIO | Non | Jusqu’à 30 minutes |
| `video_1` | Vidéo à classifier, jusqu’à 60 secondes. | VIDEO | Non | Jusqu’à 60 secondes |
| `text` | Texte sur lequel porte la question, comme un prompt ou une réponse de LLM, jusqu’à 20000 caractères. | STRING | Non | Jusqu’à 20000 caractères |

Donnez 2 à 255 options, aucune en double et aucune ne différant uniquement par la casse, sinon le nœud lève une erreur. Connectez au moins une entrée à classifier et nommez-les par socket dans la question, par exemple « Quelle saison est affichée dans image_1 ? ».

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `choice` | L’option choisie, exactement telle qu’elle a été écrite dans `options`. | STRING |
| `option_index` | Position de l’option choisie dans `options`, en commençant à 0. | INT |
| `confidence` | Confiance accordée au choix, entre 0 et 1. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionChoice/fr.md)

---
**Source fingerprint (SHA-256):** `dd21b3b8021b8917e7ee4d120471974634ae6771ff17b0f49e9460f82a2fbe78`
