# TypeSafe Jev (Yes/No)

Le nœud TypeSafe Jev (Yes/No) pose une question fermée (oui/non) sur du texte, des images ou les deux connectés, et renvoie la réponse sous forme de booléen. Connectez `result` à un nœud If/Else Switch pour aiguiller le workflow, ou lisez `probability` pour agir selon le degré de certitude du modèle. Il s’agit d’un nœud API : il s’exécute sur les serveurs de Comfy et nécessite un compte Comfy.org avec des crédits.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle Jev à utiliser. Un seul modèle est actuellement disponible : `jev-1.14.0`. | COMBO | Oui | `"jev-1.14.0"` |
| `question` | Question fermée (oui/non) à laquelle répondent le texte et les images connectés. Formulez-la de sorte que « oui » corresponde au cas sur lequel vous voulez agir ; avec plusieurs connecteurs d’image, utilisez leurs noms, par exemple `Does image_2 show the same person as image_1?` (par défaut : `Is there a person in the image?`). | STRING | Oui | 1 à 1000 caractères |
| `threshold` | La réponse est « oui » lorsque la probabilité de « oui » est au moins égale à cette valeur (par défaut : 0.5). | FLOAT | Oui | 0.01 à 0.99 (pas : 0.01) |
| `images` | Les images concernées par la question. Jusqu’à 32 images au total ; une entrée sous forme de lot compte une fois par image. Le côté long de chaque image est plafonné selon le nombre total d’images : 1568 px pour un maximum de 4 images, 1024 px pour un maximum de 8, 768 px pour un maximum de 16 et 512 px pour un maximum de 32, donc un lot plus grand signifie moins de détails dans chaque image. | AUTOGROW | Non | 0 à 32 images |
| `text` | Le texte concerné par la question, par exemple un prompt ou une réponse de LLM. | STRING | Non | 0 à 3000 caractères |

**Notes :**

- Connectez du texte ou au moins une image ; le nœud génère une erreur lorsque les deux sont vides.
- `result` est vrai lorsque `probability` est supérieure ou égale à `threshold`, et `answer` renvoie le même verdict sous la forme `yes` ou `no`.
- La facturation est basée sur les tokens ; le badge de prix sur le nœud indique le tarif approximatif pour 1 M de tokens.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `result` | La réponse sous forme de booléen : vrai lorsque la probabilité de « oui » est supérieure ou égale à `threshold`. | BOOLEAN |
| `answer` | La réponse sous forme de texte `yes` ou `no`. | STRING |
| `probability` | Probabilité de « oui », de 0 (certainement non) à 1 (certainement oui). | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevYesNo/fr.md)

---
**Source fingerprint (SHA-256):** `e8c7de5558c61e7c9058b28104a72d8d8961165983d02d63a5c9078c40855385`
