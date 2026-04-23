> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Painter/fr.md)

Le nœud Painter fournit une toile interactive pour créer ou modifier des images et des masques directement dans ComfyUI. Il vous permet de démarrer avec une toile vierge ou une image existante, de peindre dessus à l'aide d'un outil pinceau, et de produire en sortie à la fois l'image résultante et un masque alpha correspondant. Le masque définit les zones peintes, qui sont ensuite compositées par-dessus l'image de base ou la couleur d'arrière-plan.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Non | - | Image de base optionnelle sur laquelle peindre. Si elle n'est pas fournie, une toile vierge est créée en utilisant la couleur d'arrière-plan, la largeur et la hauteur spécifiées. |
| `mask` | STRING | Oui | - | Les données de peinture, généralement générées par le widget interactif intégré au nœud. Ce paramètre est géré par l'outil de peinture de l'interface utilisateur et n'est pas destiné à être connecté à une prise standard. |
| `width` | INT | Oui | 64 à 4096 | La largeur de la toile en pixels, utilisée lorsqu'aucune `image` de base n'est fournie. La valeur doit être un multiple de 64. La valeur par défaut est 512. |
| `height` | INT | Oui | 64 à 4096 | La hauteur de la toile en pixels, utilisée lorsqu'aucune `image` de base n'est fournie. La valeur doit être un multiple de 64. La valeur par défaut est 512. |
| `bg_color` | COLOR | Oui | - | La couleur d'arrière-plan de la toile, spécifiée sous forme de code hexadécimal (par exemple, #000000). Elle n'est utilisée que lorsqu'aucune `image` de base n'est fournie. La valeur par défaut est le noir (#000000). |

**Note :** L'entrée `mask` est conçue pour fonctionner avec le widget d'interface utilisateur spécialisé du nœud. Lorsque vous peignez sur la toile, le widget remplit automatiquement cette valeur. Les entrées `width` et `height` sont masquées dans l'interface standard mais définissent les dimensions de la toile lors de la création d'une nouvelle image.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | L'image finale compositée. Il s'agit du résultat du mélange des zones peintes (provenant du `mask`) par-dessus l'`image` de base fournie ou l'arrière-plan coloré. |
| `MASK` | MASK | Le masque de canal alpha (transparence) extrait de la peinture. Les zones blanches représentent les régions peintes, et les zones noires représentent l'arrière-plan non touché. |