# VOIDWarpedNoise

Génère un bruit corrélé temporellement pour la deuxième passe du processus d'affinement vidéo VOID. Il prend la vidéo de sortie de la passe 1 et déforme le bruit gaussien le long des vecteurs de flux optique, créant un bruit qui se déplace de manière cohérente avec le contenu vidéo. Ce bruit déformé est utilisé comme latent de départ pour la passe 2, ce qui améliore la cohérence temporelle de la sortie finale.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `optical_flow` | Modèle de flux optique provenant d'OpticalFlowLoader (RAFT-large). | OPTICAL_FLOW | Oui | - |
| `video` | Images vidéo de sortie de la passe 1 [T, H, W, 3]. | IMAGE | Oui | - |
| `width` | Largeur du latent de sortie (défaut : 672). | INT | Oui | 16 à MAX_RESOLUTION (step 8) |
| `height` | Hauteur du latent de sortie (défaut : 384). | INT | Oui | 16 à MAX_RESOLUTION (step 8) |
| `length` | Nombre de frames pixel. Arrondi à l'inférieur pour que `latent_t` soit pair (exigence `patch_size_t=2`), par ex. 49 → 45 (défaut : 45). | INT | Oui | 1 à MAX_RESOLUTION (step 1) |
| `batch_size` | Nombre de séquences de bruit identiques à générer (défaut : 1). | INT | Oui | 1 à 64 |

**Note sur le paramètre `length` :** La valeur de `length` est automatiquement arrondie à l'inférieur vers la valeur valide la plus proche qui produit une dimension `latent_t` paire. Cette exigence est imposée par la contrainte `patch_size_t=2` du modèle CogVideoX-Fun-V1.5. Un avertissement est consigné en cas d'arrondi.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `warped_noise` | Un tenseur 5D (B, C, T, H, W) contenant un bruit gaussien déformé par flux optique, prêt à être utilisé comme latent initial dans la passe 2 de VOID. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/fr.md)

---
**Source fingerprint (SHA-256):** `f46b0a73b09a5d2d0bc25676f9571563c6bb8bad8d835e7564ac092c72136107`
