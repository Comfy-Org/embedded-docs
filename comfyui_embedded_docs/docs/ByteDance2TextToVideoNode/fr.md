# ByteDance Seedance 2.0 Texte vers Vidéo

Ce nœud génère une vidéo à partir d'un prompt textuel en utilisant les modèles Seedance 2.5 ou 2.0 de ByteDance. Il envoie le prompt au modèle sélectionné, attend la fin du traitement de la vidéo et renvoie le fichier vidéo résultant. Sélectionner le modèle `Seedance 2.5 Draft` produit à la place un aperçu rapide en 480p ; connectez le `draft_task_id` résultant au nœud ByteDance Seedance 2.5 Draft to Final Video pour générer la version finale en 1080p.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle Seedance à utiliser pour la génération vidéo. Seedance 2.5 est le modèle le plus récent, prenant en charge des vidéos allant jusqu'à 30 secondes et une sortie mp4/mov ; Seedance 2.5 Draft produit un aperçu rapide en 480p dont la sortie `draft_task_id` permet de générer la version finale en 1080p dans le nœud ByteDance Seedance 2.5 Draft to Final Video ; Seedance 2.0 est destiné à une qualité maximale et à la 4k ; Seedance 2.0 Fast est destiné à l'optimisation de la vitesse ; Seedance 2.0 Mini est destiné à la génération la plus rapide et la moins coûteuse. La sélection d'un modèle révèle des entrées supplémentaires pour le prompt, la résolution, le rapport d'aspect, la durée et la génération audio. | DYNAMIC_COMBO | Oui | `"Seedance 2.5"`<br>`"Seedance 2.5 Draft"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | Contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la valeur de `seed`. (par défaut : 0) | INT | Non | 0 à 2147483647 |
| `filigrane` | Indique s'il faut ajouter un filigrane à la vidéo. (par défaut : False) Il s'agit d'un paramètre avancé. | BOOLEAN | Non | True / False |

### Entrées Seedance 2.5

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel pour la génération vidéo. Placez les répliques entre guillemets doubles pour orienter le dialogue généré. | STRING | Oui | — |
| `resolution` | Résolution de la vidéo de sortie. (par défaut : `"720p"`) | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | Rapport d'aspect de la vidéo de sortie. (par défaut : `"16:9"`) | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes. (par défaut : 5) | INT | Oui | 4 à 30 |
| `generate_audio` | Activer la génération audio pour la vidéo de sortie. (par défaut : True) | BOOLEAN | Oui | True / False |
| `output_format` | Format de conteneur de la vidéo de sortie. (par défaut : `"mp4"`) | COMBO | Oui | `"mp4"` |

### Entrées Seedance 2.5 Draft

Ces entrées apparaissent lorsque `Seedance 2.5 Draft` est sélectionné. L'ensemble des paramètres correspond à Seedance 2.5 ci-dessus, sauf que `resolution` ne propose que `"480p"` (par défaut `"480p"`).

### Entrées Seedance 2.0

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel pour la génération vidéo. | STRING | Oui | — |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Rapport d'aspect de la vidéo de sortie. (par défaut : `"16:9"`) | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes. (par défaut : 7) | INT | Oui | 4 à 15 |
| `generate_audio` | Activer la génération audio pour la vidéo de sortie. (par défaut : True) | BOOLEAN | Oui | True / False |

### Entrées Seedance 2.0 Fast et Seedance 2.0 Mini

Partagées par Seedance 2.0 Fast et Seedance 2.0 Mini ; les deux modèles exposent les mêmes paramètres.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel pour la génération vidéo. | STRING | Oui | — |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"` |
| `ratio` | Rapport d'aspect de la vidéo de sortie. (par défaut : `"16:9"`) | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes. (par défaut : 7) | INT | Oui | 4 à 15 |
| `generate_audio` | Activer la génération audio pour la vidéo de sortie. (par défaut : True) | BOOLEAN | Oui | True / False |

**Remarque :** Le sélecteur `model` est dynamique ; les entrées affichées sous chaque section de modèle apparaissent lorsque ce modèle est sélectionné. Le prompt doit contenir au moins 1 caractère après suppression des espaces. Les limites de résolution et de durée dépendent du modèle sélectionné : Seedance 2.5 prend en charge 480p/720p/1080p et de 4 à 30 secondes, Seedance 2.0 prend en charge 480p/720p/1080p/4k et de 4 à 15 secondes, et Seedance 2.0 Fast et Seedance 2.0 Mini prennent en charge uniquement 480p/720p et de 4 à 15 secondes ; Seedance 2.5 Draft prend en charge uniquement 480p et de 4 à 30 secondes. La sortie `draft_task_id` n'est produite que par Seedance 2.5 Draft ; avec tout autre modèle, elle doit rester non connectée, sinon l'exécution échoue. La valeur `seed` contrôle uniquement si le nœud est réexécuté ; elle ne rend pas les résultats déterministes.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le fichier vidéo généré. | VIDEO |
| `draft_task_id` | ID de tâche de l'exécution du brouillon. Seul le modèle Seedance 2.5 Draft le produit ; connectez-le au nœud ByteDance Seedance 2.5 Draft to Final Video pour générer la version finale en 1080p. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `2abad0c4eab5a1286c8da9237bcec52b275c40188b3b7dc9eede5d5f4cbb11d3`
