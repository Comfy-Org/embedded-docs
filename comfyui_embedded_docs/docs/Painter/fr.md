> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Painter/fr.md)

Voici la traduction en français de la documentation du nœud Painter, conforme à vos règles :

Le nœud Painter fournit un canevas interactif pour créer ou modifier des images et des masques directement dans ComfyUI. Il permet de démarrer avec un canevas vierge ou une image existante, de peindre dessus à l'aide d'un outil pinceau, et produit à la fois l'image résultante et un masque alpha correspondant. Le masque définit les zones peintes, qui sont ensuite composées sur l'image de base ou la couleur d'arrière-plan.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Non | - | Image de base facultative sur laquelle peindre. Si elle n'est pas fournie, un canevas vierge est créé en utilisant la couleur d'arrière-plan, la largeur et la hauteur spécifiées. |
| `mask` | STRING | Oui | - | Les données de peinture, généralement générées par le widget interactif intégré du nœud. Ce paramètre est géré par l'outil de peinture de l'interface utilisateur et n'est pas destiné à être connecté à une prise standard. |
| `width` | INT | Oui | 64 à 4096 | La largeur du canevas en pixels, utilisée lorsqu'aucune `image` de base n'est fournie. La valeur doit être un multiple de 64. Par défaut : 512. |
| `height` | INT | Oui | 64 à 4096 | La hauteur du canevas en pixels, utilisée lorsqu'aucune `image` de base n'est fournie. La valeur doit être un multiple de 64. Par défaut : 512. |
| `bg_color` | COLOR | Oui | - | La couleur d'arrière-plan du canevas, spécifiée sous forme de code hexadécimal (par exemple, #000000). Elle n'est utilisée que lorsqu'aucune `image` de base n'est fournie. Par défaut : noir (#000000). |

**Remarque :** L'entrée `mask` est conçue pour fonctionner avec le widget d'interface utilisateur spécialisé du nœud. Lorsque vous peignez sur le canevas, le widget remplit automatiquement cette valeur. Les entrées `width` et `height` sont masquées dans l'interface utilisateur standard, mais définissent les dimensions du canevas lors de la création d'une nouvelle image.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `IMAGE` | IMAGE | L'image finale composée. Il s'agit du résultat du mélange des zones peintes (provenant du `mask`) sur l'`image` de base fournie ou l'arrière-plan coloré. |
| `MASK` | MASK | Le masque de canal alpha (transparence) extrait de la peinture. Les zones blanches représentent les régions peintes, et les zones noires représentent l'arrière-plan non touché. |

---
**Source fingerprint (SHA-256):** `ae926b6d30aab65737bd99a58cb7de5a71fa36e61a677dbc97fc30b8ef8d2418`
