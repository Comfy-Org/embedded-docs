# ReferenceTimbreAudio

Ce nœud définit l'audio de référence pour le processus « ace step 1.5 ». Il prend une entrée de conditionnement et, éventuellement, une représentation latente de l'audio, puis attache ces données latentes au conditionnement afin que les nœuds suivants puissent les utiliser comme latents de timbre audio de référence. Ce nœud est marqué comme expérimental.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `conditioning` | Les données de conditionnement auxquelles les informations d'audio de référence seront attachées. | CONDITIONING | Oui |  |
| `latent` | Une représentation latente facultative de l'audio de référence (par défaut : None). Lorsqu'elle est fournie, ses échantillons sont ajoutés au conditionnement en tant que latents de timbre audio de référence. | LATENT | Non |  |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `conditioning` | Les données de conditionnement modifiées, contenant désormais les latents de timbre audio de référence si l'entrée facultative `latent` a été fournie. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/fr.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`
