> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/fr.md)

Le nœud SaveAudioMP3 enregistre les données audio au format MP3. Il prend une entrée audio et l'exporte vers le répertoire de sortie spécifié avec des paramètres personnalisables pour le nom de fichier et la qualité. Le nœud gère automatiquement la dénomination des fichiers et la conversion de format pour créer un fichier MP3 lisible.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Oui | - | Les données audio à enregistrer au format MP3 |
| `filename_prefix` | STRING | Non | - | Le préfixe pour le nom du fichier de sortie (par défaut : "audio/ComfyUI") |
| `quality` | STRING | Non | "V0"<br>"128k"<br>"320k" | Le paramètre de qualité audio pour le fichier MP3 (par défaut : "V0") |
| `prompt` | PROMPT | Non | - | Données de prompt internes (fournies automatiquement par le système) |
| `extra_pnginfo` | EXTRA_PNGINFO | Non | - | Informations PNG supplémentaires (fournies automatiquement par le système) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| *Aucune* | - | Ce nœud ne retourne aucune donnée de sortie, mais enregistre le fichier audio dans le répertoire de sortie |