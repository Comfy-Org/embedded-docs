> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/fr.md)

Ce nœud utilise le modèle Kling AI pour générer une vidéo à partir d'une description textuelle. Il envoie votre prompt à une API distante et retourne la vidéo générée. Le nœud vous permet de contrôler la durée, le format et la qualité de la vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Oui | `"kling-video-o1"` | Le modèle Kling spécifique à utiliser pour la génération de vidéo. |
| `prompt` | STRING | Oui | 1 à 2500 caractères | Un prompt textuel décrivant le contenu de la vidéo. Il peut inclure à la fois des descriptions positives et négatives. |
| `aspect_ratio` | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Le format ou les dimensions de la vidéo à générer. |
| `duration` | COMBO | Oui | `5`<br>`10` | La durée de la vidéo en secondes. |
| `resolution` | COMBO | Non | `"1080p"`<br>`"720p"` | La qualité ou la résolution en pixels de la vidéo (par défaut : `"1080p"`). |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo générée sur la base du prompt textuel fourni. |
