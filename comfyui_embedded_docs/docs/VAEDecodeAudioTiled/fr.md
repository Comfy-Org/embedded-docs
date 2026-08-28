# Décoder Audio VAE (par tuiles)

Ce nœud convertit une représentation audio compressée (échantillons latents) en une forme d'onde audio à l'aide d'un autoencodeur variationnel (VAE). Il traite les données en sections plus petites et chevauchantes (tuiles) afin de gérer l'utilisation de la mémoire, ce qui le rend adapté au traitement de séquences audio plus longues. L'audio décodé est également normalisé pour maintenir un niveau de volume cohérent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `échantillons` | La représentation latente compressée de l'audio à décoder. | LATENT | Oui | N/A |
| `vae` | Le modèle d'autoencodeur variationnel utilisé pour effectuer le décodage. | VAE | Oui | N/A |
| `taille de tuile` | La taille de chaque tuile de traitement. L'audio est décodé en sections de cette longueur pour économiser la mémoire (par défaut : 512). | INT | Oui | 32 à 8192 |
| `chevauchement` | Le nombre d'échantillons que les tuiles adjacentes se chevauchent. Cela contribue à réduire les artefacts aux frontières entre les tuiles (par défaut : 64). | INT | Oui | 0 à 1024 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La forme d'onde audio décodée, y compris les informations sur sa fréquence d'échantillonnage. | AUDIO |

La fréquence d'échantillonnage de sortie provient de l'entrée `samples` si celle-ci en contient une ; sinon, elle est lue à partir du modèle VAE (par défaut, 44100 Hz).

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudioTiled/fr.md)

---
**Source fingerprint (SHA-256):** `5ddedf218ba27ab9f463646c1e5288091172f2d7fae8f2980bb2b5e4d3dca89c`
