> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/fr.md)

Voici la traduction en français de la documentation technique du nœud ComfyUI :

---

## Aperçu

Ce nœud prépare une configuration de génération image-vers-vidéo pour les modèles vidéo AR (Auto-Régressifs). Il prend une image de départ, l'encode dans l'espace latent à l'aide d'un VAE, puis stocke l'image encodée dans la configuration du modèle. Cela permet au processus d'échantillonnage vidéo d'utiliser l'image comme première image, amorçant ainsi la génération sans nécessiter une architecture de modèle image-vers-vidéo distincte.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle vidéo AR à utiliser pour la génération. |
| `vae` | VAE | Oui | - | Le modèle VAE utilisé pour encoder l'image de départ dans l'espace latent. |
| `image_de_départ` | IMAGE | Oui | - | L'image initiale qui servira de première image à la vidéo générée. |
| `largeur` | INT | Oui | 16 à 8192 (pas : 16) | La largeur des images vidéo générées (par défaut : 832). |
| `hauteur` | INT | Oui | 16 à 8192 (pas : 16) | La hauteur des images vidéo générées (par défaut : 480). |
| `longueur` | INT | Oui | 1 à 1024 (pas : 4) | Le nombre total d'images dans la vidéo générée (par défaut : 81). |
| `taille_du_lot` | INT | Oui | 1 à 64 | Le nombre de séquences vidéo à générer en un seul lot (par défaut : 1). |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `MODEL` | MODEL | Le modèle cloné avec l'image de départ encodée stockée dans sa configuration pour la génération vidéo. |
| `LATENT` | LATENT | Un tenseur latent vide avec les dimensions correctes pour le processus de génération vidéo. |

---
**Source fingerprint (SHA-256):** `0445b279ba49fa946050cfa70d1e6b13240eaa600b99dfe63f27c3203dc4b61b`
