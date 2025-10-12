> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/fr.md)

Le nœud EmptyLatentAudio crée des tenseurs latents vides pour le traitement audio. Il génère une représentation latente audio vierge avec une durée et une taille de lot spécifiées, qui peut être utilisée comme entrée pour des workflows de génération ou de traitement audio. Le nœud calcule les dimensions latentes appropriées en fonction de la durée audio et du taux d'échantillonnage.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `secondes` | FLOAT | Oui | 1.0 - 1000.0 | La durée de l'audio en secondes (par défaut : 47.6) |
| `taille_du_lot` | INT | Oui | 1 - 4096 | Le nombre d'images latentes dans le lot (par défaut : 1) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Retourne un tenseur latent vide pour le traitement audio avec la durée et la taille de lot spécifiées |
