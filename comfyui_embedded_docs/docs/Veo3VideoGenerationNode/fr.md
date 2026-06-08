Génère des vidéos à partir de descriptions textuelles via l'API Google Veo 3. Ce nœud prend en charge plusieurs modèles Veo 3, y compris les variantes rapides et légères, et permet de spécifier la résolution, la durée et la génération audio de la vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `invite` | Description textuelle de la vidéo (par défaut : "") | STRING | Oui | - |
| `ratio_d'aspect` | Format d'image de la vidéo de sortie (par défaut : "16:9") | COMBO | Oui | "16:9"<br>"9:16" |
| `résolution` | Résolution de la vidéo de sortie. La 4K n'est pas disponible pour les modèles veo-3.1-lite et veo-3.0. (par défaut : "720p") | COMBO | Non | "720p"<br>"1080p"<br>"4k" |
| `invite_négative` | Description textuelle négative pour indiquer ce qu'il faut éviter dans la vidéo (par défaut : "") | STRING | Non | - |
| `durée_secondes` | Durée de la vidéo de sortie en secondes, par pas de 2 (par défaut : 8) | INT | Non | 4-8 |
| `améliorer_invite` | Ce paramètre est obsolète et ignoré. (par défaut : True) | BOOLEAN | Non | - |
| `génération_personnes` | Autoriser ou non la génération de personnes dans la vidéo (par défaut : "ALLOW") | COMBO | Non | "ALLOW"<br>"BLOCK" |
| `graine` | Graine pour la génération de la vidéo (0 pour aléatoire) (par défaut : 0) | INT | Non | 0-4294967295 |
| `image` | Image de référence optionnelle pour guider la génération de la vidéo | IMAGE | Non | - |
| `modèle` | Modèle Veo 3 à utiliser pour la génération de la vidéo (par défaut : "veo-3.0-generate-001") | COMBO | Non | "veo-3.1-generate"<br>"veo-3.1-fast-generate"<br>"veo-3.1-lite"<br>"veo-3.0-generate-001"<br>"veo-3.0-fast-generate-001" |
| `générer_audio` | Générer l'audio pour la vidéo. Pris en charge par tous les modèles Veo 3. (par défaut : False) | BOOLEAN | Non | - |

**Remarque :** Le paramètre `enhance_prompt` est obsolète et sa valeur est ignorée. Le nœud améliore toujours la description textuelle en interne. De plus, le paramètre `resolution` n'est appliqué qu'avec un modèle veo-3.1 ; il est ignoré pour les modèles veo-3.0.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/fr.md)

---
**Source fingerprint (SHA-256):** `36ea9d3f0ea717eb7b8146ca35dfdfbe538fbbf164541ee1d1b19b660543e375`
