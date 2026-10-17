# Get Image/Video Latent Size

Lit un latent d'image ou de vidéo et renvoie sa largeur, sa hauteur, son nombre de frames et sa taille de lot, afin que la géométrie puisse être réutilisée sans décoder le latent. Utilisez-le pour dimensionner les masques de bruit, aligner les résolutions ou déterminer les chevauchements lors du tuilage d'un sampler. Les valeurs mesurées sont également imprimées sur le nœud lui-même.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `latent` | Le latent d'image ou de vidéo à inspecter. Lorsque le latent contient plusieurs flux, c'est le premier qui est mesuré. | LATENT | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `width` | La largeur du latent, en cellules latentes plutôt qu'en pixels. | INT |
| `height` | La hauteur du latent, en cellules latentes plutôt qu'en pixels. | INT |
| `frames` | Le nombre de frames dans le latent. Les latents d'image n'ont qu'une seule frame. | INT |
| `batch_size` | Le nombre de latents dans le lot. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetLatentSize/fr.md)

---
**Source fingerprint (SHA-256):** `f75b3347cb1853b035b0bb283d5487ab1532d561d66d3cae3c67f54bf693d31a`
