# Audio latent vide LTXV

Le nœud LTXV Empty Latent Audio crée un lot de tenseurs latents audio vides (remplis de zéros). Il lit la configuration d'un modèle Audio VAE connecté pour déterminer les dimensions latentes correctes, telles que le nombre de canaux et les bins de fréquence, et calcule combien de latents audio sont nécessaires à partir du nombre de trames et de la fréquence de trames. Le latent vide résultant peut être utilisé comme point de départ pour des flux de travail de génération ou de manipulation audio.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `frames_number` | Nombre de trames. La valeur par défaut est 97. | INT | Oui | 1 à 1000 |
| `frame_rate` | Nombre de trames par seconde. La valeur par défaut est 25.0. Cette entrée accepte des valeurs FLOAT ou INT. | FLOAT | Oui | 1.0 à 1000.0 |
| `batch_size` | Nombre d'échantillons audio latents dans le lot. La valeur par défaut est 1. | INT | Oui | 1 à 4096 |
| `audio_vae` | Modèle Audio VAE à partir duquel récupérer la configuration. Affiché sous le nom « Audio VAE ». | VAE | Oui | N/A |

**Remarque :** L'entrée `audio_vae` est obligatoire. Le nœud génère une erreur si elle n'est pas fournie.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `Latent` | Un tenseur audio latent vide de forme (batch_size, z_channels, num_audio_latents, audio_freq), où le nombre de canaux et les bins de fréquence proviennent de l'Audio VAE et le nombre de latents audio est dérivé de `frames_number` et `frame_rate`. La sortie inclut également un champ `type` défini sur « audio ». | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/fr.md)

---
**Source fingerprint (SHA-256):** `3ac1bf17ebdba7c3a73bdd795f561b7bee31798d8a1efc11b972db1944f873a4`
