# OpenRouter LLM

Le nœud OpenRouter LLM envoie une invite textuelle (et éventuellement des images ou des vidéos) à un ensemble sélectionné de modèles de langage disponibles via le service OpenRouter et renvoie la réponse textuelle générée. Il prend en charge les modèles d'Anthropic (Claude), d'OpenAI (GPT), de Google (Gemini), de xAI (Grok), de DeepSeek, de Qwen, de Mistral, de Z.AI (GLM), de Moonshot (Kimi) et de Perplexity Sonar, et affiche des options spécifiques au modèle, telles que l’effort de raisonnement et le contexte de recherche Web, lorsque le modèle sélectionné les prend en charge.

## Entrées

Le sélecteur `model` est dynamique : le choix d’un modèle révèle des widgets spécifiques au modèle (effort de raisonnement, contexte de recherche Web, emplacements d’image et de vidéo) en plus des entrées communes ci-dessous.

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------|----------|-------|
| `model` | Le modèle OpenRouter utilisé pour générer la réponse. La sélection d’un modèle révèle ses entrées spécifiques au modèle (voir les sections relatives aux modèles ci-dessous). | DYNAMIC_COMBO | Oui | 34 options de modèles OpenRouter sélectionnées |
| `prompt` | Entrée textuelle pour le modèle. Doit contenir au moins un caractère non blanc. | STRING | Oui | Texte multiligne |
| `seed` | Graine pour l’échantillonnage. Réglez sur 0 pour l’omettre. La plupart des modèles ne considèrent cette valeur que comme une indication. (par défaut : 0) | INT | Oui | 0 à 2147483647 |
| `system_prompt` | Instructions fondamentales qui déterminent le comportement du modèle. (par défaut : "") | STRING | Non | Texte multiligne |

**Remarque sur `seed` :** Ce paramètre a un comportement « control_after_generate », ce qui signifie qu’il peut être configuré pour changer automatiquement (par exemple, tirage aléatoire, incrémentation ou valeur fixe) après chaque exécution du nœud, en fonction des paramètres du widget de l’utilisateur.

**Remarque sur `system_prompt` :** Ce paramètre est facultatif et est marqué comme paramètre avancé dans l’interface utilisateur.

### Entrées Anthropic Claude

Entrées partagées par `anthropic/claude-opus-5`, `anthropic/claude-opus-4.8`, `anthropic/claude-opus-4.7`, `anthropic/claude-fable-5`, `anthropic/claude-sonnet-5` et `anthropic/claude-haiku-4.5`.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. « off » désactive entièrement le raisonnement. (par défaut : « off ») | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

### Entrées OpenAI GPT

Entrées partagées par `openai/gpt-5.6-sol-pro`, `openai/gpt-5.6-sol`, `openai/gpt-5.6-terra-pro`, `openai/gpt-5.6-terra`, `openai/gpt-5.6-luna-pro`, `openai/gpt-5.6-luna`, `openai/gpt-5.5-pro` et `openai/gpt-5.5`.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. « off » désactive entièrement le raisonnement. (par défaut : « off ») | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

### Entrées Google Gemini 3.5 Flash

S’applique à `google/gemini-3.5-flash`.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. « off » désactive entièrement le raisonnement. (par défaut : « off ») | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

### Entrées xAI Grok

Entrées partagées par `x-ai/grok-4.5`, `x-ai/grok-4.20` et `x-ai/grok-4.3`.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. « off » désactive entièrement le raisonnement. (par défaut : « off ») | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

### Entrées DeepSeek

Entrées partagées par `deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash` et `deepseek/deepseek-v3.2`.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. « off » désactive entièrement le raisonnement. (par défaut : « off ») | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

### Entrées Qwen 3.6 Plus et Flash

Entrées partagées par `qwen/qwen3.6-plus` et `qwen/qwen3.6-flash`.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. « off » désactive entièrement le raisonnement. (par défaut : « off ») | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

### Entrées Mistral Large 2512

S’applique à `mistralai/mistral-large-2512`. Ce modèle n’ajoute aucun widget de paramètre spécifique ; uniquement les entrées communes et l’emplacement de référence `images` s’appliquent.

### Entrées Mistral Medium 3.5

S’applique à `mistralai/mistral-medium-3-5`.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. « off » désactive entièrement le raisonnement. (par défaut : « off ») | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

### Entrées Moonshot Kimi K3 et K2.6

Entrées partagées par `moonshotai/kimi-k3` et `moonshotai/kimi-k2.6`.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. « off » désactive entièrement le raisonnement. (par défaut : « off ») | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

### Entrées Perplexity Sonar Pro

S’applique à `perplexity/sonar-pro`.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | Quantité de contexte de recherche Web à récupérer. Une valeur plus élevée donne des réponses mieux étayées, mais plus lentes/coûteuses. (par défaut : « medium ») | COMBO | Non | "low"<br>"medium"<br>"high" |

### Entrées Perplexity Sonar Reasoning Pro et Deep Research

Entrées partagées par `perplexity/sonar-reasoning-pro` et `perplexity/sonar-deep-research`.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | Quantité de contexte de recherche Web à récupérer. Une valeur plus élevée donne des réponses mieux étayées, mais plus lentes/coûteuses. (par défaut : « medium ») | COMBO | Non | "low"<br>"medium"<br>"high" |
| `reasoning_effort` | Effort de raisonnement. « off » désactive entièrement le raisonnement. (par défaut : « off ») | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

### Modèles à raisonnement uniquement

Entrées partagées par `qwen/qwen3.6-max-preview`, `z-ai/glm-4.6`, `z-ai/glm-5` et `moonshotai/kimi-k2-thinking`.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. « off » désactive entièrement le raisonnement. (par défaut : « off ») | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

### Entrées de référence

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------|----------|-------|
| `images` | Image(s) de référence facultative(s) — envoyées sous forme d’URL. Emplacement extensible : connectez `image_1` à `image_N`, où N dépend du modèle sélectionné. | IMAGE | Non | 0 à N images (N = 8, 10 ou 20 selon le modèle) |
| `videos` | Vidéo(s) de référence facultative(s) — envoyées sous forme d’URL. Emplacement extensible : connectez `video_1` à `video_N`. Disponible uniquement sur les modèles prenant en charge la vidéo. | VIDEO | Non | 0 à 4 vidéos |

**Remarque sur les capacités et limites des modèles :**

- Prise en charge des images : jusqu’à 20 images pour les modèles Anthropic Claude, OpenAI GPT, Google Gemini 3.5 Flash et xAI Grok ; jusqu’à 10 images pour Qwen 3.6 Plus/Flash et Moonshot Kimi K3/K2.6 ; jusqu’à 8 images pour Mistral Large 2512 et Mistral Medium 3.5. Les modèles DeepSeek, Qwen 3.6 Max Preview, Z.AI GLM, Moonshot Kimi K2 Thinking et Perplexity Sonar n’acceptent pas d’images.
- Prise en charge des vidéos : seuls `google/gemini-3.5-flash`, `qwen/qwen3.6-plus` et `qwen/qwen3.6-flash` acceptent les vidéos, avec un maximum de 4 vidéos.
- Le nœud génère une erreur si le nombre d’images ou de vidéos connectées dépasse ce que le modèle sélectionné prend en charge.
- Lorsque `reasoning_effort` est défini sur « low », « medium » ou « high », le modèle raisonne en interne mais ne renvoie pas la trace de raisonnement ; « off » désactive entièrement le raisonnement.
- Le widget `search_context_size` n’apparaît que pour les modèles Perplexity Sonar. Les widgets `reasoning_effort` et `search_context_size` sont marqués comme paramètres avancés.
- Le nœud affiche un badge de prix approximatif (USD par 1 000 jetons) en fonction du modèle sélectionné.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `output` | La réponse textuelle générée par le modèle OpenRouter sélectionné. | STRING |

**Remarque sur les erreurs :** le nœud génère une erreur si OpenRouter renvoie une erreur d’API, une réponse vide (aucun choix) ou un refus du modèle.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/fr.md)

---
**Source fingerprint (SHA-256):** `534ab9ecc12e35a23a4d8f3e10f4f82d95db8e902ac8a2f2ee0ea68246516f62`
