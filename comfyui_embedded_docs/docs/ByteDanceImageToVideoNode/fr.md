> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/fr.md)

Le nœud ByteDance Image to Video génère des vidéos en utilisant les modèles ByteDance via une API à partir d'une image d'entrée et d'une invite textuelle. Il prend une image de départ comme première frame et crée une séquence vidéo qui suit la description fournie. Le nœud offre diverses options de personnalisation pour la résolution vidéo, le format d'image, la durée et d'autres paramètres de génération.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | STRING | COMBO | seedance_1_pro | Options Image2VideoModelName | Nom du modèle |
| `prompt` | STRING | STRING | - | - | L'invite textuelle utilisée pour générer la vidéo. |
| `image` | IMAGE | IMAGE | - | - | Première frame à utiliser pour la vidéo. |
| `resolution` | STRING | COMBO | - | ["480p", "720p", "1080p"] | La résolution de la vidéo de sortie. |
| `aspect_ratio` | STRING | COMBO | - | ["adaptive", "16:9", "4:3", "1:1", "3:4", "9:16", "21:9"] | Le format d'image de la vidéo de sortie. |
| `duration` | INT | INT | 5 | 3-12 | La durée de la vidéo de sortie en secondes. |
| `seed` | INT | INT | 0 | 0-2147483647 | Graine à utiliser pour la génération. |
| `camera_fixed` | BOOLEAN | BOOLEAN | False | - | Spécifie s'il faut fixer la caméra. La plateforme ajoute une instruction pour fixer la caméra à votre invite, mais ne garantit pas l'effet réel. |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Indique s'il faut ajouter un filigrane "Généré par IA" à la vidéo. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré basé sur l'image d'entrée et les paramètres de l'invite. |