# ReferenceTimbreAudio

Ce nœud définit un timbre audio de référence pour une utilisation dans le processus « ace step 1.5 ». Il prend une entrée de conditionnement et une représentation latente facultative de l'audio, puis attache ces données latentes au conditionnement afin que les nœuds ultérieurs du flux de travail puissent les utiliser comme audio de référence. Si aucune entrée latente n'est fournie, le conditionnement est renvoyé inchangé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `conditioning` | Les données de conditionnement auxquelles les informations de l'audio de référence seront attachées. | CONDITIONING | Oui |  |
| `latent` | Une représentation latente facultative de l'audio de référence. Lorsqu'elle est fournie, ses échantillons sont ajoutés au conditionnement. | LATENT | Non |  |

Lorsque `latent` est fourni, ses échantillons sont ajoutés aux latents de timbre audio de référence du conditionnement. Si aucun `latent` n'est fourni, le conditionnement d'origine est transmis tel quel.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `conditioning` | Les données de conditionnement modifiées, contenant désormais les latents de timbre audio de référence si l'entrée facultative `latent` a été fournie. Si aucun latent n'est fourni, le conditionnement d'origine est renvoyé inchangé. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/fr.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`
