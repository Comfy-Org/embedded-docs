# OpenRouter LLM

Le nœud OpenRouter LLM envoie une invite textuelle à un ensemble sélectionné de modèles de langage populaires disponibles via le service OpenRouter et renvoie la réponse textuelle générée. Il prend en charge les modèles d’Anthropic (Claude), OpenAI (GPT), Google (Gemini), xAI (Grok), DeepSeek, Qwen, Mistral, Z.AI (GLM), Moonshot (Kimi) et Perplexity Sonar, et peut éventuellement inclure des images ou des vidéos comme entrées de référence dans la requête.

## Entrées

Lorsqu’un modèle est sélectionné dans le sélecteur `model`, le nœud affiche des widgets spécifiques au modèle au-dessus des entrées communes — effort de raisonnement, taille de recherche web et/ou emplacements de médias de référence — selon les capacités du modèle choisi.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Texte envoyé au modèle. | STRING | Oui | N/A |
| `model` | Le modèle OpenRouter utilisé pour générer la réponse. | DYNAMIC_COMBO | Oui | Plusieurs options disponibles (voir les sections des modèles ci-dessous) |
| `seed` | Graine pour l’échantillonnage. Mettre à 0 pour l’omettre. La plupart des modèles ne considèrent cela que comme une indication. (défaut : 0) | INT | Oui | 0 à 2147483647 |
| `system_prompt` | Instructions de base qui déterminent le comportement du modèle. (défaut : "") | STRING | Non | N/A |

### Entrées Anthropic Claude Models

Communes à `anthropic/claude-opus-5`, `anthropic/claude-opus-4.8`, `anthropic/claude-opus-4.7`, `anthropic/claude-fable-5`, `anthropic/claude-sonnet-5` et `anthropic/claude-haiku-4.5`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. 'off' désactive entièrement le raisonnement. (défaut : "off") | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

Ces modèles prennent en charge jusqu’à 20 images de référence (voir Entrées de référence).

### Entrées OpenAI GPT Models

Communes à `openai/gpt-5.6-sol-pro`, `openai/gpt-5.6-sol`, `openai/gpt-5.6-terra-pro`, `openai/gpt-5.6-terra`, `openai/gpt-5.6-luna-pro`, `openai/gpt-5.6-luna`, `openai/gpt-5.5-pro` et `openai/gpt-5.5`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. 'off' désactive entièrement le raisonnement. (défaut : "off") | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

Ces modèles prennent en charge jusqu’à 20 images de référence (voir Entrées de référence).

### Entrées Google Gemini 3.5 Flash

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. 'off' désactive entièrement le raisonnement. (défaut : "off") | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

Ce modèle prend en charge jusqu’à 20 images de référence et jusqu’à 4 vidéos de référence (voir Entrées de référence).

### Entrées xAI Grok Models

Communes à `x-ai/grok-4.5`, `x-ai/grok-4.20` et `x-ai/grok-4.3`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. 'off' désactive entièrement le raisonnement. (défaut : "off") | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

Ces modèles prennent en charge jusqu’à 20 images de référence (voir Entrées de référence).

### Entrées DeepSeek Models

Communes à `deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash` et `deepseek/deepseek-v3.2`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. 'off' désactive entièrement le raisonnement. (défaut : "off") | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

Modèles textuels uniquement — aucune image ou vidéo de référence.

### Entrées Qwen 3.6 Max Preview

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. 'off' désactive entièrement le raisonnement. (défaut : "off") | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

Modèle textuel uniquement — aucune image ou vidéo de référence.

### Entrées Qwen 3.6 Plus et Qwen 3.6 Flash

Communes à `qwen/qwen3.6-plus` et `qwen/qwen3.6-flash`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. 'off' désactive entièrement le raisonnement. (défaut : "off") | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

Ces modèles prennent en charge jusqu’à 10 images de référence et jusqu’à 4 vidéos de référence (voir Entrées de référence).

### Entrées Mistral Large 2512

Aucune entrée spécifique au profil (profil standard). Ce modèle prend en charge jusqu’à 8 images de référence (voir Entrées de référence).

### Entrées Mistral Medium 3.5

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. 'off' désactive entièrement le raisonnement. (défaut : "off") | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

Ce modèle prend en charge jusqu’à 8 images de référence (voir Entrées de référence).

### Entrées Z.AI GLM Models

Communes à `z-ai/glm-4.6` et `z-ai/glm-5`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. 'off' désactive entièrement le raisonnement. (défaut : "off") | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

Modèles textuels uniquement — aucune image ou vidéo de référence.

### Entrées Moonshot Kimi K3 et K2.6

Communes à `moonshotai/kimi-k3` et `moonshotai/kimi-k2.6`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. 'off' désactive entièrement le raisonnement. (défaut : "off") | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

Ces modèles prennent en charge jusqu’à 10 images de référence (voir Entrées de référence).

### Entrées Moonshot Kimi K2 Thinking

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Effort de raisonnement. 'off' désactive entièrement le raisonnement. (défaut : "off") | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

Modèle textuel uniquement — aucune image ou vidéo de référence.

### Entrées Perplexity Sonar Pro

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | Quantité de contexte de recherche web à récupérer. Plus la valeur est élevée, plus le résultat est fiable, mais plus le traitement est lent et coûteux. (défaut : "medium") | COMBO | Non | "low"<br>"medium"<br>"high" |

Modèle textuel uniquement — aucune image ou vidéo de référence.

### Entrées Perplexity Sonar Reasoning Pro et Sonar Deep Research

Communes à `perplexity/sonar-reasoning-pro` et `perplexity/sonar-deep-research`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | Quantité de contexte de recherche web à récupérer. Plus la valeur est élevée, plus le résultat est fiable, mais plus le traitement est lent et coûteux. (défaut : "medium") | COMBO | Non | "low"<br>"medium"<br>"high" |
| `reasoning_effort` | Effort de raisonnement. 'off' désactive entièrement le raisonnement. (défaut : "off") | COMBO | Non | "off"<br>"low"<br>"medium"<br>"high" |

Modèles textuels uniquement — aucune image ou vidéo de référence.

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `images` | Image(s) de référence facultative(s), envoyée(s) sous forme d’URL. Emplacement extensible : connectez 1..N entrées d’image (`image_1`, `image_2`, ...) ; la limite de nombre dépend du modèle sélectionné (voir les sections des modèles). | IMAGE | Non | 0 à 20 (selon le modèle : 8, 10 ou 20) |
| `videos` | Vidéo(s) de référence facultative(s), envoyée(s) sous forme d’URL. Emplacement extensible : connectez 1..N entrées vidéo (`video_1`, `video_2`, ...) ; la limite de nombre dépend du modèle sélectionné (voir les sections des modèles). | VIDEO | Non | 0 à 4 (selon le modèle) |

**Notes :**

- **Modèles disponibles :** Les options de modèle disponibles sont construites dynamiquement et incluent des modèles aux capacités différentes. La liste complète des 34 modèles est la suivante :
  - Anthropic : `anthropic/claude-opus-5`, `anthropic/claude-opus-4.8`, `anthropic/claude-opus-4.7`, `anthropic/claude-fable-5`, `anthropic/claude-sonnet-5`, `anthropic/claude-haiku-4.5`
  - OpenAI : `openai/gpt-5.6-sol-pro`, `openai/gpt-5.6-sol`, `openai/gpt-5.6-terra-pro`, `openai/gpt-5.6-terra`, `openai/gpt-5.6-luna-pro`, `openai/gpt-5.6-luna`, `openai/gpt-5.5-pro`, `openai/gpt-5.5`
  - Google : `google/gemini-3.5-flash`
  - xAI : `x-ai/grok-4.5`, `x-ai/grok-4.20`, `x-ai/grok-4.3`
  - DeepSeek : `deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash`, `deepseek/deepseek-v3.2`
  - Qwen : `qwen/qwen3.6-max-preview`, `qwen/qwen3.6-plus`, `qwen/qwen3.6-flash`
  - Mistral : `mistralai/mistral-large-2512`, `mistralai/mistral-medium-3-5`
  - Z.AI : `z-ai/glm-4.6`, `z-ai/glm-5`
  - Moonshot : `moonshotai/kimi-k3`, `moonshotai/kimi-k2.6`, `moonshotai/kimi-k2-thinking`
  - Perplexity : `perplexity/sonar-pro`, `perplexity/sonar-reasoning-pro`, `perplexity/sonar-deep-research`

- **Contraintes d’image et de vidéo :** Le nombre maximal d’images et de vidéos de référence dépend du modèle sélectionné. Le nœud génère une erreur si le nombre total d’images ou de vidéos fournies dépasse la limite du modèle. Les modèles sans prise en charge d’images ou de vidéos n’affichent pas les emplacements de référence correspondants.

- **Comportement du raisonnement :** Lorsque `reasoning_effort` est défini sur une valeur autre que "off", la requête demande au fournisseur de raisonner en interne sans renvoyer la trace de raisonnement.

- **Comportement de la graine :** Le paramètre `seed` a un comportement "control_after_generate", ce qui signifie qu’il peut être configuré pour changer automatiquement (par exemple, aléatoire, incrément ou fixe) après chaque exécution du nœud, selon les réglages des widgets de l’utilisateur.

- **Invite système :** Le paramètre `system_prompt` est facultatif et est marqué comme paramètre avancé dans l’interface utilisateur.

- **Cas d’erreur :** Le nœud génère une erreur si l’invite est vide après suppression des espaces, si OpenRouter renvoie une erreur, si le modèle sélectionné refuse de répondre, ou si la réponse ne contient ni choix ni message. Un badge de prix sur le nœud affiche une estimation approximative du coût pour 1K tokens selon le modèle sélectionné.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `output` | La réponse textuelle générée par le modèle OpenRouter. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/fr.md)

---
**Source fingerprint (SHA-256):** `534ab9ecc12e35a23a4d8f3e10f4f82d95db8e902ac8a2f2ee0ea68246516f62`
