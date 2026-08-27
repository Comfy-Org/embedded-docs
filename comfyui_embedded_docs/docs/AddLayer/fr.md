# AddLayer

Le nœud Add Layer convertit une image d’entrée en un calque et le place sur un canevas, soit en démarrant une nouvelle pile de calques, soit en l’ajoutant à une pile existante. Vous pouvez définir le nom, la position, la taille, la rotation, l’opacité, le mode de fusion, l’ordre d’empilement et le retournement horizontal ou vertical du calque. Ce nœud est marqué comme expérimental.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `calques` | Pile de calques à laquelle ajouter le calque. Laisser non connecté pour démarrer une nouvelle pile. | LAYERS | Non | — |
| `image` | Contenu du calque à sa taille native. Un lot d’images se déploie en calques consécutifs. | IMAGE | Oui | — |
| `masque` | Masque de transparence pour ce calque. Les zones masquées (valeur 1) deviennent transparentes, en multipliant tout canal alpha que l’image contient déjà. | MASK | Non | — |
| `nom` | Nom du calque affiché dans l’éditeur de composition. (défaut : "") | STRING | Non | — |
| `x` | Placement horizontal initial sur le canevas. (défaut : 0) | INT | Non | -MAX_RESOLUTION à MAX_RESOLUTION |
| `y` | Placement vertical initial sur le canevas. (défaut : 0) | INT | Non | -MAX_RESOLUTION à MAX_RESOLUTION |
| `opacité` | Opacité initiale du calque. (défaut : 1.0) | FLOAT | Non | 0.0 à 1.0 (pas 0.01) |
| `mode de fusion` | Mode de fusion initial, appliqué aux calques inférieurs. Sur le calque inférieur, au-dessus du fond transparent par défaut, les modes non normaux produisent de la transparence. (défaut : "normal") | COMBO | Non | Plusieurs options disponibles |
| `rotation` | Rotation initiale en degrés, dans le sens horaire. (défaut : 0.0) | FLOAT | Non | -360.0 à 360.0 (pas 1.0) |
| `largeur` | Largeur d’affichage initiale. 0 conserve la largeur native de l’image. (défaut : 0) | INT | Non | 0 à MAX_RESOLUTION |
| `hauteur` | Hauteur d’affichage initiale. 0 conserve la hauteur native de l’image. (défaut : 0) | INT | Non | 0 à MAX_RESOLUTION |
| `z_index` | Surcharge d’empilement. Les calques sont triés de manière stable selon `z_index` ; les valeurs égales conservent leur ordre de liste. (défaut : 0) | INT | Non | -1000 à 1000 |
| `retourner_h` | Retourne le calque horizontalement. (défaut : False) | BOOLEAN | Non | false / true |
| `retourner_v` | Retourne le calque verticalement. (défaut : False) | BOOLEAN | Non | false / true |

Notes :

- Seul `image` est requis ; tous les autres paramètres sont facultatifs.
- Lorsque `layers` est laissé non connecté, une nouvelle pile de calques est créée. Lorsqu’une pile de calques est connectée, le nouveau calque y est ajouté.
- Un lot d’images dans l’entrée `image` crée plusieurs calques consécutifs.
- `width` et `height` ont pour valeur par défaut 0, ce qui conserve les dimensions natives de l’image. Des valeurs supérieures à 0 remplacent la taille d’affichage.
- `opacity`, `blend_mode`, `rotation`, `width` et `height` ne sont appliqués que lorsqu’ils diffèrent de leurs valeurs par défaut.
- La taille du canevas d’une pile de calques connectée est préservée dans la sortie.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `layers` | La pile de calques avec ce calque ajouté. | LAYERS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddLayer/fr.md)

---
**Source fingerprint (SHA-256):** `b7bf1a012d17cb5768b49d5c0617e13562ba015f695e6c9b1d1bbefba4150f9e`
