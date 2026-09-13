# FluxDisableGuidance

Ce nœud désactive complètement l'embedding de guidage sur les modèles Flux et de type Flux. Il prend en entrée des données de conditionnement et définit leur valeur de guidage sur None, ce qui désactive effectivement le conditionnement basé sur le guidage pour le processus de génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `conditioning` | Données de conditionnement à traiter et dont le guidage doit être retiré | CONDITIONING | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `conditioning` | Données de conditionnement modifiées avec le guidage désactivé | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/fr.md)

---
**Source fingerprint (SHA-256):** `da3286194f9f5e7e49dd7047d6b0a0c97bb2570eaa9281abbd3992a743302fbf`
