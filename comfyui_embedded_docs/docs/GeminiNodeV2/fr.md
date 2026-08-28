# Google Gemini

Génère des réponses textuelles avec les modèles Google Gemini. Fournissez une invite texte et, éventuellement, une ou plusieurs images, clips audio, vidéos ou fichiers comme contexte multimodal.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `modèle` | Le modèle Gemini utilisé pour générer la réponse. | DYNAMIC_COMBO | Oui | `"Gemini 3.7 Flash"`<br>`"Gemini 3.5 Flash"`<br>`"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |
| `invite` | Entrée texte destinée au modèle. Incluez des instructions détaillées, des questions ou du contexte. Doit contenir au moins un caractère non vide. (défaut : "") | STRING | Oui |  |
| `graine` | Graine pour l'échantillonnage. Mettez 0 pour une graine aléatoire. La sortie déterministe n'est pas garantie. (défaut : 42) | INT | Oui | 0 à 2147483647 |
| `invite système` | Instructions fondamentales qui régissent le comportement du modèle. (défaut : "") | STRING | Non |  |

### Entrées Gemini 3.7 Flash

Ces entrées apparaissent lorsque `model` est défini sur `"Gemini 3.7 Flash"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Niveau d'effort de raisonnement interne du modèle avant de répondre. HIGH améliore la qualité sur les tâches difficiles mais consomme davantage de jetons de réflexion et est plus lent. (défaut : "MEDIUM") | COMBO | Oui | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `temperature` | Contrôle le caractère aléatoire. Une valeur plus basse donne un résultat plus ciblé/déterministe, une valeur plus élevée plus créatif. (défaut : 1.0) | FLOAT | Oui | 0.0 à 2.0 |
| `top_p` | Échantillonnage nucleus : échantillonner à partir du plus petit ensemble de jetons dont la probabilité cumulée atteint top_p. (défaut : 0.95) | FLOAT | Oui | 0.0 à 1.0 |
| `max_output_tokens` | Nombre maximal de jetons à générer, y compris le raisonnement interne du modèle. Avec thinking_level HIGH, une valeur faible peut ne laisser aucune place à la réponse ; augmentez cette valeur si les réponses reviennent vides ou tronquées. Le modèle s'arrête dès qu'il a terminé, donc un plafond plus élevé ne coûte rien de plus pour les réponses courtes. (défaut : 32768) | INT | Oui | 16 à 65536 |

### Entrées Gemini 3.5 Flash

Ces entrées apparaissent lorsque `model` est défini sur `"Gemini 3.5 Flash"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Niveau d'effort de raisonnement interne du modèle avant de répondre. HIGH améliore la qualité sur les tâches difficiles mais consomme davantage de jetons de réflexion et est plus lent. (défaut : "MEDIUM") | COMBO | Oui | `"MINIMAL"`<br>`"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `temperature` | Contrôle le caractère aléatoire. Une valeur plus basse donne un résultat plus ciblé/déterministe, une valeur plus élevée plus créatif. (défaut : 1.0) | FLOAT | Oui | 0.0 à 2.0 |
| `top_p` | Échantillonnage nucleus : échantillonner à partir du plus petit ensemble de jetons dont la probabilité cumulée atteint top_p. (défaut : 0.95) | FLOAT | Oui | 0.0 à 1.0 |
| `max_output_tokens` | Nombre maximal de jetons à générer, y compris le raisonnement interne du modèle. Avec thinking_level HIGH, une valeur faible peut ne laisser aucune place à la réponse ; augmentez cette valeur si les réponses reviennent vides ou tronquées. Le modèle s'arrête dès qu'il a terminé, donc un plafond plus élevé ne coûte rien de plus pour les réponses courtes. (défaut : 32768) | INT | Oui | 16 à 65536 |

### Entrées Gemini 3.1 Pro

Ces entrées apparaissent lorsque `model` est défini sur `"Gemini 3.1 Pro"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Niveau d'effort de raisonnement interne du modèle avant de répondre. HIGH améliore la qualité sur les tâches difficiles mais consomme davantage de jetons de réflexion et est plus lent. (défaut : "HIGH") | COMBO | Oui | `"LOW"`<br>`"HIGH"` |
| `temperature` | Contrôle le caractère aléatoire. Une valeur plus basse donne un résultat plus ciblé/déterministe, une valeur plus élevée plus créatif. (défaut : 1.0) | FLOAT | Oui | 0.0 à 2.0 |
| `top_p` | Échantillonnage nucleus : échantillonner à partir du plus petit ensemble de jetons dont la probabilité cumulée atteint top_p. (défaut : 0.95) | FLOAT | Oui | 0.0 à 1.0 |
| `max_output_tokens` | Nombre maximal de jetons à générer, y compris le raisonnement interne du modèle. Avec thinking_level HIGH, une valeur faible peut ne laisser aucune place à la réponse ; augmentez cette valeur si les réponses reviennent vides ou tronquées. Le modèle s'arrête dès qu'il a terminé, donc un plafond plus élevé ne coûte rien de plus pour les réponses courtes. (défaut : 32768) | INT | Oui | 16 à 65536 |

### Entrées Gemini 3.1 Flash-Lite

Ces entrées apparaissent lorsque `model` est défini sur `"Gemini 3.1 Flash-Lite"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Niveau d'effort de raisonnement interne du modèle avant de répondre. HIGH améliore la qualité sur les tâches difficiles mais consomme davantage de jetons de réflexion et est plus lent. (défaut : "LOW") | COMBO | Oui | `"LOW"`<br>`"HIGH"` |
| `temperature` | Contrôle le caractère aléatoire. Une valeur plus basse donne un résultat plus ciblé/déterministe, une valeur plus élevée plus créatif. (défaut : 1.0) | FLOAT | Oui | 0.0 à 2.0 |
| `top_p` | Échantillonnage nucleus : échantillonner à partir du plus petit ensemble de jetons dont la probabilité cumulée atteint top_p. (défaut : 0.95) | FLOAT | Oui | 0.0 à 1.0 |
| `max_output_tokens` | Nombre maximal de jetons à générer, y compris le raisonnement interne du modèle. Avec thinking_level HIGH, une valeur faible peut ne laisser aucune place à la réponse ; augmentez cette valeur si les réponses reviennent vides ou tronquées. Le modèle s'arrête dès qu'il a terminé, donc un plafond plus élevé ne coûte rien de plus pour les réponses courtes. (défaut : 32768) | INT | Oui | 16 à 65536 |

### Entrées média et fichiers

Les entrées suivantes sont partagées par les quatre modèles et apparaissent aux côtés des entrées spécifiques au modèle.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `images` | Emplacement extensible : connectez 1 à 16 images (`image_1` ... `image_16`). Image(s) facultative(s) à utiliser comme contexte pour le modèle. Jusqu'à 16 images. | IMAGE | Non | 0 à 16 images |
| `audio` | Emplacement extensible : connectez un clip audio (`audio_1`). Clip audio facultatif à utiliser comme contexte pour le modèle. | AUDIO | Non | 0 à 1 clip |
| `video` | Emplacement extensible : connectez un clip vidéo (`video_1`). Clip vidéo facultatif à utiliser comme contexte pour le modèle. | VIDEO | Non | 0 à 1 clip |
| `files` | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Input Files. | GEMINI_INPUT_FILES | Non |  |

**Remarque :** lorsque des médias (images, audio ou vidéo) sont attachés, le nœud télécharge les 10 premiers éléments média vers le stockage ComfyAPI et les transmet sous forme d'URL ; ce budget d'URL est partagé entre tous les types de médias et est consommé dans l'ordre (vidéo d'abord, puis audio, puis images). Tout média restant est encodé en ligne sous forme de données base64, avec une charge utile combinée maximale de 18 Mo. Si la charge utile en ligne dépassait 18 Mo, le nœud générerait une erreur. Le paramètre `prompt` doit contenir au moins un caractère non vide. Définir `seed` sur 0 demande une graine aléatoire.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `output` | La réponse texte générée par le modèle Gemini. Si le modèle ne produit aucun texte, la chaîne « Empty response from Gemini model... » est renvoyée. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `00e0f614303fa723eb787ad763e0b0c6322f89abf43d93b697357527b2fae49c`
