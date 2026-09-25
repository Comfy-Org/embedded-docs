# ByteDance Seedance 2.0 Première-Dernière-Image vers Vidéo

Ce nœud génère une vidéo à partir d'une image de première frame obligatoire et d'une image de dernière frame facultative en utilisant les modèles ByteDance Seedance. Vous décrivez la vidéo avec un prompt textuel ; la première frame guide le début de la vidéo et la dernière frame guide la fin. Il prend en charge Seedance 2.5 et la famille Seedance 2.0 (Seedance 2.0, Seedance 2.0 Fast et Seedance 2.0 Mini). Sélectionner le modèle `Seedance 2.5 Draft` génère à la place un aperçu rapide en 480p ; connectez le `draft_task_id` résultant au nœud ByteDance Seedance 2.5 Draft to Final Video pour effectuer le rendu final en 1080p.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Seedance 2.5 pour le modèle le plus récent, des vidéos jusqu'à 30 secondes et une sortie mp4 ; Seedance 2.5 Draft pour un aperçu rapide en 480p dont la sortie `draft_task_id` effectue le rendu final en 1080p dans le nœud ByteDance Seedance 2.5 Draft to Final Video ; Seedance 2.0 pour une qualité maximale et la 4k ; Fast pour l'optimisation de la vitesse ; Mini pour la génération la plus rapide et la moins coûteuse. Sélectionner un modèle révèle les entrées propres au modèle ci-dessous. | DYNAMIC_COMBO | Oui | `"Seedance 2.5"`<br>`"Seedance 2.5 Draft"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `première image` | Image de la première frame pour la vidéo. | IMAGE | Non | - |
| `dernière image` | Image de la dernière frame pour la vidéo. | IMAGE | Non | - |
| `first_frame_asset_id` | asset_id Seedance à utiliser comme première frame. Mutuellement exclusif avec l'entrée image `first_frame`. La valeur par défaut est une chaîne vide. | STRING | Non | - |
| `last_frame_asset_id` | asset_id Seedance à utiliser comme dernière frame. Mutuellement exclusif avec l'entrée image `last_frame`. La valeur par défaut est une chaîne vide. | STRING | Non | - |
| `seed` | La seed contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la seed. La valeur par défaut est 0. | INT | Oui | 0 à 2147483647 |
| `filigrane` | Indique s'il faut ajouter un filigrane à la vidéo. La valeur par défaut est False. | BOOLEAN | Oui | False<br>True |

### Entrées Seedance 2.5

Ces entrées apparaissent lorsque `Seedance 2.5` est sélectionné.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel pour la génération de la vidéo. Placez les répliques parlées entre guillemets doubles pour orienter le dialogue généré. | STRING | Oui | - |
| `resolution` | Résolution de la vidéo de sortie. La valeur par défaut est 720p. | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | Durée de la vidéo de sortie en secondes (4-30). La valeur par défaut est 5. | INT | Oui | 4 à 30 |
| `generate_audio` | Activer la génération audio pour la vidéo de sortie. La valeur par défaut est True. | BOOLEAN | Oui | False<br>True |
| `output_format` | Format de conteneur de la vidéo de sortie. La valeur par défaut est mp4. | COMBO | Oui | `"mp4"` |

### Entrées Seedance 2.5 Draft

Ces entrées apparaissent lorsque `Seedance 2.5 Draft` est sélectionné. L'ensemble des paramètres correspond à Seedance 2.5 ci-dessus, sauf que `resolution` ne propose que `"480p"` (valeur par défaut `"480p"`).

### Entrées Seedance 2.0

Ces entrées apparaissent lorsque `Seedance 2.0` est sélectionné.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel pour la génération de la vidéo. | STRING | Oui | - |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Rapport d'aspect de la vidéo de sortie. La valeur par défaut est `adaptive`, qui utilise le rapport pris en charge le plus proche du rapport d'aspect de la frame d'entrée. | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes (4-15). La valeur par défaut est 7. | INT | Oui | 4 à 15 |
| `generate_audio` | Activer la génération audio pour la vidéo de sortie. La valeur par défaut est True. | BOOLEAN | Oui | False<br>True |

### Entrées Seedance 2.0 Fast et Seedance 2.0 Mini

Partagées par `Seedance 2.0 Fast` et `Seedance 2.0 Mini`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel pour la génération de la vidéo. | STRING | Oui | - |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"` |
| `ratio` | Rapport d'aspect de la vidéo de sortie. La valeur par défaut est `adaptive`, qui utilise le rapport pris en charge le plus proche du rapport d'aspect de la frame d'entrée. | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes (4-15). La valeur par défaut est 7. | INT | Oui | 4 à 15 |
| `generate_audio` | Activer la génération audio pour la vidéo de sortie. La valeur par défaut est True. | BOOLEAN | Oui | False<br>True |

**Contraintes des paramètres**

- Vous devez fournir la première frame soit sous forme d'image `first_frame`, soit via `first_frame_asset_id`. Fournir les deux déclenche une erreur ; n'en fournir aucun déclenche également une erreur.
- Les entrées `last_frame` et `last_frame_asset_id` sont facultatives, mais vous ne pouvez pas fournir les deux pour la même frame.
- Les ID d'asset doivent référencer des assets Seedance Image existants et actifs.
- L'entrée `prompt` est obligatoire et ne peut pas être vide.
- Chaque exécution renvoie son ID de tâche en tant que `draft_task_id`, mais seul l'ID d'une exécution `Seedance 2.5 Draft` peut être rendu par le nœud ByteDance Seedance 2.5 Draft to Final Video. Avec tout autre modèle, la sortie doit rester non connectée, sinon l'exécution échoue.
- Avec `Seedance 2.5`, le rapport d'aspect de sortie est toujours adaptatif et suit le rapport d'aspect propre à la première frame ; aucune entrée `ratio` n'est donc affichée.
- Avec les modèles de la famille Seedance 2.0 et des images de frame locales, les images sont recadrées au centre et redimensionnées à la résolution et au rapport de sortie cibles avant la génération. Lorsque `ratio` est `adaptive`, le rapport pris en charge le plus proche de l'image d'entrée est utilisé.
- Les images de frame locales sont validées pour leur rapport d'aspect et leurs dimensions pris en charge ; les images surdimensionnées sont réduites.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La vidéo générée. | VIDEO |
| `draft_task_id` | ID de tâche renvoyé par l'exécution. Seule une exécution `Seedance 2.5 Draft` produit un brouillon dont le nœud ByteDance Seedance 2.5 Draft to Final Video peut effectuer le rendu ; avec tout autre modèle, la sortie doit rester non connectée, sinon l'exécution échoue. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `363f1baac1685c2dada0e64a0b339f6ab2671161dccb002eb81f6b4f0d0aa243`
