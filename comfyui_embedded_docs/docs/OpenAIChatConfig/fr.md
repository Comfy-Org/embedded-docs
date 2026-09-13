# Options avancées OpenAI ChatGPT

Le nœud OpenAIChatConfig définit des options avancées qui contrôlent la manière dont le nœud OpenAI Chat génère ses réponses. Il vous permet de définir la stratégie de troncature, de limiter le nombre de tokens de sortie, de fournir des instructions personnalisées et de choisir l'effort de raisonnement que le modèle doit appliquer avant de répondre.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `troncature` | La stratégie de troncature à utiliser pour la réponse du modèle. auto : si le contexte de cette réponse et des précédentes dépasse la taille de la fenêtre de contexte du modèle, le modèle tronquera la réponse pour l'adapter à la fenêtre de contexte en supprimant des éléments d'entrée au milieu de la conversation. disabled : si une réponse du modèle dépasse la taille de la fenêtre de contexte d'un modèle, la requête échouera avec une erreur 400 (par défaut : "auto") | COMBO | Oui | "auto"<br>"disabled" |
| `jetons_sortie_max` | Une limite supérieure du nombre de tokens pouvant être générés pour une réponse, y compris les tokens de sortie visibles et les tokens de raisonnement (par défaut : 4096) | INT | Non | 16 à 16384 |
| `instructions` | Instructions destinées au modèle sur la manière de générer la réponse (saisie multiligne prise en charge) | STRING | Non | - |
| `reasoning_effort` | Dans quelle mesure le modèle raisonne avant de répondre. « default » laisse le choix au modèle. Les niveaux pris en charge varient selon le modèle : GPT-6 Astra low-max, GPT-5.6 none-max (pas de minimal), GPT-5.5 none-xhigh, GPT-5.5 Pro medium-xhigh, GPT-5 minimal-high, o-series low-high ; GPT-4.1 n'a pas de raisonnement. Les niveaux non pris en charge sont rejetés avant l'envoi de la requête. (par défaut : "default") | COMBO | Non | "default"<br>"none"<br>"minimal"<br>"low"<br>"medium"<br>"high"<br>"xhigh"<br>"max" |

Remarque : bien que `top_p` et `temperature` soient listés comme propriétés dans la spécification de l'API, ils ne sont pas pris en charge par tous les modèles et ne sont donc pas exposés en tant qu'entrées.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `OPENAI_CHAT_CONFIG` | Objet de configuration contenant les paramètres avancés spécifiés, à utiliser avec les nœuds OpenAI Chat | OPENAI_CHAT_CONFIG |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/fr.md)

---
**Source fingerprint (SHA-256):** `37d18a13b9d5bb36359603e5bab5918e7fea200ac552ea8439fff1488a88263c`
