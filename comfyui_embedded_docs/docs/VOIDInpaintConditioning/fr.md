> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/fr.md)

Le nœud VOIDInpaintConditioning prépare les données de conditionnement nécessaires à l'infilling (remplissage) avec les modèles CogVideoX. Il prend une vidéo source et un quadmask prétraité, les encode via le VAE, puis les combine en un signal de conditionnement à 32 canaux que le modèle utilise pour remplir les zones masquées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Le conditionnement positif à enrichir avec les informations latentes d'infilling |
| `negative` | CONDITIONING | Oui | - | Le conditionnement négatif à enrichir avec les informations latentes d'infilling |
| `vae` | VAE | Oui | - | Le modèle VAE utilisé pour encoder le masque et la vidéo masquée dans l'espace latent |
| `video` | IMAGE | Oui | - | Images vidéo source [T, H, W, 3] |
| `quadmask` | MASK | Oui | - | Quadmask prétraité provenant de VOIDQuadmaskPreprocess [T, H, W] |
| `width` | INT | Oui | 16 à MAX_RESOLUTION (pas : 8) | Largeur de redimensionnement de la vidéo et du masque (par défaut : 672) |
| `height` | INT | Oui | 16 à MAX_RESOLUTION (pas : 8) | Hauteur de redimensionnement de la vidéo et du masque (par défaut : 384) |
| `length` | INT | Oui | 1 à MAX_RESOLUTION (pas : 1) | Nombre d'images pixels à traiter. Pour CogVideoX-Fun-V1.5 (patch_size_t=2), latent_t doit être pair — les longueurs produisant un latent_t impair sont arrondies à l'inférieur (ex. 49 → 45) (par défaut : 45) |
| `batch_size` | INT | Oui | 1 à 64 | Taille du lot pour le bruit latent de sortie (par défaut : 1) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `positive` | CONDITIONING | Le conditionnement positif avec les informations latentes d'infilling ajoutées |
| `negative` | CONDITIONING | Le conditionnement négatif avec les informations latentes d'infilling ajoutées |
| `latent` | LATENT | Un tenseur de bruit latent rempli de zéros avec la forme [batch_size, 16, latent_t, latent_h, latent_w] |

---
**Source fingerprint (SHA-256):** `a1fe36376d7930286c7a288f261dcf2961d6b13cc412d1a0d42af8a4f9ebeeaf`
