> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/fr.md)

Le nœud SaveAudioOpus enregistre les données audio dans un fichier au format Opus. Il prend une entrée audio et l'exporte sous forme de fichier Opus compressé avec des paramètres de qualité configurables. Le nœud gère automatiquement la nomination des fichiers et enregistre la sortie dans le répertoire de sortie désigné.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Oui | - | Les données audio à enregistrer au format Opus |
| `filename_prefix` | STRING | Non | - | Le préfixe pour le nom du fichier de sortie (par défaut : "audio/ComfyUI") |
| `quality` | COMBO | Non | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" | Le paramètre de qualité audio pour le fichier Opus (par défaut : "128k") |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| - | - | Ce nœud ne retourne aucune valeur de sortie. Sa fonction principale est d'enregistrer le fichier audio sur le disque. |
