# Méthode latente multi-référence FluxKontext

Le nœud FluxKontextMultiReferenceLatentMethod met à jour les données de conditionnement en y stockant une méthode de latents de référence choisie. La méthode stockée est ensuite utilisée lorsque les latents de référence sont traités lors des étapes de génération ultérieures. Ce nœud est marqué comme expérimental et appartient au système de conditionnement Flux.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `conditionnement` | Les données de conditionnement à modifier avec la méthode de latents de référence | CONDITIONING | Oui | - |
| `méthode_des_latents_de_référence` | La méthode utilisée pour le traitement des latents de référence. Si une valeur contenant "uxo" ou "uso" est sélectionnée, elle est convertie en "uxo" avant d'être stockée. Ce paramètre est marqué comme avancé. | COMBO | Oui | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"`<br>`"index_timestep_zero_isolated"`<br>`"index_timestep_zero_text_start"` |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `conditioning` | Les données de conditionnement modifiées avec la méthode de latents de référence appliquée | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/fr.md)

---
**Source fingerprint (SHA-256):** `de2e3d34f9e47a90ff37300489bffef8082eb92deefbc2ce338b17b0d853ac77`
