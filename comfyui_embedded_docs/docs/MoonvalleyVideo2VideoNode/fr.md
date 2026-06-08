Voici la traduction en français de la documentation du nœud ComfyUI **Moonvalley Video to Video** :

Le nœud Moonvalley Marey Video to Video transforme une vidéo d'entrée en une nouvelle vidéo basée sur une description textuelle. Il utilise l'API Moonvalley pour générer des vidéos correspondant à votre invite tout en conservant les caractéristiques de mouvement ou de posture de la vidéo d'origine. Vous pouvez contrôler le style et le contenu de la vidéo de sortie via des invites textuelles et divers paramètres de génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Décrit la vidéo à générer (saisie multiligne) | STRING | Oui | - |
| `negative_prompt` | Texte de l'invite négative (par défaut : liste étendue de descripteurs négatifs) | STRING | Non | - |
| `seed` | Valeur de la graine aléatoire (par défaut : 9) | INT | Oui | 0 à 4294967295 |
| `video` | La vidéo de référence utilisée pour générer la vidéo de sortie. Doit durer au moins 5 secondes. Les vidéos de plus de 5 s seront automatiquement rognées. Seul le format MP4 est pris en charge. | VIDEO | Oui | - |
| `control_type` | Sélection du type de contrôle (par défaut : "Motion Transfer") | COMBO | Non | "Motion Transfer"<br>"Pose Transfer" |
| `motion_intensity` | Utilisé uniquement si `control_type` est "Motion Transfer" (par défaut : 100) | INT | Non | 0 à 100 |
| `steps` | Nombre d'étapes d'inférence (par défaut : 33) | INT | Oui | 1 à 100 |

**Remarque :** Le paramètre `motion_intensity` n'est appliqué que lorsque `control_type` est défini sur "Motion Transfer". Lorsque vous utilisez "Pose Transfer", ce paramètre est ignoré.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo générée en sortie | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyVideo2VideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `8202a4be469afa16d77b9e0287c290b9c3f390347fc60f23878f50fd95a758e0`
