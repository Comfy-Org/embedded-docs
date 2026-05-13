> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/fr.md)

Voici la traduction en français de la documentation du nœud Veo3FirstLastFrameNode :

Le nœud Veo3FirstLastFrameNode utilise le modèle Veo 3 de Google pour générer une vidéo à partir d'une invite textuelle, avec une première et une dernière image fournies qui définissent le début et la fin de la séquence vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Description textuelle de la vidéo (par défaut : chaîne vide). |
| `negative_prompt` | STRING | Non | N/A | Invite textuelle négative pour guider ce qu'il faut éviter dans la vidéo (par défaut : chaîne vide). |
| `resolution` | COMBO | Oui | `"720p"`<br>`"1080p"`<br>`"4k"` | La résolution de la vidéo de sortie. |
| `aspect_ratio` | COMBO | Non | `"16:9"`<br>`"9:16"` | Format d'image de la vidéo de sortie (par défaut : "16:9"). |
| `duration` | INT | Non | 4 à 8 | Durée de la vidéo de sortie en secondes (par défaut : 8). |
| `seed` | INT | Non | 0 à 4294967295 | Graine pour la génération vidéo (par défaut : 0). |
| `first_frame` | IMAGE | Oui | N/A | L'image de début de la vidéo. |
| `last_frame` | IMAGE | Oui | N/A | L'image de fin de la vidéo. |
| `model` | COMBO | Non | `"veo-3.1-generate"`<br>`"veo-3.1-fast-generate"`<br>`"veo-3.1-lite"` | Le modèle Veo 3 spécifique à utiliser pour la génération (par défaut : "veo-3.1-generate"). |
| `generate_audio` | BOOLEAN | Non | N/A | Générer l'audio pour la vidéo (par défaut : Vrai). |

**Remarque :** Le modèle `veo-3.1-lite` ne prend pas en charge la résolution 4K. Si vous sélectionnez `veo-3.1-lite` et la résolution `4k`, une erreur se produira.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | Le fichier vidéo généré. |

---
**Source fingerprint (SHA-256):** `b486b22e71a305172700760bb3eff256b0e571bba75e68f27e23a1e1a1319b5a`
