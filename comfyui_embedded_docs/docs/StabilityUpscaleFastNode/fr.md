> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleFastNode/fr.md)

Agrandit rapidement une image via un appel API Stability pour la redimensionner à 4 fois sa taille d'origine. Ce nœud est spécifiquement conçu pour agrandir des images de faible qualité ou compressées en les envoyant au service d'agrandissement rapide de Stability AI.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à agrandir |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | IMAGE | L'image agrandie renvoyée par l'API Stability AI |
