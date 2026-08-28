# Couleur vers RGB Int

Le nœud **ColorToRGBInt** convertit une couleur donnée au format hexadécimal (comme `#FF5733`) en une valeur entière RVB unique. Il extrait les composantes rouge, verte et bleue de la chaîne de caractères de la couleur, les combine en un entier unique, et renvoie également la représentation hexadécimale d'origine et la valeur alpha (opacité).

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `couleur` | Une valeur de couleur au format hexadécimal `#RRGGBB` ou `#RRGGBBAA`. Doit contenir 7 ou 9 caractères et commencer par `#`. | COLOR | Oui | `#RRGGBB`<br>`#RRGGBBAA` |

**Remarque :** La chaîne `color` d'entrée doit respecter le format `#RRGGBB` ou `#RRGGBBAA`. Si elle ne contient pas 7 ou 9 caractères, ne commence pas par `#`, ou contient des caractères hexadécimaux invalides, le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `rgb_int` | La valeur entière RVB calculée, dérivée de la formule : `(Red * 65536) + (Green * 256) + Blue`. | INT |
| `hex` | La chaîne de caractères hexadécimale au format `#RRGGBB`. Si l'entrée comprenait un canal alpha, celui-ci est supprimé de cette sortie. | COLOR |
| `alpha` | La valeur alpha (opacité) comprise entre 0.0 et 1.0. Égale à 1.0 lorsque l'entrée est `#RRGGBB`, ou à la valeur du canal alpha divisée par 255 lorsque l'entrée est `#RRGGBBAA`. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/fr.md)

---
**Source fingerprint (SHA-256):** `4e64616d168beee73bca4364d47e2a089418b5046a76bfcfa061dfab9a5e49ed`
