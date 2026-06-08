Voici la traduction en français de la documentation du nœud Veo3FirstLastFrameNode :

Le nœud Veo3FirstLastFrameNode utilise le modèle Veo 3 de Google pour générer une vidéo à partir d'une invite textuelle, avec une première et une dernière image fournies qui définissent le début et la fin de la séquence vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Description textuelle de la vidéo (par défaut : chaîne vide). | STRING | Oui | N/A |
| `negative_prompt` | Invite textuelle négative pour guider ce qu'il faut éviter dans la vidéo (par défaut : chaîne vide). | STRING | Non | N/A |
| `résolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"720p"`<br>`"1080p"`<br>`"4k"` |
| `rapport d'aspect` | Format d'image de la vidéo de sortie (par défaut : "16:9"). | COMBO | Non | `"16:9"`<br>`"9:16"` |
| `durée` | Durée de la vidéo de sortie en secondes (par défaut : 8). | INT | Non | 4 à 8 |
| `seed` | Graine pour la génération vidéo (par défaut : 0). | INT | Non | 0 à 4294967295 |
| `première image` | L'image de début de la vidéo. | IMAGE | Oui | N/A |
| `dernière image` | L'image de fin de la vidéo. | IMAGE | Oui | N/A |
| `modèle` | Le modèle Veo 3 spécifique à utiliser pour la génération (par défaut : "veo-3.1-generate"). | COMBO | Non | `"veo-3.1-generate"`<br>`"veo-3.1-fast-generate"`<br>`"veo-3.1-lite"` |
| `générer audio` | Générer l'audio pour la vidéo (par défaut : Vrai). | BOOLEAN | Non | N/A |

**Remarque :** Le modèle `veo-3.1-lite` ne prend pas en charge la résolution 4K. Si vous sélectionnez `veo-3.1-lite` et la résolution `4k`, une erreur se produira.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `b486b22e71a305172700760bb3eff256b0e571bba75e68f27e23a1e1a1319b5a`
