# CoupeLatente

Le nœud LatentCut extrait une section spécifique des échantillons latents le long d'une dimension choisie. Il vous permet de découper une partie de la représentation latente en spécifiant la dimension (`x`, `y` ou `t`), la position de départ et la quantité à extraire. Le nœud gère à la fois l'indexation positive et négative et ajuste automatiquement la quantité d'extraction pour rester dans les limites disponibles.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `samples` | Les échantillons latents d'entrée à partir desquels extraire | LATENT | Oui | - |
| `dim` | La dimension le long de laquelle couper les échantillons latents | COMBO | Oui | "x"<br>"y"<br>"t" |
| `index` | La position de départ pour la coupe (par défaut : 0). Les valeurs positives comptent depuis le début, les valeurs négatives depuis la fin. Le nœud limite automatiquement l'index pour rester dans la plage valide des échantillons latents | INT | Oui | -16384 à 16384 |
| `amount` | Le nombre d'éléments à extraire le long de la dimension spécifiée (par défaut : 1). Le nœud réduit automatiquement cette valeur si elle dépasse les données disponibles au-delà de l'index de départ | INT | Oui | 1 à 16384 |

Remarque : `x` coupe le long de la dernière dimension du tenseur latent, `y` le long de l'avant-dernière dimension et `t` le long de la troisième dimension en partant de la fin. Lorsque `index` est positif, il est limité à la dernière position valide de la dimension choisie ; lorsqu'il est négatif, il est limité de manière à ne pas pointer avant le début des données. `amount` est réduit chaque fois que la coupe demandée s'étendrait au-delà des données disponibles.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La partie extraite des échantillons latents | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/fr.md)

---
**Source fingerprint (SHA-256):** `7682de2644a4b85dba0571406f9f9802eca7caab09dc2ccf1ac91dc13b41bcdf`
