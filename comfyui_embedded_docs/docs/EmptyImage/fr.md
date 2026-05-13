> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyImage/fr.md)

Voici la traduction en français de la documentation du nœud EmptyImage :

## Description de la fonction

Le nœud EmptyImage est utilisé pour créer des images vierges avec des dimensions et des couleurs spécifiées. Il peut générer des images d'arrière-plan de couleur unie, couramment utilisées comme points de départ ou images d'arrière-plan pour les workflows de traitement d'image.

## Principe de fonctionnement

Tout comme un peintre prépare une toile vierge avant de commencer à créer, le nœud EmptyImage vous fournit une « toile numérique ». Vous pouvez spécifier la taille de la toile (largeur et hauteur), choisir la couleur de base de la toile, et même préparer plusieurs toiles de mêmes spécifications à la fois. Ce nœud est comme un magasin de fournitures artistiques intelligent qui peut créer des toiles standardisées répondant parfaitement à vos exigences de taille et de couleur.

## Entrées

| Nom du paramètre | Type de données | Description |
|------------------|-----------------|-------------|
| `largeur` | INT | Définit la largeur de l'image générée (en pixels), déterminant les dimensions horizontales de la toile |
| `hauteur` | INT | Définit la hauteur de l'image générée (en pixels), déterminant les dimensions verticales de la toile |
| `taille_du_lot` | INT | Le nombre d'images à générer en une seule fois, utilisé pour la création par lots d'images avec les mêmes spécifications |
| `couleur` | INT | La couleur d'arrière-plan de l'image. Vous pouvez saisir des paramètres de couleur hexadécimaux, qui seront automatiquement convertis en décimal |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `image` | IMAGE | Le tenseur d'image vierge généré, formaté en [batch_size, height, width, 3], contenant les trois canaux de couleur RVB |

## Valeurs de couleur de référence courantes

Étant donné que la saisie de couleur actuelle de ce nœud n'est pas conviviale, toutes les valeurs de couleur étant converties en décimal, voici quelques valeurs de couleur courantes qui peuvent être utilisées directement pour une application rapide.

| Nom de la couleur | Valeur hexadécimale |
|-------------------|---------------------|
| Noir              | 0x000000            |
| Blanc             | 0xFFFFFF            |
| Rouge             | 0xFF0000            |
| Vert              | 0x00FF00            |
| Bleu              | 0x0000FF            |
| Jaune             | 0xFFFF00            |
| Cyan              | 0x00FFFF            |
| Magenta           | 0xFF00FF            |
| Orange            | 0xFF8000            |
| Violet            | 0x8000FF            |
| Rose              | 0xFF80C0            |
| Marron            | 0x8B4513            |
| Gris foncé        | 0x404040            |
| Gris clair        | 0xC0C0C0            |
| Bleu marine       | 0x000080            |
| Vert foncé        | 0x008000            |
| Rouge foncé       | 0x800000            |
| Or                | 0xFFD700            |
| Argent            | 0xC0C0C0            |
| Beige             | 0xF5F5DC            |