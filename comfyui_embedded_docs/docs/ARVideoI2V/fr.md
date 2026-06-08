Voici la traduction en français de la documentation technique du nœud ComfyUI :

---

## Aperçu

Ce nœud prépare une configuration de génération image-vers-vidéo pour les modèles vidéo AR (Auto-Régressifs). Il prend une image de départ, l'encode dans l'espace latent à l'aide d'un VAE, puis stocke l'image encodée dans la configuration du modèle. Cela permet au processus d'échantillonnage vidéo d'utiliser l'image comme première image, amorçant ainsi la génération sans nécessiter une architecture de modèle image-vers-vidéo distincte.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle vidéo AR à utiliser pour la génération. | MODEL | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder l'image de départ dans l'espace latent. | VAE | Oui | - |
| `image_de_départ` | L'image initiale qui servira de première image à la vidéo générée. | IMAGE | Oui | - |
| `largeur` | La largeur des images vidéo générées (par défaut : 832). | INT | Oui | 16 à 8192 (pas : 16) |
| `hauteur` | La hauteur des images vidéo générées (par défaut : 480). | INT | Oui | 16 à 8192 (pas : 16) |
| `longueur` | Le nombre total d'images dans la vidéo générée (par défaut : 81). | INT | Oui | 1 à 1024 (pas : 4) |
| `taille_du_lot` | Le nombre de séquences vidéo à générer en un seul lot (par défaut : 1). | INT | Oui | 1 à 64 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le modèle cloné avec l'image de départ encodée stockée dans sa configuration pour la génération vidéo. | MODEL |
| `LATENT` | Un tenseur latent vide avec les dimensions correctes pour le processus de génération vidéo. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/fr.md)

---
**Source fingerprint (SHA-256):** `0445b279ba49fa946050cfa70d1e6b13240eaa600b99dfe63f27c3203dc4b61b`
