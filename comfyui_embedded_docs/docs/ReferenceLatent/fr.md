# LatentDeRéférence

Ce nœud définit le latent de référence pour un modèle d'édition. Il prend des données de conditionnement et une entrée latente facultative, puis modifie le conditionnement pour inclure les informations du latent de référence. Si le modèle le prend en charge, vous pouvez chaîner plusieurs nœuds ReferenceLatent pour définir plusieurs images de référence.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `conditionnement` | Les données de conditionnement à modifier avec les informations du latent de référence | CONDITIONING | Oui | - |
| `latent` | Données latentes facultatives à utiliser comme référence pour le modèle d'édition | LATENT | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Les données de conditionnement modifiées contenant les informations du latent de référence | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/fr.md)

---
**Source fingerprint (SHA-256):** `d233778cfa7d6f057509f93f8445a0bbf151308e430fc50e28577f48cf136b53`
