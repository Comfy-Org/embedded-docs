# Google Gemini Decision (Choice)

Choisissez l’une de vos propres options pour le texte, les images, l’audio ou la vidéo que vous connectez, et récupérez l’option choisie, sa position et un indice de confiance. Connectez `choice` à un nœud Branch dont les entrées portent les mêmes noms d’option, ou effectuez le routage sur `option_index` lorsqu’un nœud Branch n’est pas disponible.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `model` | Modèle à utiliser (par défaut : `"gemini-decision-1"`). | COMBO | Oui | `"gemini-decision-1"` |
| `question` | La question à laquelle les options répondent, jusqu’à 5000 caractères (par défaut : "What style is the image?"). | STRING | Oui | 1 à 5000 caractères |
| `options` | Une option par ligne, utilisée exactement telle que saisie, jusqu’à 128 caractères chacune. Ajoutez une option telle que `other` pour les entrées qui ne correspondent à aucune d’elles (par défaut : `photo`, `illustration`, `3d render`, `anime`, `sketch`, `other`). | STRING | Oui | 2 à 255 options |
| `images` | Images à classer, jusqu’à 16 via les emplacements extensibles (`image_1` ... `image_16`). Une image en lot compte une fois par image. | IMAGE | Non | Jusqu’à 16 images |
| `audio` | Clip audio à classer. | AUDIO | Non | - |
| `video` | Clip vidéo à classer. | VIDEO | Non | - |
| `text` | Texte sur lequel porte la question, tel qu’un prompt ou une réponse de LLM, jusqu’à 20000 caractères. | STRING | Non | Jusqu’à 20000 caractères |

Donnez au moins 2 et au plus 255 options, sans en lister aucune deux fois ; sinon, le nœud lève une erreur. Connectez au moins l’un de `text`, `images`, `audio` ou `video`, et nommez plusieurs images `image_1`, `image_2`, etc. dans la question.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `choice` | L’option choisie, exactement telle qu’elle a été écrite dans `options`. | STRING |
| `option_index` | Position de l’option choisie dans `options`, en commençant à 0. | INT |
| `confidence` | Confiance dans le choix, entre 0 et 1. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionChoice/fr.md)

---
**Source fingerprint (SHA-256):** `200c63a9197cd95ba0a21da88c5f3117014b37b0651541094a775219381afe43`
