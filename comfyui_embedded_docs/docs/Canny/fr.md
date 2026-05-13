> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Canny/fr.md)

Extrayez toutes les lignes de contour des photos, comme si vous traciez le contour d'une photo avec un stylo, en dessinant les limites des objets et les détails de leurs contours.

## Principe de fonctionnement

Imaginez que vous êtes un artiste devant tracer le contour d'une photo avec un stylo. Le nœud Canny agit comme un assistant intelligent, vous aidant à décider où tracer des lignes (contours) et où ne pas en tracer.

Ce processus s'apparente à un travail de filtrage :

- **Seuil haut** correspond à la « norme de tracé obligatoire » : seules les lignes de contour très évidentes et nettes seront tracées, comme les contours du visage d'une personne ou les structures d'un bâtiment.
- **Seuil bas** correspond à la « norme de non-tracé absolu » : les contours trop faibles seront ignorés pour éviter de tracer du bruit et des lignes sans signification.
- **Zone intermédiaire** : les contours situés entre les deux seuils seront tracés ensemble s'ils sont connectés à des « lignes de tracé obligatoire », mais ne seront pas tracés s'ils sont isolés.

Le résultat final est une image en noir et blanc, où les parties blanches sont les lignes de contour détectées et les parties noires sont les zones sans contour.

## Entrées

| Nom du paramètre | Type de données | Type d'entrée | Valeur par défaut | Plage      | Description de la fonction |
|------------------|-----------------|---------------|-------------------|------------|----------------------------|
| `image`          | IMAGE           | Entrée        | -                 | -          | Photo originale nécessitant une extraction des contours |
| `low_threshold`  | FLOAT           | Widget        | 0.4               | 0.01-0.99  | Seuil bas, détermine quels contours faibles ignorer. Des valeurs plus basses préservent plus de détails mais peuvent générer du bruit |
| `high_threshold` | FLOAT           | Widget        | 0.8               | 0.01-0.99  | Seuil haut, détermine quels contours forts conserver. Des valeurs plus élevées ne conservent que les lignes de contour les plus évidentes |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `image`       | IMAGE           | Image de contour en noir et blanc, les lignes blanches sont les contours détectés, les zones noires sont les parties sans contour |

## Comparaison des paramètres

![Image originale](./asset/input.webp)

![Comparaison des paramètres](./asset/compare.webp)

**Problèmes courants :**

- Contours brisés : essayez d'abaisser le seuil haut
- Trop de bruit : augmentez le seuil bas
- Détails importants manquants : abaissez le seuil bas
- Contours trop grossiers : vérifiez la qualité et la résolution de l'image d'entrée