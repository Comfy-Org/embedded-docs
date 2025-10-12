> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/fr.md)

Le nœud SaveAudio enregistre les données audio dans un fichier au format FLAC. Il prend une entrée audio et l'écrit dans le répertoire de sortie spécifié avec le préfixe de nom de fichier donné. Le nœud gère automatiquement la dénomination des fichiers et garantit que l'audio est correctement enregistré pour une utilisation ultérieure.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Oui | - | Les données audio à enregistrer |
| `filename_prefix` | STRING | Non | - | Le préfixe pour le nom de fichier de sortie (par défaut : "audio/ComfyUI") |

*Note : Les paramètres `prompt` et `extra_pnginfo` sont cachés et gérés automatiquement par le système.*

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| *Aucune* | - | Ce nœud ne retourne aucune donnée de sortie mais enregistre le fichier audio dans le répertoire de sortie |