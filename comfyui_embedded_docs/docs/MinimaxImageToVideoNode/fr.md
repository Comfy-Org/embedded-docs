> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxImageToVideoNode/fr.md)

Génère des vidéos de manière synchrone à partir d'une image et d'une description textuelle, avec des paramètres optionnels utilisant l'API de MiniMax. Ce nœud prend une image d'entrée et une description textuelle pour créer une séquence vidéo, avec diverses options de modèles et paramètres de configuration disponibles.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | Image à utiliser comme première frame de la génération vidéo |
| `texte d'invite` | STRING | Oui | - | Description textuelle pour guider la génération de la vidéo (par défaut : chaîne vide) |
| `modèle` | COMBO | Oui | "I2V-01-Director"<br>"I2V-01"<br>"I2V-01-live" | Modèle à utiliser pour la génération vidéo (par défaut : "I2V-01") |
| `graine` | INT | Non | 0 à 18446744073709551615 | La graine aléatoire utilisée pour créer le bruit (par défaut : 0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo générée en sortie |