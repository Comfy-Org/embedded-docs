# FluxDisableGuidance

Ce nœud désactive complètement l'intégration du guidage sur les modèles Flux et similaires. Il prend des données de conditionnement en entrée et supprime la composante de guidage en la définissant sur None, désactivant ainsi le conditionnement basé sur le guidage pour le processus de génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `conditionnement` | Les données de conditionnement à traiter et dont le guidage doit être retiré | CONDITIONING | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `conditioning` | Les données de conditionnement modifiées avec le guidage désactivé | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/fr.md)

---
**Source fingerprint (SHA-256):** `da3286194f9f5e7e49dd7047d6b0a0c97bb2570eaa9281abbd3992a743302fbf`
