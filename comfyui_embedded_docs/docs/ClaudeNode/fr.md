# Anthropic Claude

```markdown
Génère des réponses textuelles à partir d'un modèle Anthropic Claude. Ce nœud envoie une invite textuelle et des images facultatives à un modèle Claude, puis renvoie la réponse textuelle générée.

## Entrées

Le paramètre `model` est un sélecteur dynamique : lorsque vous choisissez un modèle, des paramètres supplémentaires spécifiques au modèle tels que la limite de jetons, la température et l'effort de raisonnement apparaissent en dessous.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Entrée de texte destinée au modèle. Doit être non vide après suppression des espaces. (défaut : chaîne vide) | STRING | Oui | N/A |
| `model` | Le modèle Claude utilisé pour générer la réponse. | DYNAMIC_COMBO | Oui | `"Opus 5"`<br>`"Opus 4.8"`<br>`"Fable 5"`<br>`"Sonnet 5"`<br>`"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `seed` | Le paramètre `seed` contrôle si le nœud doit s'exécuter à nouveau ; les résultats sont non déterministes quelle que soit la graine. (défaut : 0) | INT | Oui | 0 à 2147483647 |
| `images` | Image(s) facultative(s) à utiliser comme contexte pour le modèle. Emplacement extensible : connectez `image_1` à `image_20` ; jusqu'à 20 images. (défaut : aucune) | IMAGE | Non | 0 à 20 images |
| `system_prompt` | Instructions fondamentales qui déterminent le comportement du modèle. (défaut : chaîne vide) | STRING | Non | N/A |

### Entrées Opus 5 et Fable 5

Partagées par Opus 5 et Fable 5. Ces modèles utilisent toujours la réflexion approfondie et n'exposent pas de paramètre de température.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `max_tokens` | Nombre maximal de jetons à générer (inclut les jetons de raisonnement lorsqu'ils sont activés). (défaut : 32768) | INT | Oui | 4096 à 64000 |
| `reasoning_effort` | Effort de réflexion approfondie. Le raisonnement est toujours activé pour ce modèle. (défaut : "high") | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"` |

### Entrées Opus 4.8 et Sonnet 5

Partagées par Opus 4.8 et Sonnet 5. Ces modèles n'exposent pas de paramètre de température.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `max_tokens` | Nombre maximal de jetons à générer (inclut les jetons de raisonnement lorsqu'ils sont activés). (défaut : 32768) | INT | Oui | 4096 à 64000 |
| `reasoning_effort` | Effort de réflexion approfondie. La valeur « off » désactive le raisonnement. (défaut : « off ») | COMBO | Oui | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Entrées Opus 4.7, Opus 4.6, Sonnet 4.6 et Sonnet 4.5

Partagées par Opus 4.7, Opus 4.6, Sonnet 4.6 et Sonnet 4.5. Pour Opus 4.7, le paramètre de température est affiché mais ignoré, et l'API utilise la valeur par défaut de 1.0.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `max_tokens` | Nombre maximal de jetons à générer (inclut les jetons de raisonnement lorsqu'ils sont activés). (défaut : 32768) | INT | Oui | 4096 à 64000 |
| `temperature` | Contrôle le caractère aléatoire. 0.0 est déterministe, 1.0 est le plus aléatoire. Ignoré pour Opus 4.7 et pour tout modèle lorsque `reasoning_effort` est défini. (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas de 0.01) |
| `reasoning_effort` | Effort de réflexion approfondie. La valeur « off » désactive le raisonnement. (défaut : « off ») | COMBO | Oui | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Entrées Haiku 4.5

Ce modèle ne prend pas en charge la réflexion approfondie, donc aucun paramètre `reasoning_effort` n'est disponible.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `max_tokens` | Nombre maximal de jetons à générer (inclut les jetons de raisonnement lorsqu'ils sont activés). (défaut : 32768) | INT | Oui | 4096 à 64000 |
| `temperature` | Contrôle le caractère aléatoire. 0.0 est déterministe, 1.0 est le plus aléatoire. (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas de 0.01) |

### Contraintes de paramètres

- Jusqu'à 20 images peuvent être fournies par requête. Le nombre total de pixels pour les images téléchargées est limité à 1568 × 1568 pixels.
- La température n'est pas configurable pour Opus 5, Fable 5, Opus 4.8 et Sonnet 5. Lorsqu'un paramètre de température est disponible, il est ignoré pour Opus 4.7 et pour tout modèle où `reasoning_effort` est défini sur une valeur autre que « off ».
- Le raisonnement est toujours activé pour Opus 5 et Fable 5, donc les options `reasoning_effort` pour ces modèles n'incluent pas « off ». Le modèle Haiku 4.5 ne prend pas en charge la réflexion approfondie et ne possède donc aucun paramètre `reasoning_effort`.
- Si Claude refuse de répondre à une demande pour des raisons de sécurité, le nœud lève une erreur au lieu de renvoyer du texte.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La réponse textuelle générée par le modèle Claude. Si aucun texte visible n'est généré, la sortie est `"Empty response from Claude model."` Les blocs de réflexion ou de raisonnement ne sont pas inclus dans la sortie. | STRING |
```

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/fr.md)

---
**Source fingerprint (SHA-256):** `b0381e7981e5886d66b6976c7ddcad3f142bdd803271a6ac8567293dcddaa98a`
