# Méthode latente multi-référence FluxKontext

Le nœud `FluxKontextMultiReferenceLatentMethod` modifie les données de conditionnement en définissant une méthode spécifique de latents de référence. Il ajoute la méthode choisie à l’entrée de conditionnement, ce qui affecte la manière dont les latents de référence sont traités lors des étapes de génération suivantes. Ce nœud est marqué comme expérimental et fait partie du système de conditionnement Flux.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `conditioning` | Les données de conditionnement à modifier avec la méthode de latents de référence | CONDITIONING | Oui | - |
| `reference_latents_method` | La méthode à utiliser pour le traitement des latents de référence. Si « uxo » ou « uso » est sélectionné, il sera converti en « uxo ». Ce paramètre est marqué comme avancé. | COMBO | Oui | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `conditioning` | Les données de conditionnement modifiées avec la méthode de latents de référence appliquée | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/fr.md)

---
**Source fingerprint (SHA-256):** `cbe069d0c9f8adbf7f8c909b1cd644d9cd3730e934f0e5856213ff06fa8ecc56`
