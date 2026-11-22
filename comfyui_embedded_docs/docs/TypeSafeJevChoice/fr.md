# TypeSafe Jev (Choice)

Le nœud TypeSafe Jev (Choice) sélectionne l’une de vos propres options pour du texte, des images ou les deux, connectés. Connectez `choice` à un nœud Branch dont les entrées portent les noms des options, ou utilisez `option_index` pour basculer selon la position de l’option choisie. Il s’agit d’un nœud API qui nécessite un compte Comfy.org et une clé API.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle Jev à utiliser. Un seul modèle est actuellement disponible : `jev-1.14.0`. | COMBO | Oui | `"jev-1.14.0"` |
| `question` | La question à laquelle les options répondent. Avec plusieurs sockets d’images, utilisez leurs noms, par exemple `Which season is shown in image_1?` (par défaut : `What style is the image?`). | STRING | Oui | 1 à 1000 caractères |
| `options` | Les options parmi lesquelles choisir, une par ligne. Ajoutez une option telle que `other` pour les entrées qui ne correspondent à aucune d’elles (par défaut : `photo`, `illustration`, `3d render`, `anime`, `sketch` et `other`, une par ligne). | STRING | Oui | 2 à 50 options, jusqu’à 40 caractères chacune |
| `images` | Les images auxquelles la question se rapporte. Jusqu’à 32 images au total ; une entrée groupée compte une fois par image, et plus de 4 images sont envoyées à une taille plus petite. | AUTOGROW | Non | 0 à 32 images |
| `text` | Le texte auquel la question se rapporte, comme un prompt ou une réponse de LLM. | STRING | Non | 0 à 3000 caractères |

**Remarques :**

- Connectez du texte ou au moins une image ; le nœud lève une erreur lorsque les deux sont vides.
- Le nœud lève une erreur lorsque moins de 2 ou plus de 50 options sont fournies, lorsqu’une option dépasse 40 caractères, ou lorsque deux options ne diffèrent que par la casse.
- `option_index` compte à partir de 0 ; la première option de la liste a donc l’indice 0.
- La facturation est basée sur les tokens ; le badge de prix sur le nœud indique le tarif approximatif pour 1 M de tokens.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `choice` | L’option choisie, écrite exactement telle qu’elle apparaît dans `options`. | STRING |
| `option_index` | Position de l’option choisie dans la liste des options, en commençant à 0. | INT |
| `confidence` | Le degré de certitude de Jev, de 0 (aucun gagnant clair) à 1 (certain). | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevChoice/fr.md)

---
**Source fingerprint (SHA-256):** `b1cd36d600f5c07935c455d9e926e6c0a53f172fcc1a6f602c8d4dc70eeffabe`
