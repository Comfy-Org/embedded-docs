> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/fr.md)

Ce nœud génère une vidéo à l'aide d'une instruction textuelle ainsi que des images de première et dernière frame. Il utilise votre description et les deux images clés pour créer une séquence vidéo complète qui effectue une transition entre elles. Le nœud offre diverses options pour contrôler la résolution, le format, la durée et autres paramètres de génération de la vidéo.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | COMBO | combo | seedance_1_lite | seedance_1_lite | Nom du modèle |
| `prompt` | STRING | string | - | - | L'instruction textuelle utilisée pour générer la vidéo. |
| `first_frame` | IMAGE | image | - | - | Première frame à utiliser pour la vidéo. |
| `last_frame` | IMAGE | image | - | - | Dernière frame à utiliser pour la vidéo. |
| `resolution` | COMBO | combo | - | 480p, 720p, 1080p | La résolution de la vidéo de sortie. |
| `aspect_ratio` | COMBO | combo | - | adaptive, 16:9, 4:3, 1:1, 3:4, 9:16, 21:9 | Le format de la vidéo de sortie. |
| `duration` | INT | slider | 5 | 3-12 | La durée de la vidéo de sortie en secondes. |
| `seed` | INT | number | 0 | 0-2147483647 | Graine à utiliser pour la génération. (optionnel) |
| `camera_fixed` | BOOLEAN | boolean | False | - | Spécifie s'il faut fixer la caméra. La plateforme ajoute une instruction pour fixer la caméra à votre prompt, mais ne garantit pas l'effet réel. (optionnel) |
| `watermark` | BOOLEAN | boolean | True | - | Indique s'il faut ajouter un filigrane "Généré par IA" à la vidéo. (optionnel) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré |