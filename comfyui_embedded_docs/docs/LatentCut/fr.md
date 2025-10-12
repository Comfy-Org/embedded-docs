> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/fr.md)

Le nœud LatentCut extrait une section spécifique des échantillons latents le long d'une dimension choisie. Il vous permet de découper une partie de la représentation latente en spécifiant la dimension (x, y ou t), la position de départ et la quantité à extraire. Le nœud gère à la fois l'indexation positive et négative et ajuste automatiquement la quantité d'extraction pour rester dans les limites disponibles.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Oui | - | Les échantillons latents d'entrée à partir desquels extraire |
| `dim` | COMBO | Oui | "x"<br>"y"<br>"t" | La dimension le long de laquelle couper les échantillons latents |
| `index` | INT | Non | -16384 à 16384 | La position de départ pour la coupe (par défaut : 0). Les valeurs positives comptent depuis le début, les valeurs négatives comptent depuis la fin |
| `amount` | INT | Non | 1 à 16384 | Le nombre d'éléments à extraire le long de la dimension spécifiée (par défaut : 1) |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | LATENT | La partie extraite des échantillons latents |
