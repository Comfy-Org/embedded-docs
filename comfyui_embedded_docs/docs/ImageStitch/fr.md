Ce nœud vous permet d'assembler deux images dans une direction spécifiée (haut, bas, gauche, droite), avec prise en charge de l'adaptation des tailles et d'un espacement entre les images.

## Entrées

| Nom du paramètre | Description | Type de données | Type d'entrée | Valeur par défaut | Plage |
| --- | --- | --- | --- | --- | --- |
| `image1` | La première image à assembler | IMAGE | Requise | - | - |
| `image2` | La deuxième image à assembler ; si non fournie, seule la première image est renvoyée | IMAGE | Optionnelle | None | - |
| `direction` | La direction dans laquelle assembler la deuxième image : droite, bas, gauche ou haut | STRING | Requise | right | right/down/left/up |
| `correspondre_taille_image` | Indique s'il faut redimensionner la deuxième image pour qu'elle corresponde aux dimensions de la première image | BOOLEAN | Requis | True | True/False |
| `espacement_largeur` | Largeur de l'espacement entre les images, doit être un nombre pair | INT | Requis | 0 | 0-1024 |
| `espacement_couleur` | Couleur de l'espacement entre les images assemblées | STRING | Requis | white | white/black/red/green/blue |

> Pour `spacing_color`, lors de l'utilisation de couleurs autres que "white/black", si `match_image_size` est défini sur `false`, la zone de remplissage sera remplie de noir

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | L'image assemblée | IMAGE |

## Exemple de Workflow

Dans le workflow ci-dessous, nous utilisons 3 images d'entrée de tailles différentes comme exemples :

- image1 : 500x300
- image2 : 400x250
- image3 : 300x300

![workflow](./asset/workflow.webp)

**Premier nœud d'assemblage d'image**

- `match_image_size` : false, les images seront assemblées à leurs tailles d'origine
- `direction` : up, `image2` sera placée au-dessus de `image1`
- `spacing_width` : 20
- `spacing_color` : black

Image de sortie 1 :

![output1](./asset/output-1.webp)

**Deuxième nœud d'assemblage d'image**

- `match_image_size` : true, la deuxième image sera mise à l'échelle pour correspondre à la hauteur ou à la largeur de la première image
- `direction` : right, `image3` apparaîtra sur le côté droit
- `spacing_width` : 20
- `spacing_color` : white

Image de sortie 2 :

![output2](./asset/output-2.webp)

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageStitch/fr.md)
