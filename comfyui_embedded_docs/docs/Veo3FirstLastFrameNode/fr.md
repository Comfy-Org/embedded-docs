> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/fr.md)

Le nœud Veo3FirstLastFrameNode utilise le modèle Veo 3 de Google pour générer une vidéo. Il crée une vidéo à partir d'une description textuelle, en utilisant une première et une dernière image fournies pour guider le début et la fin de la séquence.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Description textuelle de la vidéo (par défaut : chaîne vide). |
| `negative_prompt` | STRING | Non | N/A | Description textuelle négative pour guider ce qu'il faut éviter dans la vidéo (par défaut : chaîne vide). |
| `resolution` | COMBO | Oui | `"720p"`<br>`"1080p"` | La résolution de la vidéo en sortie. |
| `aspect_ratio` | COMBO | Non | `"16:9"`<br>`"9:16"` | Ratio d'aspect de la vidéo en sortie (par défaut : "16:9"). |
| `duration` | INT | Non | 4 à 8 | Durée de la vidéo en sortie en secondes (par défaut : 8). |
| `seed` | INT | Non | 0 à 4294967295 | Graine pour la génération de la vidéo (par défaut : 0). |
| `first_frame` | IMAGE | Oui | N/A | L'image de départ pour la vidéo. |
| `last_frame` | IMAGE | Oui | N/A | L'image de fin pour la vidéo. |
| `model` | COMBO | Non | `"veo-3.1-generate"`<br>`"veo-3.1-fast-generate"` | Le modèle Veo 3 spécifique à utiliser pour la génération (par défaut : "veo-3.1-fast-generate"). |
| `generate_audio` | BOOLEAN | Non | N/A | Générer l'audio pour la vidéo (par défaut : True). |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré. |
