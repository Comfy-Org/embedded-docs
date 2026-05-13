> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/fr.md)

Voici la traduction en français de la documentation du nœud OpenAIChatConfig :

Le nœud OpenAIChatConfig permet de définir des options de configuration supplémentaires pour le nœud OpenAI Chat. Il offre des paramètres avancés qui contrôlent la manière dont le modèle génère les réponses, notamment le comportement de troncature, les limites de longueur de sortie et les instructions personnalisées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `truncation` | COMBO | Oui | `"auto"`<br>`"disabled"` | La stratégie de troncature à utiliser pour la réponse du modèle. auto : Si le contexte de cette réponse et des précédentes dépasse la taille de la fenêtre de contexte du modèle, celui-ci tronquera la réponse pour l'adapter à la fenêtre de contexte en supprimant des éléments d'entrée au milieu de la conversation. disabled : Si une réponse du modèle dépasse la taille de la fenêtre de contexte pour un modèle, la requête échouera avec une erreur 400 (par défaut : "auto") |
| `max_output_tokens` | INT | Non | 16 à 16384 | Une limite supérieure pour le nombre de jetons pouvant être générés pour une réponse, y compris les jetons de sortie visibles (par défaut : 4096) |
| `instructions` | STRING | Non | - | Instructions pour le modèle sur la manière de générer la réponse (saisie multiligne prise en charge) |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `OPENAI_CHAT_CONFIG` | OPENAI_CHAT_CONFIG | Objet de configuration contenant les paramètres spécifiés pour une utilisation avec les nœuds OpenAI Chat |

---
**Source fingerprint (SHA-256):** `6d956aa1bc7f822c18ddaa55cd2345dad947fd93833de25a957f49878484af97`
