> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideo/fr.md)

Le nœud Load Video charge les fichiers vidéo depuis le répertoire d'entrée et les rend disponibles pour le traitement dans le workflow. Il lit les fichiers vidéo depuis le dossier d'entrée désigné et les sort sous forme de données vidéo pouvant être connectées à d'autres nœuds de traitement vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `fichier` | STRING | Oui | Plusieurs options disponibles | Le fichier vidéo à charger depuis le répertoire d'entrée |

**Note :** Les options disponibles pour le paramètre `file` sont dynamiquement peuplées à partir des fichiers vidéo présents dans le répertoire d'entrée. Seuls les fichiers vidéo avec des types de contenu pris en charge sont affichés.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `video` | VIDEO | Les données vidéo chargées qui peuvent être transmises à d'autres nœuds de traitement vidéo |
