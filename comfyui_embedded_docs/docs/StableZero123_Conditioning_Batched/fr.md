# StableZero123_Conditioning_Batched

Le nœud StableZero123_Conditioning_Batched prépare les données de conditionnement nécessaires pour générer des vues 3D d'un objet avec le modèle Stable Zero123. Il encode une image d'entrée avec un modèle de vision CLIP et un VAE, combine les caractéristiques de l'image avec les angles d'élévation et d'azimut de la caméra pour chaque élément d'un lot, et produit un conditionnement positif et négatif ainsi qu'un latent vide. Les entrées d'incrément de lot augmentent ou diminuent l'angle de caméra pour chaque élément consécutif du lot.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip_vision` | Le modèle de vision CLIP utilisé pour encoder l'image d'entrée en embeddings d'image. | CLIP_VISION | Oui | - |
| `init_image` | L'image d'entrée initiale à traiter et à encoder. | IMAGE | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder les pixels de l'image dans l'espace latent. | VAE | Oui | - |
| `width` | Largeur cible de l'image traitée (défaut : 256) | INT | Oui | 16 to MAX_RESOLUTION (step 8) |
| `height` | Hauteur cible de l'image traitée (défaut : 256) | INT | Oui | 16 to MAX_RESOLUTION (step 8) |
| `batch_size` | Nombre d'échantillons de conditionnement à générer dans le lot (défaut : 1) | INT | Oui | 1 to 4096 |
| `elevation` | Angle d'élévation initial de la caméra en degrés (défaut : 0.0) | FLOAT | Oui | -180.0 to 180.0 (step 0.1) |
| `azimuth` | Angle d'azimut initial de la caméra en degrés (défaut : 0.0) | FLOAT | Oui | -180.0 to 180.0 (step 0.1) |
| `elevation_batch_increment` | Valeur ajoutée à l'angle d'élévation pour chaque élément consécutif du lot (défaut : 0.0, paramètre avancé) | FLOAT | Oui | -180.0 to 180.0 (step 0.1) |
| `azimuth_batch_increment` | Valeur ajoutée à l'angle d'azimut pour chaque élément consécutif du lot (défaut : 0.0, paramètre avancé) | FLOAT | Oui | -180.0 to 180.0 (step 0.1) |

**Remarque :** Les valeurs `width` et `height` doivent être des multiples de 8 (le pas de sélection de 8 l'impose), car le nœud les divise par 8 pour construire les dimensions du latent. Pour chaque élément du lot, les valeurs `elevation` et `azimuth` sont augmentées de `elevation_batch_increment` et `azimuth_batch_increment`, de sorte que les éléments consécutifs du lot reçoivent des angles de caméra progressifs.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif combinant les embeddings d'image, les embeddings de caméra et l'image d'entrée encodée utilisée pour la concaténation lors de la génération | CONDITIONING |
| `negative` | Conditionnement négatif utilisant des embeddings d'image initialisés à zéro et un latent zéro pour la concaténation | CONDITIONING |
| `latent` | Latent vide de dimensions (batch_size, 4, height/8, width/8) et contenant les informations d'index de lot | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/fr.md)

---
**Source fingerprint (SHA-256):** `94fc53dace8f294a746c47f8aa0da145f3e7beeb77a95912a38f0037ac094292`
