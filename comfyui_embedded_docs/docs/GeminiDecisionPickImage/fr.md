# Google Gemini Decision (Pick Image)

Choisissez la meilleure image d'un lot. Connectez `index` à Get Image from Batch pour conserver l'image choisie, afin que le reste du workflow ne s'exécute que sur cette sélection.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser (par défaut : `"gemini-decision-1"`). | COMBO | Oui | `"gemini-decision-1"` |
| `question` | Quelle image choisir (par défaut : "Which image best matches the prompt in text? If there is no text, which image has the best quality?"). | STRING | Oui | 1 à 5000 caractères |
| `images` | Les images parmi lesquelles choisir, sous forme de lot ou de lot unique de frames. | IMAGE | Oui | 2 à 64 images |
| `text` | Texte sur lequel porte la question, tel que le prompt à partir duquel les images ont été créées, jusqu'à 20000 caractères. | STRING | Non | Jusqu'à 20000 caractères |

Le nœud nécessite de 2 à 64 images et renvoie une erreur pour une seule image. Connectez `text` lorsque le choix doit suivre un prompt plutôt que la seule qualité de l'image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `index` | Position de l'image choisie dans le lot, en commençant à 0. | INT |
| `confidence` | Confiance dans la sélection, entre 0 et 1. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionPickImage/fr.md)

---
**Source fingerprint (SHA-256):** `55eb604923cb66b42f23f37d0c710a97033cc2c5d95880d45397bba10e44dab0`
