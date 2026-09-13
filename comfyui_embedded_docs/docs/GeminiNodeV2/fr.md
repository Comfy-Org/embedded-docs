# Google Gemini

Générez des réponses textuelles avec les modèles Gemini de Google. Fournissez un prompt textuel et, éventuellement, une ou plusieurs images, clips audio, vidéos ou fichiers comme contexte multimodal.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Modèle Gemini utilisé pour générer la réponse. | DYNAMIC_COMBO | Oui | `"Gemini 3.8 Flash"`<br>`"Gemini 3.7 Flash"`<br>`"Gemini 3.5 Flash"`<br>`"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |
| `invite` | Entrée textuelle pour le modèle. Incluez des instructions détaillées, des questions ou du contexte. Doit contenir au moins un caractère autre qu'un espace blanc. (valeur par défaut : "") | STRING | Oui |  |
| `graine` | Graine pour l'échantillonnage. Définissez sur 0 pour une graine aléatoire. Une sortie déterministe n'est pas garantie. (valeur par défaut : 42) | INT | Oui | 0 à 2147483647 |
| `invite système` | Instructions fondamentales qui dictent le comportement du modèle. (valeur par défaut : "") | STRING | Non |  |

### Entrées Gemini 3.8 Flash

Ces entrées apparaissent lorsque `model` est défini sur `"Gemini 3.8 Flash"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `thinking_level` | Intensité avec laquelle le modèle raisonne en interne avant de répondre. HIGH améliore la qualité sur les tâches difficiles, mais consomme plus de tokens (de réflexion) et est plus lent. (valeur par défaut : "MEDIUM") | COMBO | Oui | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `max_output_tokens` | Nombre maximal de tokens à générer, y compris la réflexion interne du modèle. Avec thinking_level HIGH, une valeur faible peut ne laisser aucune place à la réponse ; augmentez-la si les réponses reviennent vides ou tronquées. Le modèle s'arrête tôt lorsqu'il a terminé, donc un plafond plus élevé ne coûte rien de plus pour les réponses courtes. (valeur par défaut : 32768) | INT | Oui | 16 à 65536 |

**Remarque :** Ce modèle n'expose pas les contrôles d'échantillonnage `temperature` ou `top_p`.

### Entrées Gemini 3.7 Flash

Ces entrées apparaissent lorsque `model` est défini sur `"Gemini 3.7 Flash"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `thinking_level` | Intensité avec laquelle le modèle raisonne en interne avant de répondre. HIGH améliore la qualité sur les tâches difficiles, mais consomme plus de tokens (de réflexion) et est plus lent. (valeur par défaut : "MEDIUM") | COMBO | Oui | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `temperature` | Contrôle l'aléatoire. Une valeur plus faible est plus ciblée/déterministe, une valeur plus élevée est plus créative. (valeur par défaut : 1.0) | FLOAT | Oui | 0.0 à 2.0 |
| `top_p` | Échantillonnage par noyau (nucleus sampling) : échantillonne à partir du plus petit ensemble de tokens dont la probabilité cumulée atteint top_p. (valeur par défaut : 0.95) | FLOAT | Oui | 0.0 à 1.0 |
| `max_output_tokens` | Nombre maximal de tokens à générer, y compris la réflexion interne du modèle. Avec thinking_level HIGH, une valeur faible peut ne laisser aucune place à la réponse ; augmentez-la si les réponses reviennent vides ou tronquées. Le modèle s'arrête tôt lorsqu'il a terminé, donc un plafond plus élevé ne coûte rien de plus pour les réponses courtes. (valeur par défaut : 32768) | INT | Oui | 16 à 65536 |

### Entrées Gemini 3.5 Flash

Ces entrées apparaissent lorsque `model` est défini sur `"Gemini 3.5 Flash"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `thinking_level` | Intensité avec laquelle le modèle raisonne en interne avant de répondre. HIGH améliore la qualité sur les tâches difficiles, mais consomme plus de tokens (de réflexion) et est plus lent. (valeur par défaut : "MEDIUM") | COMBO | Oui | `"MINIMAL"`<br>`"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `temperature` | Contrôle l'aléatoire. Une valeur plus faible est plus ciblée/déterministe, une valeur plus élevée est plus créative. (valeur par défaut : 1.0) | FLOAT | Oui | 0.0 à 2.0 |
| `top_p` | Échantillonnage par noyau (nucleus sampling) : échantillonne à partir du plus petit ensemble de tokens dont la probabilité cumulée atteint top_p. (valeur par défaut : 0.95) | FLOAT | Oui | 0.0 à 1.0 |
| `max_output_tokens` | Nombre maximal de tokens à générer, y compris la réflexion interne du modèle. Avec thinking_level HIGH, une valeur faible peut ne laisser aucune place à la réponse ; augmentez-la si les réponses reviennent vides ou tronquées. Le modèle s'arrête tôt lorsqu'il a terminé, donc un plafond plus élevé ne coûte rien de plus pour les réponses courtes. (valeur par défaut : 32768) | INT | Oui | 16 à 65536 |

### Entrées Gemini 3.1 Pro

Ces entrées apparaissent lorsque `model` est défini sur `"Gemini 3.1 Pro"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `thinking_level` | Intensité avec laquelle le modèle raisonne en interne avant de répondre. HIGH améliore la qualité sur les tâches difficiles, mais consomme plus de tokens (de réflexion) et est plus lent. (valeur par défaut : "HIGH") | COMBO | Oui | `"LOW"`<br>`"HIGH"` |
| `temperature` | Contrôle l'aléatoire. Une valeur plus faible est plus ciblée/déterministe, une valeur plus élevée est plus créative. (valeur par défaut : 1.0) | FLOAT | Oui | 0.0 à 2.0 |
| `top_p` | Échantillonnage par noyau (nucleus sampling) : échantillonne à partir du plus petit ensemble de tokens dont la probabilité cumulée atteint top_p. (valeur par défaut : 0.95) | FLOAT | Oui | 0.0 à 1.0 |
| `max_output_tokens` | Nombre maximal de tokens à générer, y compris la réflexion interne du modèle. Avec thinking_level HIGH, une valeur faible peut ne laisser aucune place à la réponse ; augmentez-la si les réponses reviennent vides ou tronquées. Le modèle s'arrête tôt lorsqu'il a terminé, donc un plafond plus élevé ne coûte rien de plus pour les réponses courtes. (valeur par défaut : 32768) | INT | Oui | 16 à 65536 |

### Entrées Gemini 3.1 Flash-Lite

Ces entrées apparaissent lorsque `model` est défini sur `"Gemini 3.1 Flash-Lite"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `thinking_level` | Intensité avec laquelle le modèle raisonne en interne avant de répondre. HIGH améliore la qualité sur les tâches difficiles, mais consomme plus de tokens (de réflexion) et est plus lent. (valeur par défaut : "LOW") | COMBO | Oui | `"LOW"`<br>`"HIGH"` |
| `temperature` | Contrôle l'aléatoire. Une valeur plus faible est plus ciblée/déterministe, une valeur plus élevée est plus créative. (valeur par défaut : 1.0) | FLOAT | Oui | 0.0 à 2.0 |
| `top_p` | Échantillonnage par noyau (nucleus sampling) : échantillonne à partir du plus petit ensemble de tokens dont la probabilité cumulée atteint top_p. (valeur par défaut : 0.95) | FLOAT | Oui | 0.0 à 1.0 |
| `max_output_tokens` | Nombre maximal de tokens à générer, y compris la réflexion interne du modèle. Avec thinking_level HIGH, une valeur faible peut ne laisser aucune place à la réponse ; augmentez-la si les réponses reviennent vides ou tronquées. Le modèle s'arrête tôt lorsqu'il a terminé, donc un plafond plus élevé ne coûte rien de plus pour les réponses courtes. (valeur par défaut : 32768) | INT | Oui | 16 à 65536 |

### Entrées de médias et de fichiers

Les entrées suivantes sont partagées par tous les modèles et apparaissent à côté des entrées propres à chaque modèle.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Emplacement extensible : connectez 1 à 16 images (`image_1` ... `image_16`). Image(s) facultative(s) à utiliser comme contexte pour le modèle. Jusqu'à 16 images. | IMAGE | Non | 0 à 16 images |
| `audio` | Emplacement extensible : connectez un clip audio (`audio_1`). Clip audio facultatif à utiliser comme contexte pour le modèle. | AUDIO | Non | 0 à 1 clip |
| `video` | Emplacement extensible : connectez un clip vidéo (`video_1`). Clip vidéo facultatif à utiliser comme contexte pour le modèle. | VIDEO | Non | 0 à 1 clip |
| `files` | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Input Files. | GEMINI_INPUT_FILES | Non |  |

**Remarque :** Lorsque des médias (images, audio ou vidéo) sont joints, le nœud téléverse les 10 premiers éléments multimédias vers le stockage ComfyAPI et les transmet sous forme d'URL ; ce budget d'URL est partagé entre tous les types de médias et est consommé dans l'ordre (vidéo d'abord, puis audio, puis images). Tout média restant est encodé en ligne en données base64, avec une charge utile en ligne combinée maximale de 18 Mo. Si la charge utile en ligne dépasse 18 Mo, le nœud génère une erreur. Le paramètre `prompt` doit contenir au moins un caractère autre qu'un espace blanc. Définir `seed` sur 0 demande une graine aléatoire.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Réponse textuelle générée par le modèle Gemini. Si le modèle ne produit aucun texte, la chaîne "Empty response from Gemini model..." est renvoyée. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `98a19d1b29e80907477d24d813593950a028021ee8bcf634f505e11a15daa383`
