# StableZero123_Conditioning

Le nœud StableZero123_Conditioning traite une image d’entrée et des angles de caméra pour générer des données de conditionnement et des représentations latentes pour la génération de modèles 3D. Il utilise un modèle de vision CLIP pour encoder les caractéristiques de l’image, les combine avec des informations d’intégration de caméra basées sur les angles d’élévation et d’azimut, et produit un conditionnement positif et négatif ainsi qu’une représentation latente pour les tâches de génération 3D en aval.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip_vision` | Le modèle de vision CLIP utilisé pour encoder les caractéristiques de l’image | CLIP_VISION | Oui | - |
| `init_image` | L’image d’entrée à traiter et à encoder | IMAGE | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder les pixels dans l’espace latent | VAE | Oui | - |
| `largeur` | Largeur de sortie pour la représentation latente (par défaut : 256, doit être divisible par 8) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de sortie pour la représentation latente (par défaut : 256, doit être divisible par 8) | INT | Oui | 16 à MAX_RESOLUTION |
| `taille_lot` | Nombre d’échantillons à générer dans le lot (par défaut : 1) | INT | Oui | 1 à 4096 |
| `élévation` | Angle d’élévation de la caméra en degrés (par défaut : 0.0) | FLOAT | Oui | -180.0 à 180.0 |
| `azimut` | Angle d’azimut de la caméra en degrés (par défaut : 0.0) | FLOAT | Oui | -180.0 à 180.0 |

**Remarque :** Les paramètres `width` et `height` doivent être divisibles par 8, car le nœud les divise automatiquement par 8 pour créer les dimensions de la représentation latente.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Données de conditionnement positives combinant les caractéristiques de l’image et les intégrations de caméra, y compris l’image d’entrée encodée par le VAE comme latent à concaténer | CONDITIONING |
| `négatif` | Données de conditionnement négatives avec des caractéristiques initialisées à zéro et un latent initialisé à zéro | CONDITIONING |
| `latent` | Représentation latente initialisée à zéro avec les dimensions [batch_size, 4, height//8, width//8] | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/fr.md)

---
**Source fingerprint (SHA-256):** `a694610c9f22fe0dab3ae02f4aabb33e3de8e5031c82dff5e8ba232c098f4a1d`
