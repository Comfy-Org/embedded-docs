# ByteDance Seedance 2.0 Texte vers Vidéo

Ce nœud génère une vidéo à partir d'un prompt texte en utilisant les modèles Seedance 2.5 ou 2.0 de ByteDance. Il envoie le prompt au modèle sélectionné, attend que la vidéo soit traitée, puis renvoie le fichier vidéo résultant.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle Seedance à utiliser pour la génération vidéo. Seedance 2.5 est le modèle le plus récent, prenant en charge des vidéos jusqu'à 30 secondes et une sortie mp4/mov ; Seedance 2.0 est destiné à une qualité maximale et à la 4k ; Seedance 2.0 Fast est optimisé pour la vitesse ; Seedance 2.0 Mini est conçu pour la génération la plus rapide et la moins coûteuse. La sélection d'un modèle révèle des entrées supplémentaires pour le prompt, la résolution, le format d'image, la durée et la génération audio. | DYNAMIC_COMBO | Oui | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | Contrôle si le nœud doit être relancé ; les résultats ne sont pas déterministes quel que soit le seed. (défaut : 0) | INT | Non | 0 à 2147483647 |
| `filigrane` | Indique s'il faut ajouter un filigrane à la vidéo. (défaut : False) Il s'agit d'un paramètre avancé. | BOOLEAN | Non | True / False |

### Entrées Seedance 2.5

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt texte pour la génération vidéo. Mettez les répliques entre guillemets doubles pour orienter le dialogue généré. | STRING | Oui | — |
| `resolution` | Résolution de la vidéo de sortie. (défaut : `"720p"`) | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | Format d'image de la vidéo de sortie. (défaut : `"16:9"`) | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes. (défaut : 5) | INT | Oui | 4 à 30 |
| `generate_audio` | Activer la génération audio pour la vidéo de sortie. (défaut : True) | BOOLEAN | Oui | True / False |
| `output_format` | Format de conteneur de la vidéo de sortie. (défaut : `"mp4"`) | COMBO | Oui | `"mp4"` |

### Entrées Seedance 2.0

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt texte pour la génération vidéo. | STRING | Oui | — |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Format d'image de la vidéo de sortie. (défaut : `"16:9"`) | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes. (défaut : 7) | INT | Oui | 4 à 15 |
| `generate_audio` | Activer la génération audio pour la vidéo de sortie. (défaut : True) | BOOLEAN | Oui | True / False |

### Entrées Seedance 2.0 Fast et Seedance 2.0 Mini

Partagées par Seedance 2.0 Fast et Seedance 2.0 Mini ; les deux modèles présentent les mêmes paramètres.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt texte pour la génération vidéo. | STRING | Oui | — |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"` |
| `ratio` | Format d'image de la vidéo de sortie. (défaut : `"16:9"`) | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes. (défaut : 7) | INT | Oui | 4 à 15 |
| `generate_audio` | Activer la génération audio pour la vidéo de sortie. (défaut : True) | BOOLEAN | Oui | True / False |

**Remarque :** Le sélecteur `model` est dynamique ; les entrées affichées dans chaque section de modèle apparaissent lorsque ce modèle est sélectionné. Le prompt doit contenir au moins 1 caractère après suppression des espaces blancs. Les limites de résolution et de durée dépendent du modèle sélectionné : Seedance 2.5 prend en charge 480p/720p/1080p et 4 à 30 secondes, Seedance 2.0 prend en charge 480p/720p/1080p/4k et 4 à 15 secondes, et Seedance 2.0 Fast et Seedance 2.0 Mini ne prennent en charge que 480p/720p et 4 à 15 secondes. La valeur `seed` contrôle uniquement si le nœud doit être relancé ; elle ne rend pas les résultats déterministes.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `e3b11f5a538d4b9b7e49f651d3939651edfe85000e02e66a8d7700c3389c4b9c`
