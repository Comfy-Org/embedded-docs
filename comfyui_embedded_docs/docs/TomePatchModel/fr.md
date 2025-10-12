> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/fr.md)

Le nœud TomePatchModel applique la fusion de tokens (ToMe) à un modèle de diffusion pour réduire les exigences computationnelles lors de l'inférence. Il fonctionne en fusionnant sélectivement les tokens similaires dans le mécanisme d'attention, permettant au modèle de traiter moins de tokens tout en maintenant la qualité de l'image. Cette technique aide à accélérer la génération sans perte de qualité significative.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle de diffusion auquel appliquer la fusion de tokens |
| `ratio` | FLOAT | Non | 0.0 - 1.0 | Le ratio de tokens à fusionner (par défaut : 0.3) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `modèle` | MODEL | Le modèle modifié avec la fusion de tokens appliquée |
