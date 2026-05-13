> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/fr.md)

Voici la traduction en français de la documentation du nœud VAEEncodeTiled :

Le nœud VAEEncodeTiled traite les images en les divisant en tuiles plus petites et en les encodant à l'aide d'un autoencodeur variationnel. Cette approche par tuiles permet de gérer de grandes images qui pourraient autrement dépasser les limites de mémoire. Le nœud prend en charge à la fois les VAE d'image et de vidéo, avec des contrôles de tuilage séparés pour les dimensions spatiales et temporelles.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `pixels` | IMAGE | Oui | - | Les données d'image d'entrée à encoder |
| `vae` | VAE | Oui | - | Le modèle d'autoencodeur variationnel utilisé pour l'encodage |
| `tile_size` | INT | Oui | 64-4096 (pas : 64) | La taille de chaque tuile pour le traitement spatial (par défaut : 512) |
| `overlap` | INT | Oui | 0-4096 (pas : 32) | La quantité de chevauchement entre les tuiles adjacentes (par défaut : 64) |
| `temporal_size` | INT | Oui | 8-4096 (pas : 4) | Utilisé uniquement pour les VAE vidéo : nombre d'images à encoder à la fois (par défaut : 64) |
| `temporal_overlap` | INT | Oui | 4-4096 (pas : 4) | Utilisé uniquement pour les VAE vidéo : nombre d'images à chevaucher (par défaut : 8) |

**Remarque :** Les paramètres `temporal_size` et `temporal_overlap` ne sont pertinents que lors de l'utilisation de VAE vidéo et n'ont aucun effet sur les VAE d'image standard.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `LATENT` | LATENT | La représentation latente encodée de l'image d'entrée |

---
**Source fingerprint (SHA-256):** `87420b96ef9b2d5ef18ecb0339a62b6955151e2a9d2c4390758048c00432939a`
