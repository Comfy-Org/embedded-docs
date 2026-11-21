# Google Gemini Decision (Yes/No)

Posez une question fermée (oui/non) sur le texte, les images, l’audio ou la vidéo que vous connectez et obtenez un booléen sur lequel effectuer un routage. Connectez `result` à un nœud If/Else Switch pour envoyer l’exécution sur l’un des deux chemins, et lisez `answer` et `probability` lorsque vous voulez voir pourquoi le modèle a répondu de cette façon.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `model` | Modèle à utiliser (par défaut : `"gemini-decision-1"`). | COMBO | Oui | `"gemini-decision-1"` |
| `question` | La question fermée (oui/non) concernant ce qui est connecté, jusqu’à 5000 caractères. Formulez-la de sorte que « yes » corresponde au cas sur lequel vous agissez (par défaut : "Is there a person in the image?"). | STRING | Oui | 1 à 5000 caractères |
| `threshold` | Probabilité de « yes » à laquelle `result` devient vrai. Les réponses clairement « yes » obtiennent environ 0.85 à 0.92, donc 0.9 ou plus en rejette beaucoup (par défaut : 0.5). | FLOAT | Oui | 0.01 à 0.99 (pas : 0.01) |
| `images` | Images sur lesquelles porte la question, jusqu’à 16 réparties entre les emplacements extensibles (`image_1` ... `image_16`). Une image fournie dans un lot compte une fois par image. | IMAGE | Non | Jusqu’à 16 images |
| `audio` | Clip audio sur lequel porte la question. | AUDIO | Non | - |
| `video` | Clip vidéo sur lequel porte la question. | VIDEO | Non | - |
| `text` | Texte sur lequel porte la question, comme un prompt ou une réponse de LLM, jusqu’à 20000 caractères. | STRING | Non | Jusqu’à 20000 caractères |

Connectez au moins l’un des éléments `text`, `images`, `audio` ou `video` ; le nœud lève une erreur lorsqu’il n’y a rien à examiner. Avec plusieurs images, nommez-les `image_1`, `image_2`, etc. dans la question : un lot est développé image par image, donc les numéros comptent les images individuelles à travers les emplacements dans l’ordre de connexion.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `result` | Vrai lorsque la probabilité de « yes » atteint `threshold`, faux sinon. | BOOLEAN |
| `answer` | Le verdict sous forme de chaîne `"yes"` ou `"no"`, en suivant le même `threshold` que `result`. | STRING |
| `probability` | Probabilité de « yes » entre 0 et 1. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionYesNo/fr.md)

---
**Source fingerprint (SHA-256):** `0339031baf5648609b82526bed97ce8744986878bcbb706dcd3aa79a7370d83f`
