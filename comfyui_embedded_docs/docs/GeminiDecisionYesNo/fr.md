# Google Gemini Decision (Yes/No)

Posez une question de type oui/non sur le texte, les images, l’audio ou la vidéo que vous connectez et obtenez un booléen sur lequel aiguiller. Connectez `result` à un nœud If/Else Switch pour envoyer l’exécution dans l’une des deux branches, et lisez `answer` et `probability` lorsque vous voulez voir pourquoi le modèle a répondu de cette manière.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `model` | Modèle à utiliser (par défaut : `"gemini-decision-1"`). | COMBO | Oui | `"gemini-decision-1"` |
| `question` | La question oui/non portant sur ce qui est connecté, jusqu’à 5000 caractères. Posez-la de sorte que « oui » corresponde au cas que vous souhaitez traiter (par défaut : « Is there a person in the image? »). | STRING | Oui | 1 à 5000 caractères |
| `threshold` | Probabilité de « oui » à laquelle `result` devient true. Les réponses clairement affirmatives obtiennent environ 0.85 à 0.92, donc 0.9 ou plus en rejette beaucoup (par défaut : 0.5). | FLOAT | Oui | 0.01 à 0.99 (pas : 0.01) |
| `images` | Images sur lesquelles porte la question, jusqu’à 16 réparties entre les emplacements extensibles (`image_1` ... `image_16`). Un lot d’images compte une fois par image qu’il contient. | IMAGE | Non | Jusqu’à 16 images |
| `audio` | Clip audio sur lequel porte la question. | AUDIO | Non | - |
| `video` | Clip vidéo sur lequel porte la question. | VIDEO | Non | - |
| `text` | Texte sur lequel porte la question, comme un prompt ou une réponse de LLM, jusqu’à 20000 caractères. | STRING | Non | Jusqu’à 20000 caractères |

Connectez au moins l’un des éléments `text`, `images`, `audio` ou `video` ; le nœud lève une erreur lorsqu’il n’y a rien à examiner. Avec plusieurs images, nommez-les `image_1`, `image_2`, etc. dans la question.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `result` | La réponse sous forme de booléen : true pour « oui », false pour « non ». | BOOLEAN |
| `answer` | La réponse sous forme de chaîne `"yes"` ou `"no"`. | STRING |
| `probability` | Probabilité de « oui » entre 0 et 1. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionYesNo/fr.md)

---
**Source fingerprint (SHA-256):** `0339031baf5648609b82526bed97ce8744986878bcbb706dcd3aa79a7370d83f`
