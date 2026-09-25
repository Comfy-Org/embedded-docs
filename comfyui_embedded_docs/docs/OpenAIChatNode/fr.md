# OpenAI ChatGPT

Ce nœud génère des réponses textuelles à partir d’un modèle OpenAI. Il envoie votre prompt textuel, et éventuellement des images ou des fichiers, à un modèle OpenAI, puis renvoie la réponse textuelle générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `invite` | Entrées textuelles pour le modèle, utilisées pour générer une réponse (par défaut : chaîne vide). | STRING | Oui | - |
| `conserver_contexte` | Ce paramètre est obsolète et n’a aucun effet (par défaut : False). | BOOLEAN | Oui | - |
| `modèle` | Le modèle utilisé pour générer la réponse (par défaut : `gpt-5`) | COMBO | Oui | `gpt-6-astra`<br>`gpt-6-sol`<br>`gpt-6-luna`<br>`gpt-5.6-sol`<br>`gpt-5.6-terra`<br>`gpt-5.6-luna`<br>`gpt-5.5-pro`<br>`gpt-5.5`<br>`gpt-5`<br>`gpt-5-mini`<br>`gpt-5-nano`<br>`gpt-4.1`<br>`gpt-4.1-mini`<br>`gpt-4.1-nano`<br>`o4-mini`<br>`o3`<br>`o1-pro`<br>`o1` |
| `images` | Image(s) facultative(s) à utiliser comme contexte pour le modèle. Pour inclure plusieurs images, vous pouvez utiliser le nœud Batch Images. | IMAGE | Non | - |
| `fichiers` | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud OpenAI Chat Input Files. | OPENAI_INPUT_FILES | Non | - |
| `options_avancées` | Configuration facultative pour le modèle. Accepte les entrées du nœud OpenAI Chat Advanced Options. | OPENAI_CHAT_CONFIG | Non | - |

Remarque : lorsqu’une configuration `advanced_options` qui définit un effort de raisonnement est connectée, le `model` sélectionné doit prendre en charge cette valeur d’effort. Par exemple, la famille de modèles gpt-4.1 ne prend en charge aucun effort de raisonnement, `gpt-6-sol` et `gpt-6-luna` prennent en charge none, low, medium, high, xhigh et max, `gpt-5.5` prend en charge none, low, medium, high et xhigh, et `gpt-5.5-pro` prend en charge medium, high et xhigh. Si l’effort de raisonnement n’est pas pris en charge par le modèle sélectionné, le nœud lève une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output_text` | La réponse textuelle générée par le modèle OpenAI. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/fr.md)

---
**Source fingerprint (SHA-256):** `46b4558f1368191e2b4eb68f79e098f289c9eb80e1e05f7a516123c098295f2b`
