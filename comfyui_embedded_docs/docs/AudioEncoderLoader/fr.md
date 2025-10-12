> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/fr.md)

Le nœud AudioEncoderLoader charge des modèles d'encodeur audio à partir de vos fichiers d'encodeur audio disponibles. Il prend en entrée un nom de fichier d'encodeur audio et retourne un modèle d'encodeur audio chargé qui peut être utilisé pour des tâches de traitement audio dans votre flux de travail.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `audio_encoder_name` | STRING | COMBO | - | Fichiers d'encodeur audio disponibles | Sélectionne le fichier de modèle d'encodeur audio à charger depuis votre dossier audio_encoders |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `audio_encoder` | AUDIO_ENCODER | Retourne le modèle d'encodeur audio chargé pour utilisation dans les flux de travail de traitement audio |
