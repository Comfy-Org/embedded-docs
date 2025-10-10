> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxSubjectToVideoNode/fr.md)

Génère des vidéos de manière synchrone à partir d'une image et d'une description textuelle, avec des paramètres optionnels, en utilisant l'API de MiniMax. Ce nœud utilise une image de sujet et une description textuelle pour créer une vidéo via le service de génération vidéo de MiniMax.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `subject` | IMAGE | Oui | - | Image du sujet à référencer pour la génération de la vidéo |
| `prompt_text` | STRING | Oui | - | Description textuelle guidant la génération de la vidéo (par défaut : chaîne vide) |
| `model` | COMBO | Non | "S2V-01"<br> | Modèle à utiliser pour la génération de vidéo (par défaut : "S2V-01") |
| `seed` | INT | Non | 0 à 18446744073709551615 | La graine aléatoire utilisée pour créer le bruit (par défaut : 0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo générée basée sur l'image de sujet et la description textuelle en entrée |