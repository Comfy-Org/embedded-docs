> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/fr.md)

Le nœud FluxKontextMultiReferenceLatentMethod modifie les données de conditionnement en définissant une méthode spécifique pour les latents de référence. Il ajoute la méthode choisie à l'entrée de conditionnement, ce qui affecte la façon dont les latents de référence sont traités dans les étapes de génération suivantes. Ce nœud est marqué comme expérimental et fait partie du système de conditionnement Flux.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | Oui | - | Les données de conditionnement à modifier avec la méthode des latents de référence |
| `reference_latents_method` | STRING | Oui | `"offset"`<br>`"index"`<br>`"uxo/uno"` | La méthode à utiliser pour le traitement des latents de référence. Si "uxo" ou "uso" est sélectionné, cela sera converti en "uxo" |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Les données de conditionnement modifiées avec la méthode des latents de référence appliquée |
