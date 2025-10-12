> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | Oui | - | Image de référence - URL ou chaîne encodée en Base64, ne peut pas dépasser 10 Mo, résolution d'au moins 300*300 px, ratio d'aspect entre 1:2,5 et 2,5:1. Base64 ne doit pas inclure le préfixe data:image. |
| `end_frame` | IMAGE | Oui | - | Image de référence - Contrôle de l'image de fin. URL ou chaîne encodée en Base64, ne peut pas dépasser 10 Mo, résolution d'au moins 300*300 px. Base64 ne doit pas inclure le préfixe data:image. |
| `prompt` | STRING | Oui | - | Prompt texte positif |
| `negative_prompt` | STRING | Oui | - | Prompt texte négatif |
| `cfg_scale` | FLOAT | Non | 0.0-1.0 | Contrôle l'intensité de l'influence du prompt (par défaut : 0,5) |
| `aspect_ratio` | COMBO | Non | "16:9"<br>"9:16"<br>"1:1"<br>"21:9"<br>"9:21"<br>"3:4"<br>"4:3" | Le ratio d'aspect pour la vidéo générée (par défaut : "16:9") |
| `mode` | COMBO | Non | Plusieurs options disponibles | La configuration à utiliser pour la génération de vidéo suivant le format : mode / durée / nom_du_modèle. (par défaut : troisième option parmi les modes disponibles) |

**Contraintes des images :**

- `start_frame` et `end_frame` doivent tous deux être fournis et ne peuvent pas dépasser 10 Mo
- Résolution minimale : 300×300 pixels pour les deux images
- Le ratio d'aspect de `start_frame` doit être compris entre 1:2,5 et 2,5:1
- Les images encodées en Base64 ne doivent pas inclure le préfixe "data:image"

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `video_id` | VIDEO | La séquence vidéo générée |
| `duration` | STRING | Identifiant unique pour la vidéo générée |
| `duration` | STRING | Durée de la vidéo générée |
