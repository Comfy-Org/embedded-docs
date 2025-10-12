> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/fr.md)

Génère des vidéos basées sur l'invite et la taille de sortie. Ce nœud crée des vidéos de transition entre deux images d'entrée en utilisant l'API PixVerse, vous permettant de spécifier la qualité vidéo, la durée, le style de mouvement et les paramètres de génération.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `première image` | IMAGE | Oui | - | L'image de départ pour la transition vidéo |
| `dernière image` | IMAGE | Oui | - | L'image de fin pour la transition vidéo |
| `prompt` | STRING | Oui | - | Invite pour la génération de la vidéo (par défaut : chaîne vide) |
| `qualité` | COMBO | Oui | Options de qualité disponibles dans l'énumération PixverseQuality<br>Par défaut : res_540p | Paramètre de qualité vidéo |
| `durée (secondes)` | COMBO | Oui | Options de durée disponibles dans l'énumération PixverseDuration | Durée de la vidéo en secondes |
| `mode de mouvement` | COMBO | Oui | Options de mode de mouvement disponibles dans l'énumération PixverseMotionMode | Style de mouvement pour la transition |
| `seed` | INT | Oui | 0 à 2147483647 | Graine pour la génération de vidéo (par défaut : 0) |
| `prompt négatif` | STRING | Non | - | Une description textuelle optionnelle des éléments indésirables sur une image (par défaut : chaîne vide) |

**Note :** Lors de l'utilisation de la qualité 1080p, le mode de mouvement est automatiquement défini sur normal et la durée est limitée à 5 secondes. Pour les durées autres que 5 secondes, le mode de mouvement est également automatiquement défini sur normal.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo de transition générée |