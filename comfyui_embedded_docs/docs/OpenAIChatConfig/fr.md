> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/fr.md)

Le nœud OpenAIChatConfig permet de définir des options de configuration supplémentaires pour le nœud OpenAI Chat. Il fournit des paramètres avancés qui contrôlent la manière dont le modèle génère les réponses, y compris le comportement de troncation, les limites de longueur de sortie et les instructions personnalisées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `truncation` | COMBO | Oui | `"auto"`<br>`"disabled"` | La stratégie de troncation à utiliser pour la réponse du modèle. auto : Si le contexte de cette réponse et des précédentes dépasse la taille de la fenêtre de contexte du modèle, le modèle tronquera la réponse pour s'adapter à la fenêtre de contexte en supprimant les éléments d'entrée au milieu de la conversation. disabled : Si une réponse du modèle dépasse la taille de la fenêtre de contexte pour un modèle, la requête échouera avec une erreur 400 (par défaut : "auto") |
| `max_output_tokens` | INT | Non | 16-16384 | Une limite supérieure pour le nombre de jetons qui peuvent être générés pour une réponse, incluant les jetons de sortie visibles (par défaut : 4096) |
| `instructions` | STRING | Non | - | Instructions supplémentaires pour la réponse du modèle (saisie multiligne supportée) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `OPENAI_CHAT_CONFIG` | OPENAI_CHAT_CONFIG | Objet de configuration contenant les paramètres spécifiés pour utilisation avec les nœuds OpenAI Chat |
