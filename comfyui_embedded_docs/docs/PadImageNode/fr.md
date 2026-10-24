# Pad Image

Ajoutez un remplissage à une image à l'aide d'une couleur unie ou d'une copie en miroir de ses bords. Le remplissage peut être défini en pixels exacts de chaque côté, par un multiplicateur de taille, ou par la plus petite quantité qui rend la largeur et la hauteur divisibles par un nombre, ce qui est pratique avant l'enregistrement ou le pavage. L'image d'origine conserve sa place : les remplissages `left` et `top` sont ajoutés avant elle, et les remplissages `right` et `bottom` après elle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image à remplir. | IMAGE | Oui | - |
| `padding_type` | Quantité de remplissage à ajouter : `"pad dimensions"` pour des quantités exactes par côté, `"pad by multiplier"` pour une taille de sortie relative à l'entrée, ou `"pad to multiple"` pour atteindre le multiple suivant. La sélection d'une option révèle ses paramètres. | DYNAMIC_COMBO | Oui | `"pad dimensions"`<br>`"pad by multiplier"`<br>`"pad to multiple"` |
| `left` | Pixels à ajouter à gauche. Disponible lorsque `padding_type` vaut `"pad dimensions"` (par défaut : 0). | INT | Oui | 0 à 16384 |
| `top` | Pixels à ajouter en haut. Disponible lorsque `padding_type` vaut `"pad dimensions"` (par défaut : 0). | INT | Oui | 0 à 16384 |
| `right` | Pixels à ajouter à droite. Disponible lorsque `padding_type` vaut `"pad dimensions"` (par défaut : 0). | INT | Oui | 0 à 16384 |
| `bottom` | Pixels à ajouter en bas. Disponible lorsque `padding_type` vaut `"pad dimensions"` (par défaut : 0). | INT | Oui | 0 à 16384 |
| `multiplier` | Taille de sortie relative à l'entrée ; par exemple, 1.5 ajoute 25 % de chaque côté. Le remplissage est réparti uniformément entre les côtés opposés. Disponible lorsque `padding_type` vaut `"pad by multiplier"` (par défaut : 1.0). | FLOAT | Oui | 1.0 à 8.0 (pas de 0.01) |
| `multiple` | Ajoute un remplissage pour que la largeur et la hauteur soient divisibles par ce nombre. Le remplissage est réparti uniformément entre les côtés opposés, le pixel supplémentaire allant à droite et en bas. Disponible lorsque `padding_type` vaut `"pad to multiple"` (par défaut : 32). | INT | Oui | 1 à 16384 |
| `padding_style` | Élément utilisé pour remplir la zone de remplissage : `"color"` ou `"mirror image"`. La sélection d'une option révèle ses paramètres. | DYNAMIC_COMBO | Oui | `"color"`<br>`"mirror image"` |
| `color` | Couleur de remplissage de la zone de remplissage ; l'alpha est ignoré. Disponible lorsque `padding_style` vaut `"color"` (par défaut : `"#000000"`). | COLOR | Oui | - |
| `feathering` | Mélange ce nombre de pixels du bord de l'image avec la couleur de remplissage sur les côtés remplis. 0 conserve un bord net. Disponible lorsque `padding_style` vaut `"color"` (par défaut : 0). | INT | Oui | 0 à 16384 |

`"mirror image"` reflète les bords de l'image au lieu de les remplir avec une couleur. Le pixel de bord n'est pas répété et, lorsque le remplissage est plus large ou plus haut que l'image elle-même, l'image mise en miroir se répète pour couvrir le reste. Lorsque tous les montants de remplissage valent 0, l'image d'entrée est renvoyée inchangée.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image remplie, avec la dimension de lot et le nombre de canaux de l'entrée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PadImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `9373cd6aa287befba74374b9b2a6c38b20344b5715e9aaa4cf49282ae930c91d`
