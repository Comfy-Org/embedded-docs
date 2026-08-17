# LatentDeRéférence

Ce nœud définit le latent de guidage pour un modèle d'édition. Il prend des données de conditionnement et une entrée latente facultative, puis modifie le conditionnement pour inclure les informations latentes de référence. Si le modèle le prend en charge, vous pouvez chaîner plusieurs nœuds ReferenceLatent pour définir plusieurs images de référence.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `conditioning` | Les données de conditionnement à modifier avec les informations latentes de référence | CONDITIONING | Oui | - |
| `latent` | Données latentes facultatives à utiliser comme référence pour le modèle d'édition | LATENT | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Les données de conditionnement modifiées contenant les informations latentes de référence | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/fr.md)

---
**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`
