> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/fr.md)

Le nœud AudioEncoderEncode traite les données audio en les encodant à l'aide d'un modèle d'encodeur audio. Il prend une entrée audio et la convertit en une représentation encodée qui peut être utilisée pour un traitement ultérieur dans le pipeline de conditionnement. Ce nœud transforme les formes d'onde audio brutes en un format adapté aux applications d'apprentissage automatique basées sur l'audio.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `audio_encoder` | AUDIO_ENCODER | Requis | - | - | Le modèle d'encodeur audio utilisé pour traiter l'entrée audio |
| `audio` | AUDIO | Requis | - | - | Les données audio contenant les informations de forme d'onde et de taux d'échantillonnage |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | AUDIO_ENCODER_OUTPUT | La représentation audio encodée générée par l'encodeur audio |