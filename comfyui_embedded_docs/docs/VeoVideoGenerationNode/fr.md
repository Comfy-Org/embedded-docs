> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeoVideoGenerationNode/fr.md)

Génère des vidéos à partir de prompts texte en utilisant l'API Veo de Google. Ce nœud peut créer des vidéos à partir de descriptions textuelles et d'images d'entrée optionnelles, avec un contrôle sur des paramètres tels que le ratio d'aspect, la durée, et plus encore.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Description textuelle de la vidéo (par défaut : vide) |
| `aspect_ratio` | COMBO | Oui | "16:9"<br>"9:16" | Ratio d'aspect de la vidéo de sortie (par défaut : "16:9") |
| `negative_prompt` | STRING | Non | - | Prompt texte négatif pour guider ce qu'il faut éviter dans la vidéo (par défaut : vide) |
| `duration_seconds` | INT | Non | 5-8 | Durée de la vidéo de sortie en secondes (par défaut : 5) |
| `enhance_prompt` | BOOLEAN | Non | - | Indique s'il faut améliorer le prompt avec une assistance IA (par défaut : True) |
| `person_generation` | COMBO | Non | "ALLOW"<br>"BLOCK" | Indique s'il faut autoriser la génération de personnes dans la vidéo (par défaut : "ALLOW") |
| `seed` | INT | Non | 0-4294967295 | Graine pour la génération de vidéo (0 pour aléatoire) (par défaut : 0) |
| `image` | IMAGE | Non | - | Image de référence optionnelle pour guider la génération de vidéo |
| `model` | COMBO | Non | "veo-2.0-generate-001" | Modèle Veo 2 à utiliser pour la génération de vidéo (par défaut : "veo-2.0-generate-001") |

**Note :** Le paramètre `generate_audio` est uniquement disponible pour les modèles Veo 3.0 et est automatiquement géré par le nœud en fonction du modèle sélectionné.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré |