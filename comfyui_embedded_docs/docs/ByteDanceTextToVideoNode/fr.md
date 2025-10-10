> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/fr.md)

Le nœud ByteDance Text to Video génère des vidéos en utilisant les modèles ByteDance via une API basée sur des invites textuelles. Il prend une description textuelle et divers paramètres vidéo en entrée, puis crée une vidéo correspondant aux spécifications fournies. Le nœud gère la communication avec l'API et retourne la vidéo générée en sortie.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | STRING | Combo | seedance_1_pro | Options Text2VideoModelName | Nom du modèle |
| `prompt` | STRING | String | - | - | L'invite textuelle utilisée pour générer la vidéo. |
| `resolution` | STRING | Combo | - | ["480p", "720p", "1080p"] | La résolution de la vidéo de sortie. |
| `aspect_ratio` | STRING | Combo | - | ["16:9", "4:3", "1:1", "3:4", "9:16", "21:9"] | Le rapport d'aspect de la vidéo de sortie. |
| `duration` | INT | Int | 5 | 3-12 | La durée de la vidéo de sortie en secondes. |
| `seed` | INT | Int | 0 | 0-2147483647 | Graine à utiliser pour la génération. (Optionnel) |
| `camera_fixed` | BOOLEAN | Boolean | False | - | Spécifie s'il faut fixer la caméra. La plateforme ajoute une instruction pour fixer la caméra à votre invite, mais ne garantit pas l'effet réel. (Optionnel) |
| `watermark` | BOOLEAN | Boolean | True | - | Indique s'il faut ajouter un filigrane "Généré par IA" à la vidéo. (Optionnel) |

**Contraintes des paramètres :**
- Le paramètre `prompt` doit contenir au moins 1 caractère après suppression des espaces blancs
- Le paramètre `prompt` ne peut pas contenir les paramètres textuels suivants : "resolution", "ratio", "duration", "seed", "camerafixed", "watermark"
- Le paramètre `duration` est limité aux valeurs entre 3 et 12 secondes
- Le paramètre `seed` accepte les valeurs de 0 à 2 147 483 647

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré |