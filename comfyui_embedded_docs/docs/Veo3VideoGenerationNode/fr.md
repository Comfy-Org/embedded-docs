> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/fr.md)

Génère des vidéos à partir de descriptions textuelles en utilisant l'API Veo 3 de Google. Ce nœud prend en charge deux modèles Veo 3 : veo-3.0-generate-001 et veo-3.0-fast-generate-001. Il étend le nœud Veo de base avec des fonctionnalités spécifiques à Veo 3, incluant la génération audio et une durée fixe de 8 secondes.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Description textuelle de la vidéo (par défaut : "") |
| `aspect_ratio` | COMBO | Oui | "16:9"<br>"9:16" | Ratio d'aspect de la vidéo de sortie (par défaut : "16:9") |
| `negative_prompt` | STRING | Non | - | Description textuelle négative pour guider ce qu'il faut éviter dans la vidéo (par défaut : "") |
| `duration_seconds` | INT | Non | 8-8 | Durée de la vidéo de sortie en secondes (Veo 3 ne prend en charge que 8 secondes) (par défaut : 8) |
| `enhance_prompt` | BOOLEAN | Non | - | Indique s'il faut améliorer la description avec l'assistance de l'IA (par défaut : True) |
| `person_generation` | COMBO | Non | "ALLOW"<br>"BLOCK" | Indique s'il faut autoriser la génération de personnes dans la vidéo (par défaut : "ALLOW") |
| `seed` | INT | Non | 0-4294967295 | Graine pour la génération de vidéo (0 pour aléatoire) (par défaut : 0) |
| `image` | IMAGE | Non | - | Image de référence optionnelle pour guider la génération de la vidéo |
| `model` | COMBO | Non | "veo-3.0-generate-001"<br>"veo-3.0-fast-generate-001" | Modèle Veo 3 à utiliser pour la génération de vidéo (par défaut : "veo-3.0-generate-001") |
| `generate_audio` | BOOLEAN | Non | - | Générer l'audio pour la vidéo. Pris en charge par tous les modèles Veo 3. (par défaut : False) |

**Note :** Le paramètre `duration_seconds` est fixé à 8 secondes pour tous les modèles Veo 3 et ne peut pas être modifié.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré |