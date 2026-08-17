# Séparer le latent AV

Le nœud `LTXVSeparateAVLatent` prend une représentation latente audio-visuelle combinée et la sépare en deux latents distincts : un pour la vidéo et un pour l'audio. Il fonctionne avec tout modèle audio-visuel, tel que LTXV ou MiniMax H3.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `av_latent` | La représentation latente audio-visuelle combinée à séparer. | LATENT | Oui | N/A |

**Remarque :** Le tenseur `samples` du latent d'entrée doit avoir au moins deux éléments le long de la première dimension (dimension du lot). Le premier élément est utilisé pour le latent vidéo, et le second pour le latent audio. Si un `noise_mask` est présent, il est divisé de la même manière.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video_latent` | La représentation latente contenant les données vidéo séparées. | LATENT |
| `audio_latent` | La représentation latente contenant les données audio séparées. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/fr.md)

---
**Source fingerprint (SHA-256):** `22ed38bbc1b5716cee380c35c50455810f79c273f51bbe6a535c9ae33192afe6`
