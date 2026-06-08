Le nœud **StableZero123_Conditioning_Batched** traite une image d'entrée et génère des données de conditionnement pour la création de modèles 3D. Il encode l'image à l'aide des modèles CLIP vision et VAE, puis crée des embeddings de caméra basés sur les angles d'élévation et d'azimut pour produire un conditionnement positif et négatif, ainsi que des représentations latentes pour le traitement par lots.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip_vision` | Le modèle CLIP vision utilisé pour encoder l'image d'entrée | CLIP_VISION | Oui | - |
| `init_image` | L'image d'entrée initiale à traiter et encoder | IMAGE | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder les pixels de l'image dans l'espace latent | VAE | Oui | - |
| `largeur` | La largeur de sortie pour l'image traitée (par défaut : 256, doit être divisible par 8) | INT | Non | 16 à MAX_RESOLUTION |
| `hauteur` | La hauteur de sortie pour l'image traitée (par défaut : 256, doit être divisible par 8) | INT | Non | 16 à MAX_RESOLUTION |
| `taille_lot` | Le nombre d'échantillons de conditionnement à générer dans le lot (par défaut : 1) | INT | Non | 1 à 4096 |
| `élévation` | L'angle d'élévation initial de la caméra en degrés (par défaut : 0.0) | FLOAT | Non | -180.0 à 180.0 |
| `azimut` | L'angle d'azimut initial de la caméra en degrés (par défaut : 0.0) | FLOAT | Non | -180.0 à 180.0 |
| `incrément_lot_élévation` | L'incrément d'élévation pour chaque élément du lot (par défaut : 0.0) | FLOAT | Non | -180.0 à 180.0 |
| `incrément_lot_azimut` | L'incrément d'azimut pour chaque élément du lot (par défaut : 0.0) | FLOAT | Non | -180.0 à 180.0 |

**Remarque :** Les paramètres `width` et `height` doivent être divisibles par 8, car le nœud divise ces dimensions par 8 pour la génération de l'espace latent.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `négatif` | Les données de conditionnement positif contenant les embeddings d'image et les paramètres de caméra | CONDITIONING |
| `latent` | Les données de conditionnement négatif avec des embeddings initialisés à zéro | CONDITIONING |
| `latent` | La représentation latente de l'image traitée avec les informations d'indexation par lot | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/fr.md)

---
**Source fingerprint (SHA-256):** `2b770f7a168a0d3e33da8bfa63383080709fa5d53846dbf6a4374bd1ef1746aa`
