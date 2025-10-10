> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | L'entrée de conditionnement positive à modifier avec les informations de timing audio |
| `negative` | CONDITIONING | Oui | - | L'entrée de conditionnement négative à modifier avec les informations de timing audio |
| `seconds_start` | FLOAT | Oui | 0.0 à 1000.0 | Le temps de départ en secondes pour la génération audio (par défaut : 0.0) |
| `seconds_total` | FLOAT | Oui | 0.0 à 1000.0 | La durée totale en secondes pour la génération audio (par défaut : 47.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Le conditionnement positif modifié avec les informations de timing audio appliquées |
| `negative` | CONDITIONING | Le conditionnement négatif modifié avec les informations de timing audio appliquées |