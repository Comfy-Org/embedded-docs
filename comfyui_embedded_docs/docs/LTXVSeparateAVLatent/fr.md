> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/fr.md)

Le nœud LTXVSeparateAVLatent prend une représentation latente audiovisuelle combinée et la divise en deux parties distinctes : l'une pour la vidéo et l'autre pour l'audio. Il sépare les échantillons et, le cas échéant, les masques de bruit du latent d'entrée, créant ainsi deux nouveaux objets latents.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `av_latent` | LATENT | Oui | N/D | La représentation latente audiovisuelle combinée à séparer. |

**Remarque :** Le tenseur `samples` du latent d'entrée doit contenir au moins deux éléments le long de la première dimension (dimension du lot). Le premier élément est utilisé pour le latent vidéo, et le second pour le latent audio. Si un `noise_mask` est présent, il est divisé de la même manière.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `video_latent` | LATENT | La représentation latente contenant les données vidéo séparées. |
| `audio_latent` | LATENT | La représentation latente contenant les données audio séparées. |

---
**Source fingerprint (SHA-256):** `55bce5d768e7fe13f885cc32d34ecdac5cdcbb667b03743004866ea4b6d58d46`
