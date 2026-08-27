# Concaténer le latent AV

Ce nœud fusionne un latent vidéo et un latent audio en un seul latent audio-vidéo (AV) conjoint, prêt pour des modèles AV tels que LTXV ou MiniMax H3. Si l’entrée vidéo est déjà un latent AV, son flux vidéo est conservé et seul le flux audio est remplacé par le latent audio fourni.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `video_latent` | La représentation latente des données vidéo. Lorsqu’elle contient déjà à la fois les flux vidéo et audio, le nœud conserve son flux vidéo et remplace l’audio par celui de `audio_latent`. | LATENT | Oui |  |
| `audio_latent` | La représentation latente des données audio. Sa longueur est ajustée pour correspondre au flux vidéo : l’audio plus long est tronqué, l’audio plus court est complété par des zéros. | LATENT | Oui |  |

**Remarque :** Les échantillons des deux entrées sont combinés comme une paire de flux vidéo et audio dans un tenseur imbriqué. Si l’une des entrées contient un `noise_mask`, la sortie inclut un masque combiné ; un masque manquant est remplacé par un masque de uns dont la forme correspond à celle de ses échantillons. Lorsque l’audio plus court est complété, la zone complétée reste non masquée afin que le modèle puisse la générer. Le nœud génère une erreur si le latent audio ne peut pas être adapté au latent vidéo, par exemple lorsque les deux latents diffèrent sur plus d’une dimension ou lorsqu’ils diffèrent sur les dimensions de lot ou de canaux.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `latent` | Un latent contenant les échantillons vidéo et audio regroupés en deux flux, plus un `noise_mask` combiné lorsqu’au moins une entrée en fournit un. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/fr.md)

---
**Source fingerprint (SHA-256):** `0231f9db2ce73132d8555fbb33f295b68aa68a0c1c54e4a0c5d2e1f67b5611cb`
