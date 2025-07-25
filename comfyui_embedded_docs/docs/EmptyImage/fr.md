## Description de la Fonction

Le nœud EmptyImage est utilisé pour créer des images vides avec des dimensions et des couleurs spécifiées. Il peut générer des images de fond de couleur unie, couramment utilisées comme points de départ ou images de fond pour les flux de travail de traitement d'image.

## Principe de Fonctionnement

Tout comme un peintre prépare une toile vierge avant de commencer à créer, le nœud EmptyImage vous fournit une "toile numérique". Vous pouvez spécifier la taille de la toile (largeur et hauteur), choisir la couleur de base de la toile, et même préparer plusieurs toiles des mêmes spécifications à la fois. Ce nœud est comme une boutique de fournitures d'art intelligente qui peut créer des toiles standardisées qui répondent parfaitement à vos exigences de taille et de couleur.

## Entrées

| Nom du Paramètre | Type de Données | Description |
|------------------|-----------------|-------------|
| `largeur` | INT | Définit la largeur de l'image générée (en pixels), déterminant les dimensions horizontales de la toile |
| `hauteur` | INT | Définit la hauteur de l'image générée (en pixels), déterminant les dimensions verticales de la toile |
| `taille_du_lot` | INT | Le nombre d'images à générer à la fois, utilisé pour la création en lot d'images avec les mêmes spécifications |
| `couleur` | INT | La couleur de fond de l'image. Vous pouvez saisir des paramètres de couleur hexadécimaux, qui seront automatiquement convertis en décimal |

## Sorties

| Nom de Sortie | Type de Données | Description |
|---------------|-----------------|-------------|
| `image` | IMAGE | Le tenseur d'image vide généré, formaté comme [taille_du_lot, hauteur, largeur, 3], contenant trois canaux de couleur RGB |

## Valeurs de Référence de Couleurs Communes

Étant donné que la saisie de couleur actuelle pour ce nœud n'est pas conviviale, avec toutes les valeurs de couleur étant converties en décimal, voici quelques valeurs de couleur communes qui peuvent être utilisées directement pour une application rapide.

| Nom de la Couleur | Valeur Hexadécimale |
|-------------------|---------------------|
| Noir              | 0x000000           |
| Blanc             | 0xFFFFFF           |
| Rouge             | 0xFF0000           |
| Vert              | 0x00FF00           |
| Bleu              | 0x0000FF           |
| Jaune             | 0xFFFF00           |
| Cyan              | 0x00FFFF           |
| Magenta           | 0xFF00FF           |
| Orange            | 0xFF8000           |
| Violet            | 0x8000FF           |
| Rose              | 0xFF80C0           |
| Marron            | 0x8B4513           |
| Gris Foncé        | 0x404040           |
| Gris Clair        | 0xC0C0C0           |
| Bleu Marine       | 0x000080           |
| Vert Foncé        | 0x008000           |
| Rouge Foncé       | 0x800000           |
| Or                | 0xFFD700           |
| Argent            | 0xC0C0C0           |
| Beige             | 0xF5F5DC           |
