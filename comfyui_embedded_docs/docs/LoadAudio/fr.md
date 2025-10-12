> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadAudio/fr.md)

Le nœud LoadAudio charge les fichiers audio depuis le répertoire d'entrée et les convertit dans un format pouvant être traité par d'autres nœuds audio dans ComfyUI. Il lit les fichiers audio et extrait à la fois les données de forme d'onde et le taux d'échantillonnage, les rendant disponibles pour les tâches de traitement audio en aval.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Oui | Tous les fichiers audio/vidéo pris en charge dans le répertoire d'entrée | Le fichier audio à charger depuis le répertoire d'entrée |

**Note :** Le nœud n'accepte que les fichiers audio et vidéo présents dans le répertoire d'entrée de ComfyUI. Le fichier doit exister et être accessible pour un chargement réussi.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | Données audio contenant les informations de forme d'onde et de taux d'échantillonnage |
