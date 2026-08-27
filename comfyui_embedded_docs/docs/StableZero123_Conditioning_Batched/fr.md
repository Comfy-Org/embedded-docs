# StableZero123_Conditioning_Batched

Le nœud StableZero123_Conditioning_Batched prépare les données de conditionnement pour générer un modèle 3D à partir d'une seule image d'entrée. Il encode l'image avec un modèle de vision CLIP et un VAE, combine les caractéristiques visuelles avec les embeddings de caméra construits à partir des angles d'élévation et d'azimut, et produit un conditionnement positif et négatif ainsi qu'un tenseur latent pour un lot d'échantillons. Lorsque `batch_size` est supérieur à 1, les angles d'élévation et d'azimut sont augmentés de leurs valeurs d'incrément de lot pour chaque élément du lot.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip_vision` | Le modèle de vision CLIP utilisé pour encoder l'image d'entrée | CLIP_VISION | Oui | - |
| `init_image` | L'image d'entrée initiale à traiter et à encoder | IMAGE | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder les pixels de l'image dans l'espace latent | VAE | Oui | - |
| `largeur` | La largeur de sortie de l'image traitée (par défaut : 256) | INT | Oui | 16 à MAX_RESOLUTION (pas de 8) |
| `hauteur` | La hauteur de sortie de l'image traitée (par défaut : 256) | INT | Oui | 16 à MAX_RESOLUTION (pas de 8) |
| `taille_lot` | Le nombre d'échantillons de conditionnement à générer dans le lot (par défaut : 1) | INT | Oui | 1 à 4096 |
| `élévation` | L'angle d'élévation initial de la caméra en degrés (par défaut : 0.0) | FLOAT | Oui | -180.0 à 180.0 |
| `azimut` | L'angle d'azimut initial de la caméra en degrés (par défaut : 0.0) | FLOAT | Oui | -180.0 à 180.0 |
| `incrément_lot_élévation` | La valeur d'incrément de l'élévation pour chaque élément du lot (par défaut : 0.0) | FLOAT | Oui | -180.0 à 180.0 |
| `incrément_lot_azimut` | La valeur d'incrément de l'azimut pour chaque élément du lot (par défaut : 0.0) | FLOAT | Oui | -180.0 à 180.0 |

**Remarque :** Les valeurs `width` et `height` doivent être des multiples de 8, car le nœud divise ces dimensions par 8 en interne lors de la construction du tenseur latent.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positif` | Les données de conditionnement positives contenant les embeddings d'image et les embeddings de caméra pour chaque élément du lot | CONDITIONING |
| `négatif` | Les données de conditionnement négatives avec des embeddings initialisés à zéro | CONDITIONING |
| `latent` | Un tenseur latent initialisé à zéro avec les dimensions batch_size x 4 x height/8 x width/8, ainsi que les informations d'indexation du lot | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/fr.md)

---
**Source fingerprint (SHA-256):** `94fc53dace8f294a746c47f8aa0da145f3e7beeb77a95912a38f0037ac094292`
