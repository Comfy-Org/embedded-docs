> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/fr.md)

Génère des vidéos à partir de descriptions textuelles via l'API Google Veo 3. Ce nœud prend en charge plusieurs modèles Veo 3, y compris les variantes rapides et légères, et permet de spécifier la résolution, la durée et la génération audio de la vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | - | Description textuelle de la vidéo (par défaut : "") |
| `aspect_ratio` | COMBO | Oui | "16:9"<br>"9:16" | Format d'image de la vidéo de sortie (par défaut : "16:9") |
| `resolution` | COMBO | Non | "720p"<br>"1080p"<br>"4k" | Résolution de la vidéo de sortie. La 4K n'est pas disponible pour les modèles veo-3.1-lite et veo-3.0. (par défaut : "720p") |
| `negative_prompt` | STRING | Non | - | Description textuelle négative pour indiquer ce qu'il faut éviter dans la vidéo (par défaut : "") |
| `duration_seconds` | INT | Non | 4-8 | Durée de la vidéo de sortie en secondes, par pas de 2 (par défaut : 8) |
| `enhance_prompt` | BOOLEAN | Non | - | Ce paramètre est obsolète et ignoré. (par défaut : True) |
| `person_generation` | COMBO | Non | "ALLOW"<br>"BLOCK" | Autoriser ou non la génération de personnes dans la vidéo (par défaut : "ALLOW") |
| `seed` | INT | Non | 0-4294967295 | Graine pour la génération de la vidéo (0 pour aléatoire) (par défaut : 0) |
| `image` | IMAGE | Non | - | Image de référence optionnelle pour guider la génération de la vidéo |
| `model` | COMBO | Non | "veo-3.1-generate"<br>"veo-3.1-fast-generate"<br>"veo-3.1-lite"<br>"veo-3.0-generate-001"<br>"veo-3.0-fast-generate-001" | Modèle Veo 3 à utiliser pour la génération de la vidéo (par défaut : "veo-3.0-generate-001") |
| `generate_audio` | BOOLEAN | Non | - | Générer l'audio pour la vidéo. Pris en charge par tous les modèles Veo 3. (par défaut : False) |

**Remarque :** Le paramètre `enhance_prompt` est obsolète et sa valeur est ignorée. Le nœud améliore toujours la description textuelle en interne. De plus, le paramètre `resolution` n'est appliqué qu'avec un modèle veo-3.1 ; il est ignoré pour les modèles veo-3.0.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | Le fichier vidéo généré |

---
**Source fingerprint (SHA-256):** `36ea9d3f0ea717eb7b8146ca35dfdfbe538fbbf164541ee1d1b19b660543e375`
