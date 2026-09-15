# VAEEncodeAudio

Le nœud VAE Encode Audio convertit les données audio en une représentation latente à l'aide d'un autoencodeur variationnel (VAE). Il traite l'audio entrant via le VAE pour produire des échantillons latents compressés pouvant être utilisés pour d'autres tâches de génération ou de manipulation audio. Si la fréquence d'échantillonnage de l'audio diffère de celle attendue par le VAE, l'audio est automatiquement rééchantillonné avant l'encodage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio` | Données audio à encoder, contenant les informations de forme d'onde et de fréquence d'échantillonnage | AUDIO | Oui | - |
| `vae` | Modèle d'autoencodeur variationnel utilisé pour encoder l'audio dans l'espace latent | VAE | Oui | - |

**Remarque :** L'entrée audio est automatiquement rééchantillonnée pour correspondre à la fréquence d'échantillonnage attendue par le VAE (par défaut : 44100 Hz) si la fréquence d'échantillonnage d'origine diffère de cette valeur. Si l'audio d'entrée est None (par exemple, lorsque la vidéo source ne contient pas de piste audio), le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | Représentation audio encodée dans l'espace latent, contenant des échantillons compressés | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeAudio/fr.md)

---
**Source fingerprint (SHA-256):** `224563af40a377a37209b26ec8becf035560da273b18293634f684e18c5e63ed`
