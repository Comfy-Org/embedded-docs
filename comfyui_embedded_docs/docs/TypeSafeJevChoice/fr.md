# TypeSafe Jev (Choice)

Le nœud TypeSafe Jev (Choice) sélectionne l’une de vos propres options pour du texte connecté, des images connectées, ou les deux. Connectez `choice` à un nœud Branch dont les entrées portent les noms des options, ou utilisez `option_index` pour basculer selon la position de l’option choisie. Un nœud Branch prend au plus 32 entrées, donc une liste comportant plus d’options que cela ne peut être routée que par `option_index`. Il s’agit d’un nœud API : il s’exécute sur les serveurs de Comfy et nécessite un compte Comfy.org avec des crédits.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle Jev à utiliser. Un seul modèle est actuellement disponible : `jev-1.14.0`. | COMBO | Oui | `"jev-1.14.0"` |
| `question` | La question à laquelle les options répondent. Avec plusieurs emplacements d’image, utilisez leurs noms, par exemple `Which season is shown in image_1?` (par défaut : `What style is the image?`). | STRING | Oui | 1 à 1000 caractères |
| `options` | Les options parmi lesquelles choisir, une par ligne. Les espaces de début et de fin sont supprimés de chaque ligne, et les options doivent être uniques en ignorant la casse ; une option répétée ou deux options qui ne diffèrent que par la casse sont donc rejetées. Ajoutez une option telle que `other` pour les entrées qui ne correspondent à aucune d’elles (par défaut : `photo`, `illustration`, `3d render`, `anime`, `sketch` et `other`, une par ligne). | STRING | Oui | 2 à 50 options, jusqu’à 40 caractères chacune |
| `images` | Les images auxquelles la question se rapporte. Jusqu’à 32 images au total ; une entrée en lot compte une fois par image. Le côté long de chaque image est limité par le nombre total d’images : 1568 px pour jusqu’à 4 images, 1024 px pour jusqu’à 8, 768 px pour jusqu’à 16 et 512 px pour jusqu’à 32, donc un lot plus important peut réduire le détail de chaque image. | AUTOGROW | Non | 0 à 32 images |
| `text` | Le texte auquel la question se rapporte, comme un prompt ou une réponse de LLM. | STRING | Non | 0 à 3000 caractères |

**Remarques :**

- Connectez du texte ou au moins une image ; le nœud lève une erreur lorsque les deux sont vides.
- Le nœud lève une erreur lorsque moins de 2 ou plus de 50 options sont fournies, lorsqu’une option dépasse 40 caractères ou lorsque deux options sont identiques en ignorant la casse.
- `option_index` compte à partir de 0, donc la première option de la liste a l’indice 0.
- La facturation est basée sur les tokens ; le badge de prix sur le nœud indique le tarif approximatif pour 1 million de tokens.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `choice` | L’option choisie, avec les espaces de début et de fin supprimés. Une entrée Branch dont le nom conserve ces espaces ne correspondra pas. | STRING |
| `option_index` | Position de l’option choisie dans la liste des options, en commençant à 0. | INT |
| `confidence` | Le degré de certitude de Jev, de 0 (aucun gagnant clair) à 1 (certain). | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevChoice/fr.md)

---
**Source fingerprint (SHA-256):** `b1cd36d600f5c07935c455d9e926e6c0a53f172fcc1a6f602c8d4dc70eeffabe`
