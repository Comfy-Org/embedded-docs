> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecordAudio/fr.md)

Le nœud RecordAudio charge les fichiers audio qui ont été enregistrés ou sélectionnés via l'interface d'enregistrement audio. Il traite le fichier audio et le convertit en un format de forme d'onde qui peut être utilisé par d'autres nœuds de traitement audio dans le flux de travail. Le nœud détecte automatiquement la fréquence d'échantillonnage et prépare les données audio pour une manipulation ultérieure.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO_RECORD | Oui | N/A | L'entrée d'enregistrement audio provenant de l'interface d'enregistrement audio |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | Les données audio traitées contenant les informations de forme d'onde et de fréquence d'échantillonnage |