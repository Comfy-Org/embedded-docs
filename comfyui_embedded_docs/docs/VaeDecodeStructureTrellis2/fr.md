# VaeDecodeStructureTrellis2

Ce nœud convertit les échantillons latents de structure Trellis en une grille de voxels 3D à l'aide du décodeur de structure d'un VAE. Il ne lit que les 8 premiers canaux du latent, reconstruit l'occupation des voxels et ajuste la résolution de sortie à 32 ou 64 selon la demande.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `samples` | La représentation latente de la structure à décoder. Seuls les 8 premiers canaux du latent sont utilisés pour le décodage. | LATENT | Oui | - |
| `vae` | Le VAE dont le décodeur de structure convertit le latent en une grille de voxels. Le décodage est effectué par lots. | VAE | Oui | - |
| `resolution` | La résolution spatiale cible de la grille de voxels de sortie (par défaut : « 32 »). Si la grille décodée a une résolution différente, elle est sous-échantillonnée pour correspondre. | COMBO | Oui | "32"<br>"64" |

Remarque : lorsque la résolution de la grille de voxels décodée diffère de la `resolution` sélectionnée, la grille est sous-échantillonnée à l'aide d'un max pooling 3D jusqu'à la taille demandée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `voxel` | Une grille d'occupation de voxels binaire sous forme de tenseur flottant de forme [batch, depth, height, width]. Les valeurs sont 1,0 pour les voxels occupés et 0,0 pour les voxels vides. | VOXEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeStructureTrellis2/fr.md)

---
**Source fingerprint (SHA-256):** `37764ef7351b3619d4cddb57b11d9a0da24dadeedc0fc0f70d089038d37e03b0`
