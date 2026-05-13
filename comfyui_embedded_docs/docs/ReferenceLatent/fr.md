> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/fr.md)

Ce nœud définit le latent de référence pour un modèle d'édition. Il prend des données de conditionnement et une entrée latente facultative, puis modifie le conditionnement pour inclure les informations du latent de référence. Si le modèle le prend en charge, vous pouvez chaîner plusieurs nœuds ReferenceLatent pour définir plusieurs images de référence.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `conditionnement` | CONDITIONING | Oui | - | Les données de conditionnement à modifier avec les informations du latent de référence |
| `latent` | LATENT | Non | - | Données latentes facultatives à utiliser comme référence pour le modèle d'édition |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | CONDITIONING | Les données de conditionnement modifiées contenant les informations du latent de référence |

---
**Source fingerprint (SHA-256):** `d233778cfa7d6f057509f93f8445a0bbf151308e430fc50e28577f48cf136b53`
