# Anthropic Claude

Génère des réponses textuelles à partir des modèles Claude d'Anthropic. Fournissez une invite textuelle et éventuellement une ou plusieurs images pour un contexte multimodal ; le nœud renvoie la réponse textuelle générée par le modèle.

## Entrées

Les entrées sont regroupées en paramètres communs, paramètres propres au modèle qui apparaissent lorsqu'un modèle est sélectionné, et images de référence facultatives.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle Claude utilisé pour générer la réponse. La sélection d'un modèle révèle les paramètres propres au modèle ci-dessous. | DYNAMIC_COMBO | Oui | `"Opus 5.5"`<br>`"Opus 5"`<br>`"Opus 4.8"`<br>`"Fable 5.1"`<br>`"Fable 5"`<br>`"Sonnet 5.5"`<br>`"Sonnet 5"`<br>`"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `invite` | Entrée textuelle pour le modèle. (par défaut : chaîne vide) | STRING | Oui | N/A |
| `graine` | La graine détermine si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. (par défaut : 0) | INT | Oui | 0 à 2147483647 |
| `invite système` | Instructions fondamentales qui dictent le comportement du modèle. (par défaut : chaîne vide) | STRING | Non | N/A |

### Entrées Opus 5.5, Opus 5, Fable 5.1 et Fable 5

Ces quatre modèles partagent les mêmes paramètres. Ils n'exposent pas de paramètre de température, et le raisonnement est toujours activé.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `max_tokens` | Nombre maximal de tokens à générer (inclut les tokens de raisonnement lorsqu'ils sont activés). (par défaut : 32768) | INT | Oui | 1024 à 64000 (Opus 5.5)<br>4096 à 64000 (Opus 5, Fable 5.1, Fable 5) |
| `reasoning_effort` | Effort de réflexion étendue. Le raisonnement est toujours activé pour ces modèles. (par défaut : "high") | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |

### Entrées Opus 4.8, Sonnet 5.5 et Sonnet 5

Ces trois modèles partagent les mêmes paramètres. Ils n'exposent pas de paramètre de température.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `max_tokens` | Nombre maximal de tokens à générer (inclut les tokens de raisonnement lorsqu'ils sont activés). (par défaut : 32768) | INT | Oui | 1024 à 64000 (Sonnet 5.5)<br>4096 à 64000 (Opus 4.8, Sonnet 5) |
| `reasoning_effort` | Effort de réflexion étendue. `"off"` désactive le raisonnement. (par défaut : "off") | COMBO | Oui | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |

### Entrées Opus 4.7, Opus 4.6, Sonnet 4.6 et Sonnet 4.5

Ces quatre modèles partagent les mêmes paramètres.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `max_tokens` | Nombre maximal de tokens à générer (inclut les tokens de raisonnement lorsqu'ils sont activés). (par défaut : 32768) | INT | Oui | 4096 à 64000 |
| `temperature` | Contrôle le caractère aléatoire. 0.0 est déterministe, 1.0 est le plus aléatoire. Ignoré pour Opus 4.7 et tout modèle lorsque `reasoning_effort` est défini. (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `reasoning_effort` | Effort de réflexion étendue. `"off"` désactive le raisonnement. (par défaut : "off") | COMBO | Oui | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

`reasoning_effort` propose `"off"`, `"low"`, `"medium"` et `"high"` sur les quatre modèles. Opus 4.7, Opus 4.6 et Sonnet 4.6 acceptent en plus `"max"`, et Opus 4.7 accepte également `"xhigh"`.

### Entrées Haiku 4.5

Ce modèle n'expose pas de paramètre `reasoning_effort`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `max_tokens` | Nombre maximal de tokens à générer (inclut les tokens de raisonnement lorsqu'ils sont activés). (par défaut : 32768) | INT | Oui | 4096 à 64000 |
| `temperature` | Contrôle le caractère aléatoire. 0.0 est déterministe, 1.0 est le plus aléatoire. Ignoré pour Opus 4.7 et tout modèle lorsque `reasoning_effort` est défini. (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Image(s) facultative(s) à utiliser comme contexte pour le modèle. Jusqu'à 20 images. Emplacement extensible : connectez 1 à 20 éléments (`image_1` ... `image_20`). | IMAGE | Non | 0 à 20 images |

### Contraintes sur les paramètres

- **Limite d'images :** Un maximum de 20 images peut être fourni par requête. Connecter plus de 20 images déclenche une erreur.
- **Invite requise :** L'invite doit contenir au moins un caractère non blanc. Une invite vide déclenche une erreur de validation.
- **Gestion de la température :** Lorsque la réflexion est activée, l'API Anthropic exige que la température ne soit pas définie (elle vaut 1.0 par défaut). Opus 5.5, Opus 5, Opus 4.8, Fable 5.1, Fable 5, Sonnet 5.5 et Sonnet 5 n'exposent pas de paramètre de température. Opus 4.7 ignore `temperature`, et tout modèle dont `reasoning_effort` est défini sur autre chose que `"off"` l'ignore également.
- **Comportement du raisonnement et de la réflexion :** Le paramètre `reasoning_effort` contrôle si la réflexion est activée. Opus 5.5, Opus 5, Fable 5.1 et Fable 5 ont toujours le raisonnement activé. Haiku 4.5 ne prend pas en charge le raisonnement. Lorsque la réflexion est activée, le nœud utilise le mode de réflexion approprié pour le modèle sélectionné, soit adaptatif, soit basé sur un budget. En mode budget, le budget de tokens de raisonnement est plafonné pour laisser au moins 1024 tokens à la réponse réelle. Lorsque `reasoning_effort` est `"off"` sur Sonnet 5.5, la requête utilise la réflexion `between_tools` au lieu de la réflexion désactivée, donc la réponse ne contient toujours pas de raisonnement.
- **Minimum de `max_tokens` :** `max_tokens` accepte des valeurs à partir de 1024 sur Opus 5.5 et Sonnet 5.5, et à partir de 4096 sur tous les autres modèles.
- **Refus de sécurité :** Si Claude refuse de répondre à la requête pour des raisons de sécurité, le nœud déclenche une erreur vous demandant de reformuler l'invite ou d'essayer un autre modèle.
- **Texte de sortie :** Les blocs de réflexion et de raisonnement ne sont pas inclus dans la sortie ; seul le texte généré est renvoyé.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La réponse textuelle générée par le modèle Claude. Les blocs de réflexion/raisonnement ne sont pas inclus. Si aucun texte n'est généré, renvoie "Empty response from Claude model." | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/fr.md)

---
**Source fingerprint (SHA-256):** `35b737da0f4c3a9da72910bf2053b18ae6a5c60989dc9607b61037623bc94e38`
