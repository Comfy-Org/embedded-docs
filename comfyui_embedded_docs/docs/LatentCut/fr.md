# CoupeLatente

Le nœud LatentCut extrait une section spécifique à partir d'échantillons latents le long d'une dimension choisie. Il découpe une partie de la représentation latente en spécifiant la dimension (x, y ou t), la position de départ et la quantité à extraire. Le nœud prend en charge l'indexation positive et négative et ajuste automatiquement la quantité d'extraction afin qu'elle reste dans les limites disponibles.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `samples` | Les échantillons latents d'entrée à partir desquels extraire | LATENT | Oui | - |
| `dim` | La dimension selon laquelle découper les échantillons latents. "x" coupe le long du dernier axe (généralement la largeur), "y" le long de l'avant-dernier axe (généralement la hauteur), et "t" le long du troisième axe en partant de la fin (généralement les images dans les latents vidéo) | COMBO | Oui | "x"<br>"y"<br>"t" |
| `index` | La position de départ pour la découpe (par défaut : 0). Les valeurs positives comptent depuis le début, les valeurs négatives comptent depuis la fin. Le nœud contraint l'index pour qu'il reste dans la plage valide des échantillons latents | INT | Oui | -16384 à 16384 |
| `amount` | Le nombre d'éléments à extraire le long de la dimension spécifiée (par défaut : 1). Doit être au moins 1. Le nœud réduit automatiquement cette valeur si elle devait dépasser les données disponibles au-delà de l'index de départ | INT | Oui | 1 à 16384 |

Remarque : Les valeurs `index` et `amount` sont ajustées pour correspondre à la taille réelle du latent selon la dimension sélectionnée. Si `index` est supérieur à la taille de la dimension, il est contraint à la dernière position valide. Si `index` est négatif, il est contraint à la taille de la dimension en valeur absolue, et `amount` est limité afin de ne pas dépasser la fin des données.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La portion extraite des échantillons latents | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/fr.md)

---
**Source fingerprint (SHA-256):** `7682de2644a4b85dba0571406f9f9802eca7caab09dc2ccf1ac91dc13b41bcdf`
