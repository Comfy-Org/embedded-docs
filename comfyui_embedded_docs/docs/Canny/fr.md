Extrait toutes les lignes de contour des photos, comme utiliser un stylo pour contourner une photo, en dessinant les contours et les limites de détails des objets.

## Principe de Fonctionnement

Imaginez que vous êtes un artiste qui doit utiliser un stylo pour contourner une photo. Le nœud Canny agit comme un assistant intelligent, vous aidant à décider où dessiner des lignes (contours) et où ne pas le faire.

Ce processus est comme un travail de filtrage :

- **Seuil haut** est le "standard de ligne obligatoire" : seules les lignes de contour très évidentes et claires seront dessinées, comme les contours faciaux des personnes et les cadres de bâtiments
- **Seuil bas** est le "standard de définitivement ne pas dessiner de ligne" : les contours qui sont trop faibles seront ignorés pour éviter de dessiner du bruit et des lignes sans signification
- **Zone intermédiaire** : les contours entre les deux standards seront dessinés ensemble s'ils se connectent aux "lignes obligatoires", mais ne seront pas dessinés s'ils sont isolés

La sortie finale est une image en noir et blanc, où les parties blanches sont les lignes de contour détectées et les parties noires sont les zones sans contours.

## Entrées

| Nom du Paramètre | Type de Données | Méthode d'Entrée | Valeur par Défaut | Plage de Valeurs | Description de Fonction |
|-------------------|----------------|------------------|-------------------|------------------|-------------------------|
| image | IMAGE | Connexion | - | - | Photo originale nécessitant l'extraction de contours |
| seuil_bas | FLOAT | Saisie Manuelle | 0.4 | 0.01-0.99 | Seuil bas, détermine quels contours faibles ignorer. Des valeurs plus faibles préservent plus de détails mais peuvent produire du bruit |
| seuil_haut | FLOAT | Saisie Manuelle | 0.8 | 0.01-0.99 | Seuil haut, détermine quels contours forts préserver. Des valeurs plus élevées ne gardent que les lignes de contour les plus évidentes |

## Résultats de Sortie

| Nom de Sortie | Type de Données | Description |
|---------------|----------------|-------------|
| image | IMAGE | Image de contours en noir et blanc, les lignes blanches sont les contours détectés, les zones noires sont les parties sans contours |

## Comparaison des Paramètres

![Image Originale](./asset/input.webp)

![Comparaison des Paramètres](./asset/compare.webp)

**Problèmes Courants :**

- Contours brisés : Essayez de réduire le seuil haut
- Trop de bruit : Augmentez le seuil bas
- Détails importants manqués : Réduisez le seuil bas
- Contours trop rugueux : Vérifiez la qualité et la résolution de l'image d'entrée
