# MiniMax H3 Latent Upscale With Model

MiniMax H3 Latent Upscale With Model redimensionne la partie vidéo d’un latent MiniMax H3 vers une largeur et une hauteur cibles à l’aide d’un modèle d’upscaling latent. Le latent audio est conservé intact, de sorte que le clip garde son son et qu’aucun rééchantillonnage n’est nécessaire. Utilisez-le après l’échantillonnage MiniMax H3 et avant le décodage VAE H3 lorsque le clip doit être produit dans une taille plus grande.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle d’upscaling latent, généralement chargé avec Load Latent Upscale Model. Il doit s’agir d’un upscaler latent à convolution 3D MiniMax H3. | LATENT_UPSCALE_MODEL | Oui | - |
| `samples` | Latent MiniMax H3 à redimensionner. Un latent imbriqué conserve sa partie audio telle quelle. | LATENT | Oui | - |
| `width` | Largeur vidéo cible en pixels. Le latent est redimensionné à `width / 16` colonnes, la valeur est donc arrondie vers le bas au multiple de 16 inférieur. (par défaut : 2560) | INT | Oui | 32 à 16384 (pas de 32) |
| `height` | Hauteur vidéo cible en pixels, également arrondie vers le bas au multiple de 16 inférieur. (par défaut : 1440) | INT | Oui | 32 à 16384 (pas de 32) |

Lorsque la taille demandée correspond déjà au latent, le latent d’entrée est renvoyé inchangé. Le latent redimensionné ne porte pas de `noise_mask` : un latent partiellement masqué perd alors son masque. Le réseau exécute ses convolutions 3D par tranches temporelles, ce qui maintient l’utilisation mémoire sur les longs clips proche de celle d’une seule tranche.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `LATENT` | Le latent redimensionné, prêt pour le décodage VAE H3. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3LatentUpscaleWithModel/fr.md)

---
**Source fingerprint (SHA-256):** `cd659baace5a21620033dd3470b854cccbada01d09545a2f61273b949c3a004b`
