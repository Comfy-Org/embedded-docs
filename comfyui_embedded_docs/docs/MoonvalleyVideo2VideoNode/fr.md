> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyVideo2VideoNode/fr.md)

Le nœud Moonvalley Marey Video to Video transforme une vidéo d'entrée en une nouvelle vidéo basée sur une description textuelle. Il utilise l'API Moonvalley pour générer des vidéos qui correspondent à votre prompt tout en préservant les caractéristiques de mouvement ou de pose de la vidéo originale. Vous pouvez contrôler le style et le contenu de la vidéo de sortie via des prompts textuels et divers paramètres de génération.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Décrit la vidéo à générer (entrée multiligne) |
| `negative_prompt` | STRING | Non | - | Texte du prompt négatif (par défaut : liste étendue de descripteurs négatifs) |
| `seed` | INT | Oui | 0-4294967295 | Valeur de seed aléatoire (par défaut : 9) |
| `video` | VIDEO | Oui | - | La vidéo de référence utilisée pour générer la vidéo de sortie. Doit durer au moins 5 secondes. Les vidéos plus longues que 5s seront automatiquement tronquées. Seul le format MP4 est pris en charge. |
| `control_type` | COMBO | Non | "Motion Transfer"<br>"Pose Transfer" | Sélection du type de contrôle (par défaut : "Motion Transfer") |
| `motion_intensity` | INT | Non | 0-100 | Utilisé uniquement si control_type est 'Motion Transfer' (par défaut : 100) |
| `steps` | INT | Oui | 1-100 | Nombre d'étapes d'inférence (par défaut : 33) |

**Note :** Le paramètre `motion_intensity` n'est appliqué que lorsque `control_type` est défini sur "Motion Transfer". Lors de l'utilisation de "Pose Transfer", ce paramètre est ignoré.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo générée en sortie |