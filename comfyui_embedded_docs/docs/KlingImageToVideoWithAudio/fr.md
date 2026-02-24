> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageToVideoWithAudio/fr.md)

## Entrées

| Paramètre | Type de données | Obligatoire | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Oui | `"kling-v2-6"` | La version spécifique du modèle Kling AI à utiliser pour la génération de vidéo. |
| `start_frame` | IMAGE | Oui | - | L'image qui servira de première image de la vidéo générée. L'image doit faire au moins 300x300 pixels et avoir un rapport d'aspect compris entre 1:2,5 et 2,5:1. |
| `prompt` | STRING | Oui | - | Prompt textuel positif. Il décrit le contenu vidéo que vous souhaitez générer. Le prompt doit contenir entre 1 et 2500 caractères. |
| `mode` | COMBO | Oui | `"pro"` | Le mode opérationnel pour la génération de la vidéo. |
| `duration` | COMBO | Oui | `5`<br>`10` | La durée de la vidéo à générer, en secondes. |
| `generate_audio` | BOOLEAN | Non | - | Lorsqu'il est activé, le nœud générera un audio pour accompagner la vidéo. Lorsqu'il est désactivé, la vidéo sera silencieuse. (par défaut : True) |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `video` | VIDEO | Le fichier vidéo généré, qui peut inclure de l'audio selon l'entrée `generate_audio`. |
