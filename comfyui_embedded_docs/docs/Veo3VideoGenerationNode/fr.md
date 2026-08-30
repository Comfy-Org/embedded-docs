# Génération vidéo Google Veo 3

Génère des vidéos à partir de prompts textuels à l'aide de l'API Google Veo 3. Ce nœud prend en charge plusieurs modèles Veo 3, y compris les variantes fast et lite, et permet de spécifier la résolution, la durée et la génération audio de la vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `invite` | Description textuelle de la vidéo (par défaut : "") | STRING | Oui | - |
| `ratio_d'aspect` | Ratio d'aspect de la vidéo de sortie (par défaut : "16:9") | COMBO | Oui | "16:9"<br>"9:16" |
| `résolution` | Résolution de la vidéo de sortie. La 4K n'est pas disponible pour le modèle veo-3.1-lite. (par défaut : "720p") | COMBO | Non | "720p"<br>"1080p"<br>"4k" |
| `invite_négative` | Prompt textuel négatif pour guider ce qui doit être évité dans la vidéo (par défaut : "") | STRING | Non | - |
| `durée_secondes` | Durée de la vidéo de sortie en secondes (par défaut : 8) | INT | Non | 4 - 8 (pas de 2) |
| `améliorer_invite` | Ce paramètre est obsolète et ignoré. (par défaut : True) | BOOLEAN | Non | - |
| `génération_personnes` | Indique s'il est permis de générer des personnes dans la vidéo (par défaut : "ALLOW") | COMBO | Non | "ALLOW"<br>"BLOCK" |
| `graine` | Graine pour la génération de la vidéo (0 pour aléatoire) (par défaut : 0) | INT | Non | 0 - 4294967295 |
| `image` | Image de référence facultative pour guider la génération de la vidéo | IMAGE | Non | - |
| `modèle` | Modèle Veo 3 à utiliser pour la génération de la vidéo (par défaut : "veo-3.1-generate") | COMBO | Non | "veo-3.1-generate"<br>"veo-3.1-fast-generate"<br>"veo-3.1-lite" |
| `générer_audio` | Générer l'audio pour la vidéo. Pris en charge par tous les modèles Veo 3. (par défaut : False) | BOOLEAN | Non | - |

**Remarque :** Le paramètre `enhance_prompt` est obsolète et sa valeur est ignorée. Le nœud améliore toujours le prompt en interne. Si vous sélectionnez la résolution "4k" avec le modèle veo-3.1-lite, le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Le fichier vidéo généré | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/fr.md)

---
**Source fingerprint (SHA-256):** `5320736448ad854e2f93e08ccaa870e977e06497666cb305f314bc76ff917740`
