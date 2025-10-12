> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageReferenceNode/fr.md)

Le nœud ByteDance Image Reference génère des vidéos en utilisant une invite textuelle et une à quatre images de référence. Il envoie les images et l'invite à un service API externe qui crée une vidéo correspondant à votre description tout en incorporant le style visuel et le contenu de vos images de référence. Le nœud fournit divers contrôles pour la résolution vidéo, le format d'image, la durée et d'autres paramètres de génération.

## Entrées

| Paramètre | Type de Données | Type d'Entrée | Défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seedance_1_lite | seedance_1_lite | Nom du modèle |
| `prompt` | STRING | STRING | - | - | L'invite textuelle utilisée pour générer la vidéo. |
| `images` | IMAGE | IMAGE | - | - | Une à quatre images. |
| `resolution` | STRING | COMBO | - | 480p, 720p | La résolution de la vidéo de sortie. |
| `aspect_ratio` | STRING | COMBO | - | adaptive, 16:9, 4:3, 1:1, 3:4, 9:16, 21:9 | Le format d'image de la vidéo de sortie. |
| `duration` | INT | INT | 5 | 3-12 | La durée de la vidéo de sortie en secondes. |
| `seed` | INT | INT | 0 | 0-2147483647 | Graine à utiliser pour la génération. |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Indique s'il faut ajouter un filigrane "Généré par IA" à la vidéo. |

## Sorties

| Nom de Sortie | Type de Données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré basé sur l'invite d'entrée et les images de référence. |
