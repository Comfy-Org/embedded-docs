# Google Gemini

Générez des réponses textuelles avec les modèles Gemini de Google. Fournissez une invite textuelle et, facultativement, une ou plusieurs images, clips audio, vidéos ou fichiers comme contexte multimodal.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle Gemini utilisé pour générer la réponse. | DYNAMIC_COMBO | Oui | `"Gemini 3.5 Flash"`<br>`"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |
| `prompt` | Entrée textuelle fournie au modèle. Incluez des instructions détaillées, des questions ou du contexte. Doit contenir au moins un caractère non blanc. (par défaut : "") | STRING | Oui |  |
| `seed` | Graine pour l'échantillonnage. Mettez à 0 pour obtenir une graine aléatoire. La sortie déterministe n'est pas garantie. (par défaut : 42) | INT | Oui | 0 à 2147483647 |
| `system_prompt` | Instructions fondamentales qui dictent le comportement du modèle. (par défaut : "") | STRING | Non |  |

### Entrées Gemini 3.5 Flash

Ces entrées apparaissent lorsque `model` est défini sur `"Gemini 3.5 Flash"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `thinking_level` | Le niveau d'effort de raisonnement interne avant de répondre. HIGH améliore la qualité sur les tâches difficiles mais coûte plus de jetons (de réflexion) et est plus lent. (par défaut : "MEDIUM") | COMBO | Oui | `"MINIMAL"`<br>`"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `temperature` | Contrôle le caractère aléatoire. Plus bas est plus ciblé/déterministe, plus haut est plus créatif. (par défaut : 1.0) | FLOAT | Oui | 0.0 à 2.0 |
| `top_p` | Échantillonnage par noyau : échantillonner à partir du plus petit ensemble de jetons dont la probabilité cumulée atteint top_p. (par défaut : 0.95) | FLOAT | Oui | 0.0 à 1.0 |
| `max_output_tokens` | Nombre maximal de jetons à générer, y compris le raisonnement interne du modèle. Avec `thinking_level` HIGH, une valeur faible peut ne laisser aucune place à la réponse ; augmentez cette valeur si les réponses reviennent vides ou tronquées. Le modèle s'arrête tôt une fois terminé, donc un plafond plus élevé ne coûte rien de plus pour les réponses courtes. (par défaut : 32768) | INT | Oui | 16 à 65536 |

### Entrées Gemini 3.1 Pro

Ces entrées apparaissent lorsque `model` est défini sur `"Gemini 3.1 Pro"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `thinking_level` | Le niveau d'effort de raisonnement interne avant de répondre. HIGH améliore la qualité sur les tâches difficiles mais coûte plus de jetons (de réflexion) et est plus lent. (par défaut : "HIGH") | COMBO | Oui | `"LOW"`<br>`"HIGH"` |
| `temperature` | Contrôle le caractère aléatoire. Plus bas est plus ciblé/déterministe, plus haut est plus créatif. (par défaut : 1.0) | FLOAT | Oui | 0.0 à 2.0 |
| `top_p` | Échantillonnage par noyau : échantillonner à partir du plus petit ensemble de jetons dont la probabilité cumulée atteint top_p. (par défaut : 0.95) | FLOAT | Oui | 0.0 à 1.0 |
| `max_output_tokens` | Nombre maximal de jetons à générer, y compris le raisonnement interne du modèle. Avec `thinking_level` HIGH, une valeur faible peut ne laisser aucune place à la réponse ; augmentez cette valeur si les réponses reviennent vides ou tronquées. Le modèle s'arrête tôt une fois terminé, donc un plafond plus élevé ne coûte rien de plus pour les réponses courtes. (par défaut : 32768) | INT | Oui | 16 à 65536 |

### Entrées Gemini 3.1 Flash-Lite

Ces entrées apparaissent lorsque `model` est défini sur `"Gemini 3.1 Flash-Lite"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `thinking_level` | Le niveau d'effort de raisonnement interne avant de répondre. HIGH améliore la qualité sur les tâches difficiles mais coûte plus de jetons (de réflexion) et est plus lent. (par défaut : "LOW") | COMBO | Oui | `"LOW"`<br>`"HIGH"` |
| `temperature` | Contrôle le caractère aléatoire. Plus bas est plus ciblé/déterministe, plus haut est plus créatif. (par défaut : 1.0) | FLOAT | Oui | 0.0 à 2.0 |
| `top_p` | Échantillonnage par noyau : échantillonner à partir du plus petit ensemble de jetons dont la probabilité cumulée atteint top_p. (par défaut : 0.95) | FLOAT | Oui | 0.0 à 1.0 |
| `max_output_tokens` | Nombre maximal de jetons à générer, y compris le raisonnement interne du modèle. Avec `thinking_level` HIGH, une valeur faible peut ne laisser aucune place à la réponse ; augmentez cette valeur si les réponses reviennent vides ou tronquées. Le modèle s'arrête tôt une fois terminé, donc un plafond plus élevé ne coûte rien de plus pour les réponses courtes. (par défaut : 32768) | INT | Oui | 16 à 65536 |

### Entrées de médias et de fichiers

Les entrées suivantes sont partagées par les trois modèles et apparaissent en plus des entrées spécifiques à chaque modèle.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Emplacement extensible : connectez 1 à 16 images (`image_1` ... `image_16`). Image(s) facultative(s) à utiliser comme contexte pour le modèle. | IMAGE | Non | 0 à 16 images |
| `audio` | Emplacement extensible : connectez un clip audio (`audio_1`). Clip audio facultatif à utiliser comme contexte pour le modèle. | AUDIO | Non | 0 à 1 clip |
| `video` | Emplacement extensible : connectez un clip vidéo (`video_1`). Clip vidéo facultatif à utiliser comme contexte pour le modèle. | VIDEO | Non | 0 à 1 clip |
| `files` | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Input Files. | GEMINI_INPUT_FILES | Non |  |

**Remarque :** Lorsque des médias (images, audio ou vidéo) sont joints, le nœud télécharge les 10 premiers éléments médiatiques vers le stockage ComfyAPI et les transmet sous forme d'URL ; ce budget d'URL est partagé entre tous les types de médias et est consommé dans l'ordre (vidéo d'abord, puis audio, puis images). Tout média restant est encodé directement en base64 dans la charge utile, avec une charge utile combinée maximale de 18 Mo. Si la charge utile intégrée dépasse 18 Mo, le nœud génère une erreur. Le paramètre `prompt` doit contenir au moins un caractère non blanc. Définir `seed` sur 0 demande une graine aléatoire.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La réponse textuelle générée par le modèle Gemini. Si le modèle ne produit aucun texte, la chaîne "Empty response from Gemini model..." est renvoyée. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `e88c253d9ae987ab91b0fb6b0b55cfd9cd3671438770afcedd844f236b30dc36`
