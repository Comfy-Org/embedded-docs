> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/fr.md)

Génère des vidéos basées sur l'invite et la taille de sortie. Ce nœud crée du contenu vidéo en utilisant des descriptions textuelles et divers paramètres de génération, produisant une sortie vidéo via l'API PixVerse.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Invite pour la génération de vidéo (par défaut : "") |
| `rapport d'aspect` | COMBO | Oui | Options de PixverseAspectRatio | Ratio d'aspect pour la vidéo générée |
| `qualité` | COMBO | Oui | Options de PixverseQuality | Paramètre de qualité vidéo (par défaut : PixverseQuality.res_540p) |
| `durée (secondes)` | COMBO | Oui | Options de PixverseDuration | Durée de la vidéo générée en secondes |
| `mode de mouvement` | COMBO | Oui | Options de PixverseMotionMode | Style de mouvement pour la génération de vidéo |
| `graine` | INT | Oui | 0 à 2147483647 | Graine pour la génération de vidéo (par défaut : 0) |
| `prompt négatif` | STRING | Non | - | Une description textuelle optionnelle des éléments indésirables sur une image (par défaut : "") |
| `modèle PixVerse` | CUSTOM | Non | - | Un modèle optionnel pour influencer le style de génération, créé par le nœud PixVerse Template |

**Note :** Lors de l'utilisation de la qualité 1080p, le mode de mouvement est automatiquement défini sur normal et la durée est limitée à 5 secondes. Pour les durées autres que 5 secondes, le mode de mouvement est également automatiquement défini sur normal.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré |