# Décodage TripoSplat

Décoder une représentation latente TripoSplat en un splat gaussien 3D. Ce nœud prend le latent échantillonné d'un modèle TripoSplat et le reconstruit en un ensemble de gaussiennes 3D, dont la densité peut être ajustée en modifiant le nombre de gaussiennes produites.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `samples` | Les échantillons latents à décoder. Si les échantillons contiennent un flux caméra imbriqué avec le latent, seul le flux latent est décodé. | LATENT | Oui | - |
| `vae` | Décodeur VAE TripoSplat | VAE | Oui | - |
| `num_gaussians` | Nombre de gaussiennes à produire (arrondi à un multiple de 32). 262144 correspond à la densité de points de l'octree ; une valeur plus élevée suréchantillonne les mêmes points (plus dense, mais aucun nouveau détail) et coûte proportionnellement plus de VRAM/temps. Défaut : 262144 | INT | Oui | 32 à 1048576 (pas : 32) |
| `seed` | Initialise l'échantillonneur de points de l'octree (RNG global) pour des décodages déterministes. Défaut : 0 | INT | Oui | 0 à 18446744073709551615 |

**Remarque :** La valeur de `num_gaussians` est automatiquement limitée à la plage autorisée et arrondie à un multiple du paramètre gaussiennes-par-point du décodeur VAE. Le nombre réellement utilisé peut différer légèrement de la valeur saisie.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `splat` | Le splat gaussien 3D décodé contenant les positions, échelles, rotations, opacités et coefficients d'harmoniques sphériques | SPLAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTripoSplat/fr.md)

---
**Source fingerprint (SHA-256):** `5c2b21cee31c68a6440ab4c7156e0d5c041ce7264f6467a508dc41e2eb0dc598`
