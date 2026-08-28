# ARVideoI2V

## Aperçu

Ce nœud prépare une configuration de génération image-vers-vidéo pour les modèles vidéo AR (Autorégressifs) qui utilisent le forçage causal ou l'auto-forçage. Il encode une image de départ dans l'espace latent à l'aide d'un VAE et la stocke dans les options du transformeur du modèle, afin que le processus d'échantillonnage vidéo puisse initialiser le cache KV avant le débruitage. Il utilise le même point de contrôle du modèle texte-vers-vidéo, aucune architecture image-vers-vidéo distincte n'est donc nécessaire.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle vidéo AR à utiliser pour la génération. | MODEL | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder l'image de départ dans l'espace latent. | VAE | Oui | - |
| `image_de_départ` | L'image initiale qui servira de première image de la vidéo générée. Seule la première image du lot d'entrée est utilisée, et seuls ses canaux RVB sont encodés. | IMAGE | Oui | - |
| `largeur` | La largeur des images de la vidéo générée (par défaut : 832). | INT | Oui | 16 à 8192 (pas : 16) |
| `hauteur` | La hauteur des images de la vidéo générée (par défaut : 480). | INT | Oui | 16 à 8192 (pas : 16) |
| `longueur` | Le nombre total d'images dans la vidéo générée (par défaut : 81). | INT | Oui | 1 à 1024 (pas : 4) |
| `taille_du_lot` | Le nombre de séquences vidéo à générer dans un seul lot (par défaut : 1). | INT | Oui | 1 à 64 |

Remarque : L'image de départ est redimensionnée à la `width` et à la `height` spécifiées avant d'être encodée. La dimension temporelle latente est calculée comme `((length - 1) // 4) + 1`, et les dimensions spatiales latentes sont `height / 8` et `width / 8`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le modèle cloné avec l'image de départ encodée stockée dans ses options de transformeur (`ar_config.initial_latent`), que l'échantillonneur utilise pour initialiser le cache KV avant le débruitage. | MODEL |
| `LATENT` | Un tenseur latent rempli de zéros avec la forme `[batch_size, 16, lat_t, height // 8, width // 8]`, où `lat_t = ((length - 1) // 4) + 1`. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/fr.md)

---
**Source fingerprint (SHA-256):** `984834951b9d5a22aef51c85a5019fd8ba58cdb2d6fff235371ed29f316896d8`
