# Get Audio Latent Size

Lit un latent audio et renvoie sa longueur, son nombre de canaux audio et sa taille de lot, afin que ces valeurs puissent être réutilisées sans décoder l'audio. Utilisez-le pour dimensionner les masques de bruit ou pour faire correspondre les longueurs audio et vidéo avant l'échantillonnage. Les valeurs mesurées sont également affichées sur le nœud lui-même.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `latent` | Le latent audio ou audio/vidéo à inspecter. Lorsque le latent contient plusieurs flux, le flux audio est mesuré. | LATENT | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `length` | La longueur du latent audio, en cellules latentes plutôt qu'en échantillons audio. | INT |
| `audio_channels` | Le nombre de canaux audio. Les latents sans dimension de canal audio indiquent un canal. | INT |
| `batch_size` | Le nombre de latents dans le lot. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetAudioLatentSize/fr.md)

---
**Source fingerprint (SHA-256):** `82bac0636a070d14a8845c3f4a5e73359c1d943ce223be3b93212ef25d44b1a8`
