# Couleur vers RGB Int

Le nœud **ColorToRGBInt** convertit une couleur spécifiée au format hexadécimal (comme `#FF5733`) en une valeur entière RVB unique. Il extrait les composantes rouge, vert et bleu de la chaîne de couleur et les combine en un seul entier, puis renvoie la représentation hexadécimale. Les couleurs avec un canal alpha (`#RRGGBBAA`) sont également prises en charge, et la valeur alpha est renvoyée séparément.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `color` | Une valeur de couleur au format hexadécimal `#RRGGBB` ou `#RRGGBBAA`. Elle doit comporter exactement 7 ou 9 caractères et commencer par `#`. | COLOR | Oui | `#RRGGBB`<br>`#RRGGBBAA` |

**Remarque :** La chaîne d’entrée `color` doit suivre exactement le format `#RRGGBB` ou `#RRGGBBAA`. Si la chaîne ne comporte pas 7 ou 9 caractères, ne commence pas par `#` ou contient des caractères qui ne sont pas des chiffres hexadécimaux valides, le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `rgb_int` | La valeur entière RVB calculée, dérivée de la formule : `(Red * 65536) + (Green * 256) + Blue`. | INT |
| `hex` | La chaîne de couleur hexadécimale au format `#RRGGBB`. Si l’entrée inclut un canal alpha, celui-ci est supprimé de cette sortie. | COLOR |
| `alpha` | La valeur d’alpha (opacité) exprimée par un nombre de 0.0 à 1.0. Pour les couleurs d’entrée avec un canal alpha (`#RRGGBBAA`), il s’agit de la valeur alpha à deux chiffres divisée par 255. Pour les couleurs sans canal alpha, elle est de 1.0. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/fr.md)

---
**Source fingerprint (SHA-256):** `4e64616d168beee73bca4364d47e2a089418b5046a76bfcfa061dfab9a5e49ed`
