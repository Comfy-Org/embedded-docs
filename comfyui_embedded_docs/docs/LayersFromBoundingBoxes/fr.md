# LayersFromBoundingBoxes

Ce nœud convertit un lot d'images et ses boîtes englobantes en une pile de calques, créant un calque par image et plaçant chaque calque selon sa boîte englobante correspondante. Utilisez-le lorsqu'un nœud produit des calques sous forme de lot, car un lot ne porte qu'un seul emplacement pour chaque image et les positions individuelles seraient autrement perdues.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | Lot d'images ; chaque image devient un calque. | IMAGE | Oui | — |
| `bboxes` | Boîtes de placement, alignées par index avec le lot d'images. Accepte des boîtes englobantes (x, y, largeur, hauteur), des éléments normalisés (avec un « bbox » — ceux-ci nécessitent canvas_width/canvas_height pour être résolus en pixels), ou une chaîne JSON de l'un ou l'autre. Les images sans boîte correspondante sont placées à l'origine. La largeur/hauteur d'une boîte met le calque à l'échelle pour l'adapter à la boîte. metadata.name (ou desc) et metadata.z_index sont utilisés s'ils sont présents, et metadata.content_rect (relatif à l'image) recadre l'image sur son contenu réel. | BOUNDING_BOX, ARRAY, ou STRING | Oui | — |
| `mask` | Transparence par image, alignée par index avec le lot d'images (1 = transparent, convention de LoadImage). | MASK | Non | — |
| `layers` | Pile de calques à laquelle ajouter. Laissez non connecté pour démarrer une nouvelle pile. | LAYERS | Non | — |
| `crop_to_content` | Recadre chaque image sur metadata.content_rect s'il est présent et place le contenu à la position de la boîte plus le décalage du rectangle. Laissez activé pour les lots dont les images comportent du remplissage — cela ne conserve que le contenu réel à son emplacement réel. (défaut : true) | BOOLEAN | Non | true<br>false |
| `canvas_width` | Largeur du canevas du document. 0 la déduit des calques placés. (défaut : 0) | INT | Non | 0 à MAX_RESOLUTION |
| `canvas_height` | Hauteur du canevas du document. 0 la déduit des calques placés. (défaut : 0) | INT | Non | 0 à MAX_RESOLUTION |

Remarques :

- `bboxes` et `mask` doivent être alignés par index avec `image` : la nième boîte et la nième image de masque correspondent à la nième image du lot. Les images sans boîte correspondante sont placées à l'origine.
- Lorsque `bboxes` contient des éléments normalisés (avec un « bbox »), `canvas_width` et `canvas_height` doivent être fournis afin que ces positions normalisées puissent être résolues en pixels.
- `canvas_width` et `canvas_height` doivent tous deux être supérieurs à 0 pour définir explicitement le canevas du document. Si l'un des deux est 0, le canevas est déduit des calques placés ou hérité de la pile `layers` connectée.
- Lorsque `layers` est connectée, de nouveaux calques y sont ajoutés et reçoivent des valeurs z-index supérieures au z-index le plus élevé déjà présent dans la pile.
- Lorsque `crop_to_content` est activé et qu'une image possède un metadata.content_rect, l'image est recadrée selon ce rectangle et la mise à l'échelle largeur/hauteur de la boîte n'est pas appliquée ; à la place, le décalage du rectangle est ajouté à la position de la boîte.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `LAYERS` | La pile de calques, prête pour Create Layered Image. | LAYERS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LayersFromBoundingBoxes/fr.md)

---
**Source fingerprint (SHA-256):** `a70956bf0d7ea8bdbd16767ed8b19600b274a6eeb745728f95219578adc73712`
