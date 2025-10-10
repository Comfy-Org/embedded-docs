> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioMerge/fr.md)

Le nœud AudioMerge combine deux pistes audio en superposant leurs formes d'onde. Il aligne automatiquement les taux d'échantillonnage des deux entrées audio et ajuste leurs durées pour qu'elles soient égales avant la fusion. Le nœud propose plusieurs méthodes mathématiques pour combiner les signaux audio et garantit que la sortie reste dans des niveaux de volume acceptables.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `audio1` | AUDIO | requis | - | - | Première entrée audio à fusionner |
| `audio2` | AUDIO | requis | - | - | Seconde entrée audio à fusionner |
| `merge_method` | COMBO | requis | - | ["add", "mean", "subtract", "multiply"] | La méthode utilisée pour combiner les formes d'onde audio. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | La sortie audio fusionnée contenant la forme d'onde combinée et le taux d'échantillonnage |