# CoupeLatente

Voici la traduction en français de la documentation du nœud LatentCut :

Le nœud LatentCut extrait une section spécifique d'échantillons latents le long d'une dimension choisie. Il permet de découper une partie de la représentation latente en spécifiant la dimension (x, y ou t), la position de départ et la quantité à extraire. Le nœud gère à la fois l'indexation positive et négative et ajuste automatiquement la quantité d'extraction pour rester dans les limites disponibles.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `échantillons` | Les échantillons latents d'entrée à partir desquels extraire | LATENT | Oui | - |
| `dim` | La dimension le long de laquelle couper les échantillons latents | COMBO | Oui | "x"<br>"y"<br>"t" |
| `index` | La position de départ pour la coupe (par défaut : 0). Les valeurs positives comptent à partir du début, les valeurs négatives comptent à partir de la fin. Le nœud limite automatiquement l'index pour rester dans la plage valide des échantillons latents | INT | Oui | -16384 à 16384 |
| `quantité` | Le nombre d'éléments à extraire le long de la dimension spécifiée (par défaut : 1). Le nœud réduit automatiquement cette valeur si elle dépasse les données disponibles au-delà de l'index de départ | INT | Oui | 1 à 16384 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La partie extraite des échantillons latents | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/fr.md)

---
**Source fingerprint (SHA-256):** `54f2b0cead9dce2c2cbd241d4e8c50ce85a67d3e1a40e7002056b83acbf0cf2d`
