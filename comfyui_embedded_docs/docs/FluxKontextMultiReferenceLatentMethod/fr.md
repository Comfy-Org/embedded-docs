> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/fr.md)

Voici la traduction en français de la documentation du nœud FluxKontextMultiReferenceLatentMethod :

Le nœud FluxKontextMultiReferenceLatentMethod modifie les données de conditionnement en définissant une méthode spécifique pour les latents de référence. Il ajoute la méthode choisie à l'entrée de conditionnement, ce qui affecte la façon dont les latents de référence sont traités lors des étapes de génération ultérieures. Ce nœud est marqué comme expérimental et fait partie du système de conditionnement Flux.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `conditionnement` | CONDITIONING | Oui | - | Les données de conditionnement à modifier avec la méthode de latents de référence |
| `méthode_des_latents_de_référence` | STRING | Oui | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` | La méthode à utiliser pour le traitement des latents de référence. Si "uxo" ou "uso" est sélectionné, il sera converti en "uxo". Ce paramètre est marqué comme avancé. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `conditionnement` | CONDITIONING | Les données de conditionnement modifiées avec la méthode de latents de référence appliquée |

---
**Source fingerprint (SHA-256):** `9d39a8fee08ae347a745b20b3dc39051ee2f4645392e769247ae32be35491048`
