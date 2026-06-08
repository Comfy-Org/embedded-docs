# VAEDecodeTripoSplat

Décode une représentation latente TripoSplat en un splat gaussien 3D. Ce nœud prend l'échantillon latent d'un modèle TripoSplat et le reconstruit sous forme d'un ensemble de gaussiennes 3D, dont la densité peut être ajustée en modifiant le nombre de gaussiennes produites.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `samples` | Les échantillons latents à décoder | LATENT | Oui | - |
| `vae` | Modèle de décodeur VAE TripoSplat | VAE | Oui | - |
| `num_gaussians` | Nombre de gaussiennes à produire (arrondi à un multiple de 32). 262144 correspond à la densité de points de l'octree ; des valeurs plus élevées sur-échantillonnent les mêmes points (plus dense, mais sans nouveau détail) et coûtent proportionnellement plus de VRAM/temps. Défaut : 262144 | INT | Oui | 32 à 1048576 (pas : 32) |
| `seed` | Initialise l'échantillonneur de points de l'octree (RNG global) pour des décodages déterministes. Défaut : 0 | INT | Oui | 0 à 18446744073709551615 |

**Remarque :** La valeur `num_gaussians` est automatiquement arrondie à un multiple du paramètre gaussiennes-par-point du décodeur VAE. Le nombre réel utilisé peut différer légèrement de la valeur saisie.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `splat` | Le splat gaussien 3D décodé contenant les positions, échelles, rotations, opacités et coefficients d'harmoniques sphériques | SPLAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTripoSplat/fr.md)

---
**Source fingerprint (SHA-256):** `60fff70ade38bc820eaea9db26b714daf84a111fb3563477f56f4e8ffa96ff5b`
