# TypeSafe Jev (Pick Image)

Le nœud TypeSafe Jev (Pick Image) sélectionne une image dans un lot. Connectez le même lot d'images à Get Image from Batch avec `index` pour conserver l'image sélectionnée, ou lisez `confidence` pour décider si la sélection est suffisamment bonne. Il s'agit d'un nœud API : il s'exécute sur les serveurs de Comfy et nécessite un compte Comfy.org avec des crédits.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle Jev à utiliser. Un seul modèle est actuellement disponible : `jev-1.14.0`. | COMBO | Oui | `"jev-1.14.0"` |
| `question` | Quelle image sélectionner. Connectez le prompt à `text` pour sélectionner l'image qui lui correspond le mieux (par défaut : `Which image best matches the prompt in text? If there is no text, which image has the best quality?`). | STRING | Oui | 1 à 1000 caractères |
| `images` | Les images parmi lesquelles choisir. Une entrée par lot compte une fois par image, donc chaque image du lot est candidate. Le côté long de chaque image est limité par la taille du lot avant l'envoi : 1568 px pour jusqu'à 4 images, 1024 px pour jusqu'à 8, 768 px pour jusqu'à 16 et 512 px pour jusqu'à 32 ; un lot plus important peut donc réduire le détail de chaque image. | IMAGE | Oui | 2 à 32 images |
| `text` | Le texte sur lequel porte la question, comme le prompt à partir duquel les images ont été générées. | STRING | Non | 0 à 3000 caractères |

**Remarques :**

- Le nœud renvoie une erreur lorsque moins de 2 ou plus de 32 images sont connectées.
- `index` commence à 0, ce qui correspond à la position attendue par Get Image from Batch.
- La facturation est basée sur les tokens ; le badge de prix sur le nœud indique le tarif approximatif par 1M de tokens.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `index` | Position de l'image sélectionnée dans le lot, en commençant à 0. | INT |
| `confidence` | Niveau de certitude de Jev, de 0 (aucun gagnant clair) à 1 (certain). | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/fr.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`
