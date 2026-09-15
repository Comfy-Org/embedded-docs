# Canny

Extraire toutes les lignes de contour des photos, comme si vous utilisiez un stylo pour détourer une photo, en traçant les contours et les limites de détail des objets.

## Principe de fonctionnement

Imaginez que vous êtes un artiste qui doit utiliser un stylo pour détourer une photo. Le nœud Canny agit comme un assistant intelligent, vous aidant à décider où tracer des lignes (contours) et où ne pas en tracer.

Ce processus ressemble à un travail de filtrage :

- **Seuil élevé** est la « norme de ligne à tracer obligatoirement » : seules les lignes de contour très évidentes et nettes seront tracées, comme les contours du visage des personnes et les contours des bâtiments
- **Seuil faible** est la « norme de ligne à ne surtout pas tracer » : les contours trop faibles seront ignorés afin d'éviter de dessiner du bruit et des lignes sans signification
- **Zone intermédiaire** : les contours situés entre les deux seuils seront tracés s'ils sont reliés à des « lignes à tracer obligatoirement », mais ne seront pas tracés s'ils sont isolés

Le résultat final est une image en noir et blanc, où les parties blanches sont les lignes de contour détectées et les parties noires sont les zones sans contour.

## Entrées

| Nom du paramètre | Description de la fonction | Type de données | Type d'entrée | Valeur par défaut | Plage |
| --- | --- | --- | --- | --- | --- |
| `image` | Photo originale nécessitant l'extraction des contours | IMAGE | Entrée | - | - |
| `seuil_bas` | Seuil faible, détermine quels contours trop faibles ignorer. Des valeurs plus basses préservent davantage de détails mais peuvent produire du bruit | FLOAT | Widget | 0.4 | 0.01-0.99 |
| `seuil_haut` | Seuil élevé, détermine quels contours forts préserver. Des valeurs plus élevées ne conservent que les lignes de contour les plus évidentes | FLOAT | Widget | 0.8 | 0.01-0.99 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | Image de contours en noir et blanc, les lignes blanches sont les contours détectés, les zones noires sont les parties sans contour | IMAGE |

## Comparaison des paramètres

![Image originale](./asset/input.webp)

![Comparaison des paramètres](./asset/compare.webp)

**Problèmes courants :**

- Contours brisés : essayez d'abaisser le seuil élevé
- Trop de bruit : augmentez le seuil faible
- Détails importants manquants : abaissez le seuil faible
- Contours trop grossiers : vérifiez la qualité et la résolution de l'image d'entrée

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Canny/fr.md)
