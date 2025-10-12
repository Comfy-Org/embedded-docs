> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/fr.md)

Le nœud HunyuanRefinerLatent traite les conditionnements et les entrées latentes pour les opérations de raffinement. Il applique une augmentation de bruit aux conditionnements positifs et négatifs tout en incorporant les données d'image latentes, et génère une nouvelle sortie latente avec des dimensions spécifiques pour un traitement ultérieur.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | L'entrée de conditionnement positive à traiter |
| `negative` | CONDITIONING | Oui | - | L'entrée de conditionnement négative à traiter |
| `latent` | LATENT | Oui | - | L'entrée de représentation latente |
| `noise_augmentation` | FLOAT | Oui | 0.0 - 1.0 | La quantité d'augmentation de bruit à appliquer (par défaut : 0.10) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Le conditionnement positif traité avec l'augmentation de bruit appliquée et la concaténation d'image latente |
| `negative` | CONDITIONING | Le conditionnement négatif traité avec l'augmentation de bruit appliquée et la concaténation d'image latente |
| `latent` | LATENT | Une nouvelle sortie latente avec les dimensions [batch_size, 32, height, width, channels] |
