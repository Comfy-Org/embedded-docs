Le nœud **StableZero123_Conditioning** traite une image d'entrée et des angles de caméra pour générer des données de conditionnement et des représentations latentes destinées à la création de modèles 3D. Il utilise un modèle de vision CLIP pour encoder les caractéristiques de l'image, les combine avec des informations d'encastrement de caméra basées sur les angles d'élévation et d'azimut, et produit un conditionnement positif et négatif ainsi qu'une représentation latente pour les tâches de génération 3D en aval.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip_vision` | Le modèle de vision CLIP utilisé pour encoder les caractéristiques de l'image | CLIP_VISION | Oui | - |
| `init_image` | L'image d'entrée à traiter et encoder | IMAGE | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder les pixels en espace latent | VAE | Oui | - |
| `largeur` | Largeur de sortie pour la représentation latente (par défaut : 256, doit être divisible par 8) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de sortie pour la représentation latente (par défaut : 256, doit être divisible par 8) | INT | Oui | 16 à MAX_RESOLUTION |
| `taille_lot` | Nombre d'échantillons à générer dans le lot (par défaut : 1) | INT | Oui | 1 à 4096 |
| `élévation` | Angle d'élévation de la caméra en degrés (par défaut : 0,0) | FLOAT | Oui | -180,0 à 180,0 |
| `azimut` | Angle d'azimut de la caméra en degrés (par défaut : 0,0) | FLOAT | Oui | -180,0 à 180,0 |

**Remarque :** Les paramètres `width` et `height` doivent être divisibles par 8, car le nœud les divise automatiquement par 8 pour créer les dimensions de la représentation latente.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `négatif` | Données de conditionnement positif combinant les caractéristiques de l'image et les encastrements de caméra | CONDITIONING |
| `latent` | Données de conditionnement négatif avec des caractéristiques initialisées à zéro | CONDITIONING |
| `latent` | Représentation latente avec les dimensions [batch_size, 4, height//8, width//8] | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/fr.md)

---
**Source fingerprint (SHA-256):** `a9d6619c800119c9a619665f322d49ded1478ceb40df56ca5707b31242cb0e47`
