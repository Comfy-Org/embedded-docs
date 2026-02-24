> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoWithAudio/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Oui | `"kling-v2-6"` | Le modèle d'IA spécifique à utiliser pour la génération de vidéo. |
| `prompt` | STRING | Oui | - | Prompt textuel positif. La description utilisée pour générer la vidéo. Doit contenir entre 1 et 2500 caractères. |
| `mode` | COMBO | Oui | `"pro"` | Le mode opérationnel pour la génération de vidéo. |
| `aspect_ratio` | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Le rapport largeur/hauteur souhaité pour la vidéo générée. |
| `duration` | COMBO | Oui | `5`<br>`10` | La durée de la vidéo en secondes. |
| `generate_audio` | BOOLEAN | Non | - | Contrôle si un audio est généré pour la vidéo. Lorsqu'il est activé, l'IA créera un son basé sur le prompt. (par défaut : `True`) |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré. |
