> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/fr.md)

Le nœud Vidu Text To Video Generation crée des vidéos à partir de descriptions textuelles. Il utilise divers modèles de génération vidéo pour transformer vos descriptions textuelles en contenu vidéo avec des paramètres personnalisables pour la durée, le format d'image et le style visuel.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Oui | `vidu_q1`<br>*Autres options VideoModelName* | Nom du modèle (par défaut : vidu_q1) |
| `prompt` | STRING | Oui | - | Une description textuelle pour la génération vidéo |
| `duration` | INT | Non | 5-5 | Durée de la vidéo de sortie en secondes (par défaut : 5) |
| `seed` | INT | Non | 0-2147483647 | Graine pour la génération vidéo (0 pour aléatoire) (par défaut : 0) |
| `aspect_ratio` | COMBO | Non | `r_16_9`<br>*Autres options AspectRatio* | Le format d'image de la vidéo de sortie (par défaut : r_16_9) |
| `resolution` | COMBO | Non | `r_1080p`<br>*Autres options Resolution* | Les valeurs prises en charge peuvent varier selon le modèle et la durée (par défaut : r_1080p) |
| `movement_amplitude` | COMBO | Non | `auto`<br>*Autres options MovementAmplitude* | L'amplitude du mouvement des objets dans le cadre (par défaut : auto) |

**Note :** Le champ `prompt` est obligatoire et ne peut pas être vide. Le paramètre `duration` est actuellement fixé à 5 secondes.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo générée basée sur la description textuelle |
