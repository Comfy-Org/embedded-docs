# TypeSafe Jev (Score)

Le nœud TypeSafe Jev (Score) évalue le texte, les images ou les deux qui lui sont connectés de 1 à 10 et compare la note à un seuil. Connectez `result` à un nœud If/Else Switch pour agir sur la note, ou lisez `score` pour utiliser la note brute. Il s’agit d’un nœud API : il s’exécute sur les serveurs de Comfy et nécessite un compte Comfy.org avec des crédits.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle Jev à utiliser. Un seul modèle est actuellement disponible : `jev-1.14.0`. | COMBO | Oui | `"jev-1.14.0"` |
| `question` | Ce qu’il faut évaluer, sur une échelle de 1 à 10. Indiquez ce que signifient 1 et 10, comme dans la valeur par défaut (par défaut : `Rate the technical quality of the image from 1 (worst) to 10 (best).`). | STRING | Oui | 1 à 1000 caractères |
| `threshold` | `result` est vrai lorsque la note est au moins égale à cette valeur (par défaut : 5.0). | FLOAT | Oui | 1.0 à 10.0 (pas : 0.1) |
| `images` | Les images concernées par la question. Jusqu’à 32 images au total ; une entrée groupée compte une fois par image. Le grand côté de chaque image est plafonné par le nombre total d’images : 1568 px pour jusqu’à 4 images, 1024 px pour jusqu’à 8, 768 px pour jusqu’à 16 et 512 px pour jusqu’à 32 ; ainsi, un lot plus grand peut réduire le détail de chaque image. | AUTOGROW | Non | 0 à 32 images |
| `text` | Le texte concerné par la question, comme un prompt ou une réponse de LLM. | STRING | Non | 0 à 3000 caractères |

**Remarques :**

- Connectez du texte ou au moins une image ; le nœud génère une erreur lorsque les deux sont vides.
- La note est indiquée de 1 à 10, et `result` est vrai lorsqu’elle est au moins égale à `threshold`.
- La facturation est basée sur les tokens ; le badge de prix sur le nœud indique le tarif approximatif pour 1 M de tokens.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `result` | Vrai lorsque `score` est au moins égal à `threshold`. | BOOLEAN |
| `score` | La note de 1 (le pire) à 10 (le meilleur). | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevScore/fr.md)

---
**Source fingerprint (SHA-256):** `7e1970e903d2099ab3d7481a758c5291e87614b9eaf116d0ced6a1bcd36dc126`
