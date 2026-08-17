# LTXVImgToVideoInplace

Le nœud **LTXVImgToVideoInplace** conditionne une représentation vidéo latente en encodant une image d'entrée dans ses premières images. Il fonctionne en utilisant un VAE pour encoder l'image dans l'espace latent, puis en remplaçant les premières images des échantillons vidéo latents par cette image encodée. Un masque de bruit est appliqué afin que la force de conditionnement contrôle l'influence de l'image sur ces premières images pendant la génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vae` | Le modèle VAE utilisé pour encoder l'image d'entrée dans l'espace latent. | VAE | Oui | - |
| `image` | L'image d'entrée à encoder et à utiliser pour conditionner le latent vidéo. | IMAGE | Oui | - |
| `latent` | La représentation vidéo latente cible à modifier. | LATENT | Oui | - |
| `strength` | Contrôle la force de conditionnement de l'image encodée sur les premières images latentes. Une valeur de 1,0 conditionne entièrement les premières images, tandis que des valeurs plus faibles appliquent un conditionnement plus léger. (par défaut : 1,0) | FLOAT | Non | 0.0 - 1.0 |
| `bypass` | Contourne le conditionnement. Lorsque cette option est activée, le nœud renvoie le latent d'entrée inchangé. (par défaut : False) | BOOLEAN | Non | - |

**Remarque :** L'`image` sera automatiquement redimensionnée (interpolation bilinéaire) pour correspondre aux dimensions spatiales requises par le `vae` pour l'encodage, en fonction de la largeur et de la hauteur du latent d'entrée. Seuls les 3 premiers canaux de couleur (RGB) de l'image sont utilisés ; tout canal alpha est ignoré.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `latent` | La représentation vidéo latente modifiée. Elle contient les échantillons mis à jour et un `noise_mask` qui applique la force de conditionnement aux premières images. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/fr.md)

---
**Source fingerprint (SHA-256):** `69faa4b2e7b0fedeee531dc5a8809e23a79c9ce03e9760afb865160594fef30d`
