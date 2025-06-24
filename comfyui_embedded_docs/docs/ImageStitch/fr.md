Ce nœud vous permet d'assembler deux images dans une direction spécifiée (haut, bas, gauche, droite), avec la possibilité d'ajuster la taille et d'ajouter un espacement entre les images.

## Entrées

| Nom du Paramètre | Type de Données | Type d'Entrée | Valeur par Défaut | Plage | Description |
|-----------------|-----------------|----------------|-------------------|--------|-------------|
| `image1` | IMAGE | Requis | - | - | La première image à assembler |
| `image2` | IMAGE | Optionnel | None | - | La deuxième image à assembler, si non fournie, renvoie uniquement la première image |
| `direction` | STRING | Requis | right | right/down/left/up | La direction pour assembler la deuxième image : right (droite), down (bas), left (gauche), ou up (haut) |
| `match_image_size` | BOOLEAN | Requis | True | True/False | Si la deuxième image doit être redimensionnée pour correspondre aux dimensions de la première image |
| `spacing_width` | INT | Requis | 0 | 0-1024 | Largeur de l'espacement entre les images, doit être un nombre pair |
| `spacing_color` | STRING | Requis | white | white/black/red/green/blue | Couleur de l'espacement entre les images assemblées |

> Pour `spacing_color`, lors de l'utilisation de couleurs autres que "white/black", si `match_image_size` est défini sur `false`, la zone de remplissage sera noire

## Sorties

| Nom de Sortie | Type de Données | Description |
|---------------|-----------------|-------------|
| `IMAGE` | IMAGE | L'image assemblée |

## Exemple de Flux de Travail

Dans le flux de travail ci-dessous, nous utilisons 3 images d'entrée de différentes tailles comme exemples :

- image1: 500x300
- image2: 400x250
- image3: 300x300

![workflow](./asset/workflow.webp)

**Premier Nœud Image Stitch**

- `match_image_size`: false, les images seront assemblées dans leurs tailles d'origine
- `direction`: up, `image2` sera placée au-dessus de `image1`
- `spacing_width`: 20
- `spacing_color`: black

Image de sortie 1 :

![output1](./asset/output-1.webp)

**Deuxième Nœud Image Stitch**

- `match_image_size`: true, la deuxième image sera mise à l'échelle pour correspondre à la hauteur ou la largeur de la première image
- `direction`: right, `image3` apparaîtra sur le côté droit
- `spacing_width`: 20
- `spacing_color`: white

Image de sortie 2 :

![output2](./asset/output-2.webp)
