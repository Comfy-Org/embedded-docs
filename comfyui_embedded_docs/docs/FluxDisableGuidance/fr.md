# FluxDisableGuidance

Ce nœud désactive complètement la fonctionnalité d'intégration du guidage pour les modèles Flux et similaires à Flux. Il prend des données de conditionnement en entrée, supprime le composant de guidage en le définissant sur `None`, puis renvoie les données de conditionnement modifiées, désactivant ainsi efficacement le conditionnement par guidage pour le processus de génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `conditioning` | Les données de conditionnement à traiter et dont il faut retirer le guidage | CONDITIONING | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `conditioning` | Les données de conditionnement modifiées avec le guidage désactivé | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/fr.md)

---
**Source fingerprint (SHA-256):** `da3286194f9f5e7e49dd7047d6b0a0c97bb2570eaa9281abbd3992a743302fbf`
