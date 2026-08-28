# Décodage Audio VAE LTXV

Le nœud LTXV Audio VAE Decode convertit une représentation latente de l'audio en une forme d'onde audio. Il utilise un modèle Audio VAE spécialisé pour effectuer ce processus de décodage, produisant une sortie audio avec sa fréquence d'échantillonnage associée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `samples` | Le latent à décoder. | LATENT | Oui | N/A |
| `audio_vae` | Le modèle Audio VAE utilisé pour décoder le latent. | VAE | Oui | N/A |

**Remarque :** Si le latent fourni est imbriqué (contient plusieurs latents), le nœud utilise automatiquement le dernier latent de la séquence pour le décodage.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `Audio` | La forme d'onde audio décodée et sa fréquence d'échantillonnage associée. La forme d'onde est placée sur le même appareil que le latent d'entrée, et la fréquence d'échantillonnage est déterminée par le modèle Audio VAE. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEDecode/fr.md)

---
**Source fingerprint (SHA-256):** `fc94f3cb78ede86ada374444d613411cc9bb5849e5cdb8a24074babee50719b1`
