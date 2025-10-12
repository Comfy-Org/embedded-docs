> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxTextToVideoNode/fr.md)

Génère des vidéos de manière synchrone à partir d'une description textuelle et de paramètres optionnels en utilisant l'API de MiniMax. Ce nœud crée du contenu vidéo à partir de descriptions textuelles en se connectant au service de génération de vidéo à partir de texte de MiniMax.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `texte d'invite` | STRING | Oui | - | Description textuelle pour guider la génération de la vidéo |
| `modèle` | COMBO | Non | "T2V-01"<br>"T2V-01-Director" | Modèle à utiliser pour la génération de vidéo (par défaut : "T2V-01") |
| `graine` | INT | Non | 0 à 18446744073709551615 | La graine aléatoire utilisée pour créer le bruit (par défaut : 0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo générée basée sur la description textuelle d'entrée |
