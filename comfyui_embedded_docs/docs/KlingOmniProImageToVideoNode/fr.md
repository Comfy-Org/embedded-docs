> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageToVideoNode/fr.md)

Ce nœud utilise le modèle Kling AI pour générer une vidéo à partir d'un texte descriptif et jusqu'à sept images de référence. Il permet de contrôler le format, la durée et la résolution de la vidéo. Le nœud envoie la requête à une API externe et renvoie la vidéo générée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Oui | `"kling-video-o1"` | Le modèle Kling spécifique à utiliser pour la génération de vidéo. |
| `prompt` | STRING | Oui | - | Un texte décrivant le contenu de la vidéo. Il peut inclure des descriptions positives et négatives. Le texte est automatiquement normalisé et doit contenir entre 1 et 2500 caractères. |
| `aspect_ratio` | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Le format d'image souhaité pour la vidéo générée. |
| `duration` | INT | Oui | 3 à 10 | La durée de la vidéo en secondes. La valeur peut être ajustée avec un curseur (par défaut : 3). |
| `reference_images` | IMAGE | Oui | - | Jusqu'à 7 images de référence. Chaque image doit mesurer au moins 300x300 pixels et avoir un format d'image compris entre 1:2,5 et 2,5:1. |
| `resolution` | COMBO | Non | `"1080p"`<br>`"720p"` | La résolution de sortie de la vidéo. Ce paramètre est optionnel (par défaut : "1080p"). |

**Note :** L'entrée `reference_images` accepte un maximum de 7 images. Si plus d'images sont fournies, le nœud générera une erreur. Chaque image est validée pour ses dimensions minimales et son format d'image.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré. |
