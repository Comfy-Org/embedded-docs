# Créer des boîtes englobantes

Dessinez des boîtes englobantes sur une toile. Génère des éléments d’invite Ideogram, des boîtes englobantes en espace pixel et une image d’aperçu.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `arrière-plan` | Image optionnelle utilisée comme arrière-plan sur la toile et dans l’aperçu. | IMAGE | No | - |
| `bboxes` | Bounding boxes, elements, or a JSON string to initialize the canvas. A new upstream value initializes the canvas; edits made on the canvas take priority and are kept until the upstream value changes again. | BOUNDING_BOX, ARRAY, STRING | No | - |
| `largeur` | Largeur de la toile et de la grille de pixels pour les boîtes englobantes. | INT | Yes | 64 to 16384 (step: 16) |
| `hauteur` | Hauteur de la toile et de la grille de pixels pour les boîtes englobantes. | INT | Yes | 64 to 16384 (step: 16) |
| `état_éditeur` | Dessinez des boîtes englobantes et définissez pour chaque boîte le type, le texte, la description, la palette de couleurs. Commencez par l’élément d’arrière-plan et terminez par le premier plan. | BOUNDING_BOXES | Yes | - |
| `last_incoming` | Internal state managed by the canvas: the upstream bboxes value that last initialized it. Leave empty to re-initialize the canvas from the bboxes input on the next run. | BOUNDING_BOXES | No | - |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `preview` | An RGB image showing the canvas with all bounding boxes rendered, including labels, color palette swatches, and descriptive text. | IMAGE |
| `bboxes` | A list of bounding boxes in pixel coordinates, with each box containing x, y, width, and height values. | BOUNDING_BOX |
| `elements` | A structured array of element objects, each containing type, bounding box coordinates (normalized 0-1000), text (for text type), description, and color palette. | ARRAY |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateBoundingBoxes/fr.md)

---
**Source fingerprint (SHA-256):** `dc5545dffefdccf14f3919ff4d9966dbfd1a497dcd64e1863556d5728659ee94`
