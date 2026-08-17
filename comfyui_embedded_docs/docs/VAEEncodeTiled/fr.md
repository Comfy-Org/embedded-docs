# VAE Encode (Tiled)

Le nœud VAEEncodeTiled traite les images en les découpant en petites tuiles et en les encodant à l'aide d'un autoencodeur variationnel. Cette approche par tuiles permet de gérer de grandes images qui pourraient autrement dépasser les limites de mémoire. Le nœud prend en charge à la fois les VAE d'image et de vidéo, avec des contrôles de tuilage distincts pour les dimensions spatiales et temporelles.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `pixels` | Les données d'image d'entrée à encoder | IMAGE | Oui | - |
| `vae` | Le modèle d'autoencodeur variationnel utilisé pour l'encodage | VAE | Oui | - |
| `tile_size` | La taille de chaque tuile pour le traitement spatial (par défaut : 512) | INT | Oui | 64-4096 (pas : 64) |
| `overlap` | La quantité de chevauchement entre les tuiles adjacentes (par défaut : 64) | INT | Oui | 0-4096 (pas : 32) |
| `temporal_size` | Utilisé uniquement pour les VAE vidéo : nombre d'images à encoder à la fois (par défaut : 64) | INT | Oui | 8-4096 (pas : 4) |
| `temporal_overlap` | Utilisé uniquement pour les VAE vidéo : nombre d'images à chevaucher (par défaut : 8) | INT | Oui | 4-4096 (pas : 4) |

**Remarque :** Les paramètres `temporal_size` et `temporal_overlap` ne sont pertinents que lors de l'utilisation de VAE vidéo et n'ont aucun effet sur les VAE d'image standard.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | La représentation latente encodée de l'image d'entrée | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/fr.md)

---
**Source fingerprint (SHA-256):** `c36b02f8eeed5c72f9efa2392e2013e89be7644c022d987d413d4da088dfbaad`
