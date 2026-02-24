> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/fr.md)

## Vue d'ensemble

Le nœud WanMoveConcatTrack combine deux ensembles de données de suivi de mouvement en une seule séquence plus longue. Il fonctionne en joignant les trajectoires de suivi et les masques de visibilité des pistes d'entrée le long de leurs dimensions respectives. Si une seule piste est fournie en entrée, il transmet simplement ces données sans les modifier.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `tracks_1` | TRACKS | Oui | | Le premier ensemble de données de suivi de mouvement à concaténer. |
| `tracks_2` | TRACKS | Non | | Un second ensemble optionnel de données de suivi de mouvement. S'il n'est pas fourni, `tracks_1` est transmis directement à la sortie. |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `tracks` | TRACKS | Les données de suivi de mouvement concaténées, contenant la combinaison des `track_path` et `track_visibility` provenant des entrées. |
