# OpenRouter LLM

Voici la traduction en français de la documentation du nœud OpenRouter LLM, en respectant vos règles :

## Aperçu

Le nœud LLM OpenRouter envoie une invite textuelle à un ensemble sélectionné de modèles de langage populaires disponibles via le service OpenRouter et renvoie la réponse textuelle générée. Il prend en charge les modèles de fournisseurs tels que xAI, DeepSeek, Qwen, Mistral, Z.AI (GLM), Moonshot (Kimi) et Perplexity Sonar, et peut éventuellement inclure des images ou des vidéos dans la requête.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Texte d'entrée pour le modèle. | STRING | Oui | N/A |
| `model` | Le modèle OpenRouter utilisé pour générer la réponse. | STRING | Oui | Plusieurs options disponibles (voir note ci-dessous) |
| `seed` | Graine pour l'échantillonnage. Mettre à 0 pour omettre. La plupart des modèles ne traitent cela qu'à titre indicatif. (par défaut : 0) | INT | Oui | 0 à 2147483647 |
| `system_prompt` | Instructions fondamentales qui dictent le comportement du modèle. (par défaut : "") | STRING | Non | N/A |

**Note sur le paramètre `model :** Les options de modèle disponibles sont construites dynamiquement et peuvent inclure des modèles aux capacités différentes. Certains modèles prennent en charge des fonctionnalités supplémentaires comme l'effort de raisonnement, la recherche web ou les entrées d'images/vidéos. Le nœud validera que le nombre d'images ou de vidéos fournies ne dépasse pas le nombre maximal pris en charge par le modèle.

**Note sur le paramètre `seed` :** Le paramètre `seed` a un comportement "control_after_generate", ce qui signifie qu'il peut être configuré pour changer automatiquement (par exemple, aléatoire, incrémentiel ou fixe) après chaque exécution du nœud, en fonction des paramètres du widget de l'utilisateur.

**Note sur `system_prompt` :** Ce paramètre est facultatif et est marqué comme un paramètre avancé dans l'interface utilisateur.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La réponse textuelle générée par le modèle OpenRouter. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/fr.md)

---
**Source fingerprint (SHA-256):** `24757e36bf2356cc1805a6f071db88ca455e17944695672f19845a4cd1826c8a`
