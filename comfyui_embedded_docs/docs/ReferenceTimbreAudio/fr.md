> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/fr.md)

Ce nœud définit un timbre audio de référence pour une utilisation dans le processus "ace step 1.5". Il fonctionne en prenant une entrée de conditionnement et, éventuellement, une représentation latente de l'audio, puis attache ces données latentes au conditionnement pour une utilisation par les nœuds suivants du workflow.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `conditionnement` | CONDITIONING | Oui | | Les données de conditionnement auxquelles les informations du timbre audio de référence seront attachées. |
| `latent` | LATENT | Non | | Une représentation latente facultative de l'audio de référence. Lorsqu'elle est fournie, ses échantillons sont ajoutés au conditionnement. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `conditionnement` | CONDITIONING | Les données de conditionnement modifiées, contenant désormais les latences du timbre audio de référence si l'entrée facultative `latent` a été fournie. |

---
**Source fingerprint (SHA-256):** `2d39399eb79cfe76b72d01326b89863e2553bc23414b1166d310e5222b215b29`
