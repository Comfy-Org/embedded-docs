# GeminiNodeV3

Générez des réponses textuelles avec les modèles Gemini de Google. Fournissez une invite textuelle et, éventuellement, une ou plusieurs images, clips audio, vidéos ou fichiers comme contexte multimodal. Le modèle sélectionné détermine quels réglages supplémentaires apparaissent.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle Gemini utilisé pour générer la réponse. Le modèle sélectionné détermine quelles entrées supplémentaires sont affichées. | DYNAMIC_COMBO | Oui | `"Gemini 3.8 Flash"`<br>`"Gemini 3.7 Flash"`<br>`"Gemini 3.5 Flash"`<br>`"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |

### Entrées multimédias

Ces entrées multimédias extensibles sont disponibles pour chaque option de modèle.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Image(s) facultative(s) à utiliser comme contexte pour le modèle. Jusqu'à 16 images. Emplacement extensible : connectez les images de `image_1` à `image_16`. | IMAGE | Non | Jusqu'à 16 images |
| `audio` | Clip audio facultatif à utiliser comme contexte pour le modèle. Emplacement extensible : `audio_1`. | AUDIO | Non | 1 clip audio |
| `video` | Clip vidéo facultatif à utiliser comme contexte pour le modèle. Emplacement extensible : `video_1`. | VIDEO | Non | 1 clip vidéo |

### Entrées Gemini 3.8 Flash

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Entrée textuelle pour le modèle. Incluez des instructions détaillées, des questions ou du contexte. Ne doit pas être vide. | STRING | Oui | Texte multiligne (doit contenir au moins un caractère non blanc) |
| `video_processing` | Comment le modèle lit la vidéo jointe. `static` échantillonne des trames à un rythme fixe et les envoie toutes comme contexte ; `agentic` laisse le modèle parcourir lui-même la chronologie et charger uniquement les trames, l'audio ou la transcription dont il a besoin, ce qui coûte bien moins de jetons d'entrée sur les vidéos longues. | COMBO | Oui | `"static"`<br>`"agentic"` (par défaut : `"static"`) |
| `files` | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées provenant du nœud Gemini Input Files. | GEMINI_INPUT_FILES | Non | N/A |
| `thinking_level` | Intensité de raisonnement interne du modèle avant sa réponse. HIGH améliore la qualité sur les tâches difficiles, mais consomme plus de jetons (de réflexion) et est plus lent. | COMBO | Oui | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` (par défaut : `"MEDIUM"`) |
| `max_output_tokens` | Nombre maximal de jetons à générer, y compris la réflexion interne du modèle. Avec thinking_level HIGH, une valeur faible peut ne laisser aucune place à la réponse ; augmentez cette valeur si les réponses reviennent vides ou tronquées. Le modèle s'arrête tôt lorsqu'il a terminé, donc un plafond plus élevé ne coûte rien de plus pour les réponses courtes. | INT | Oui | 16-65536 (par défaut : 32768) |
| `seed` | Graine pour l'échantillonnage. Définissez sur 0 pour une graine aléatoire. Le caractère déterministe de la sortie n'est pas garanti. | INT | Oui | 0-2147483647 (par défaut : 42) |
| `system_prompt` | Instructions fondamentales qui dictent le comportement du modèle. | STRING | Oui | Texte multiligne (par défaut : vide) |

### Entrées Gemini 3.7 Flash

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Entrée textuelle pour le modèle. Incluez des instructions détaillées, des questions ou du contexte. Ne doit pas être vide. | STRING | Oui | Texte multiligne (doit contenir au moins un caractère non blanc) |
| `files` | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées provenant du nœud Gemini Input Files. | GEMINI_INPUT_FILES | Non | N/A |
| `thinking_level` | Intensité de raisonnement interne du modèle avant sa réponse. HIGH améliore la qualité sur les tâches difficiles, mais consomme plus de jetons (de réflexion) et est plus lent. | COMBO | Oui | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` (par défaut : `"MEDIUM"`) |
| `temperature` | Contrôle le caractère aléatoire. Une valeur plus basse est plus ciblée/déterministe, une valeur plus élevée est plus créative. | FLOAT | Oui | 0.0-2.0 (par défaut : 1.0) |
| `top_p` | Échantillonnage par noyau : échantillonne à partir du plus petit ensemble de jetons dont la probabilité cumulée atteint top_p. | FLOAT | Oui | 0.0-1.0 (par défaut : 0.95) |
| `max_output_tokens` | Nombre maximal de jetons à générer, y compris la réflexion interne du modèle. Avec thinking_level HIGH, une valeur faible peut ne laisser aucune place à la réponse ; augmentez cette valeur si les réponses reviennent vides ou tronquées. Le modèle s'arrête tôt lorsqu'il a terminé, donc un plafond plus élevé ne coûte rien de plus pour les réponses courtes. | INT | Oui | 16-65536 (par défaut : 32768) |
| `seed` | Graine pour l'échantillonnage. Définissez sur 0 pour une graine aléatoire. Le caractère déterministe de la sortie n'est pas garanti. | INT | Oui | 0-2147483647 (par défaut : 42) |
| `system_prompt` | Instructions fondamentales qui dictent le comportement du modèle. | STRING | Oui | Texte multiligne (par défaut : vide) |

### Entrées Gemini 3.5 Flash

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Entrée textuelle pour le modèle. Incluez des instructions détaillées, des questions ou du contexte. Ne doit pas être vide. | STRING | Oui | Texte multiligne (doit contenir au moins un caractère non blanc) |
| `files` | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées provenant du nœud Gemini Input Files. | GEMINI_INPUT_FILES | Non | N/A |
| `thinking_level` | Intensité de raisonnement interne du modèle avant sa réponse. HIGH améliore la qualité sur les tâches difficiles, mais consomme plus de jetons (de réflexion) et est plus lent. | COMBO | Oui | `"MINIMAL"`<br>`"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` (par défaut : `"MEDIUM"`) |
| `temperature` | Contrôle le caractère aléatoire. Une valeur plus basse est plus ciblée/déterministe, une valeur plus élevée est plus créative. | FLOAT | Oui | 0.0-2.0 (par défaut : 1.0) |
| `top_p` | Échantillonnage par noyau : échantillonne à partir du plus petit ensemble de jetons dont la probabilité cumulée atteint top_p. | FLOAT | Oui | 0.0-1.0 (par défaut : 0.95) |
| `max_output_tokens` | Nombre maximal de jetons à générer, y compris la réflexion interne du modèle. Avec thinking_level HIGH, une valeur faible peut ne laisser aucune place à la réponse ; augmentez cette valeur si les réponses reviennent vides ou tronquées. Le modèle s'arrête tôt lorsqu'il a terminé, donc un plafond plus élevé ne coûte rien de plus pour les réponses courtes. | INT | Oui | 16-65536 (par défaut : 32768) |
| `seed` | Graine pour l'échantillonnage. Définissez sur 0 pour une graine aléatoire. Le caractère déterministe de la sortie n'est pas garanti. | INT | Oui | 0-2147483647 (par défaut : 42) |
| `system_prompt` | Instructions fondamentales qui dictent le comportement du modèle. | STRING | Oui | Texte multiligne (par défaut : vide) |

### Entrées Gemini 3.1 Pro

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Entrée textuelle pour le modèle. Incluez des instructions détaillées, des questions ou du contexte. Ne doit pas être vide. | STRING | Oui | Texte multiligne (doit contenir au moins un caractère non blanc) |
| `files` | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées provenant du nœud Gemini Input Files. | GEMINI_INPUT_FILES | Non | N/A |
| `thinking_level` | Intensité de raisonnement interne du modèle avant sa réponse. HIGH améliore la qualité sur les tâches difficiles, mais consomme plus de jetons (de réflexion) et est plus lent. | COMBO | Oui | `"LOW"`<br>`"HIGH"` (par défaut : `"HIGH"`) |
| `temperature` | Contrôle le caractère aléatoire. Une valeur plus basse est plus ciblée/déterministe, une valeur plus élevée est plus créative. | FLOAT | Oui | 0.0-2.0 (par défaut : 1.0) |
| `top_p` | Échantillonnage par noyau : échantillonne à partir du plus petit ensemble de jetons dont la probabilité cumulée atteint top_p. | FLOAT | Oui | 0.0-1.0 (par défaut : 0.95) |
| `max_output_tokens` | Nombre maximal de jetons à générer, y compris la réflexion interne du modèle. Avec thinking_level HIGH, une valeur faible peut ne laisser aucune place à la réponse ; augmentez cette valeur si les réponses reviennent vides ou tronquées. Le modèle s'arrête tôt lorsqu'il a terminé, donc un plafond plus élevé ne coûte rien de plus pour les réponses courtes. | INT | Oui | 16-65536 (par défaut : 32768) |
| `seed` | Graine pour l'échantillonnage. Définissez sur 0 pour une graine aléatoire. Le caractère déterministe de la sortie n'est pas garanti. | INT | Oui | 0-2147483647 (par défaut : 42) |
| `system_prompt` | Instructions fondamentales qui dictent le comportement du modèle. | STRING | Oui | Texte multiligne (par défaut : vide) |

### Entrées Gemini 3.1 Flash-Lite

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Entrée textuelle pour le modèle. Incluez des instructions détaillées, des questions ou du contexte. Ne doit pas être vide. | STRING | Oui | Texte multiligne (doit contenir au moins un caractère non blanc) |
| `files` | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées provenant du nœud Gemini Input Files. | GEMINI_INPUT_FILES | Non | N/A |
| `thinking_level` | Intensité de raisonnement interne du modèle avant sa réponse. HIGH améliore la qualité sur les tâches difficiles, mais consomme plus de jetons (de réflexion) et est plus lent. | COMBO | Oui | `"LOW"`<br>`"HIGH"` (par défaut : `"LOW"`) |
| `temperature` | Contrôle le caractère aléatoire. Une valeur plus basse est plus ciblée/déterministe, une valeur plus élevée est plus créative. | FLOAT | Oui | 0.0-2.0 (par défaut : 1.0) |
| `top_p` | Échantillonnage par noyau : échantillonne à partir du plus petit ensemble de jetons dont la probabilité cumulée atteint top_p. | FLOAT | Oui | 0.0-1.0 (par défaut : 0.95) |
| `max_output_tokens` | Nombre maximal de jetons à générer, y compris la réflexion interne du modèle. Avec thinking_level HIGH, une valeur faible peut ne laisser aucune place à la réponse ; augmentez cette valeur si les réponses reviennent vides ou tronquées. Le modèle s'arrête tôt lorsqu'il a terminé, donc un plafond plus élevé ne coûte rien de plus pour les réponses courtes. | INT | Oui | 16-65536 (par défaut : 32768) |
| `seed` | Graine pour l'échantillonnage. Définissez sur 0 pour une graine aléatoire. Le caractère déterministe de la sortie n'est pas garanti. | INT | Oui | 0-2147483647 (par défaut : 42) |
| `system_prompt` | Instructions fondamentales qui dictent le comportement du modèle. | STRING | Oui | Texte multiligne (par défaut : vide) |

Remarque : pour Gemini 3.8 Flash, `temperature` et `top_p` ne sont pas disponibles, et `video_processing` n'est disponible que pour cette option de modèle. Les options et la valeur par défaut de `thinking_level` diffèrent selon le modèle, comme indiqué ci-dessus.

Remarque : l'entrée `prompt` ne doit pas être vide. Le nœud vérifie qu'elle contient au moins un caractère non blanc.

Remarque : le nœud téléverse jusqu'aux 10 premiers éléments multimédias sous forme d'URL, en donnant la priorité à la vidéo, puis à l'audio, puis aux images. Tout média restant est incorporé dans la requête en base64. Le total des médias incorporés est limité à 18 Mo ; en cas de dépassement, le nœud génère une erreur vous demandant de réduire le nombre ou la taille des médias joints.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `STRING` | La réponse textuelle générée par le modèle Gemini sélectionné. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV3/fr.md)

---
**Source fingerprint (SHA-256):** `d04d1e97a9c213297899291ad30db14a9f946b07506d0377fead4e29510c5ad9`
