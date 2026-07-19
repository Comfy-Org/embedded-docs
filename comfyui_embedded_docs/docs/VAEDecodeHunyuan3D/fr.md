# VAEDecodeHunyuan3D

Le nœud VAEDecodeHunyuan3D convertit des représentations latentes en données voxel 3D à l'aide d'un décodeur VAE. Il traite les échantillons latents via le modèle VAE avec des paramètres configurables de fragmentation et de résolution pour générer des données volumétriques adaptées aux applications 3D.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `échantillons` | La représentation latente à décoder en données voxel 3D | LATENT | Oui | - |
| `vae` | Le modèle VAE utilisé pour décoder les échantillons latents | VAE | Oui | - |
| `nombre_de_morceaux` | Le nombre de fragments pour diviser le traitement afin de gérer la mémoire (par défaut : 8000) | INT | Oui | 1000-500000 |
| `résolution_octree` | La résolution de la structure d'octree utilisée pour la génération de voxels 3D (par défaut : 256) | INT | Oui | 16-512 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `voxels` | Les données voxel 3D générées à partir de la représentation latente décodée | VOXEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/fr.md)

---
**Source fingerprint (SHA-256):** `a53ad8e14a2ffca6278866753046d5959f057a4c3fdba5623b37545cee27d557`
