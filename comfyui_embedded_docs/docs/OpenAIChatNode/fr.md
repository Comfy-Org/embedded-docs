# OpenAI ChatGPT

Ce nœud génère des réponses textuelles à partir d'un modèle OpenAI. Il envoie votre invite textuelle, et éventuellement des images ou des fichiers, à un modèle OpenAI et renvoie la réponse textuelle générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `invite` | Entrées de texte envoyées au modèle, utilisées pour générer une réponse (défaut : vide) | STRING | Oui | - |
| `conserver_contexte` | Ce paramètre est obsolète et n'a aucun effet (défaut : False) | BOOLEAN | Oui | - |
| `modèle` | Modèle utilisé pour générer la réponse (défaut : `gpt-5`) | COMBO | Oui | `gpt-5.6-sol`<br>`gpt-5.6-terra`<br>`gpt-5.6-luna`<br>`gpt-5.5-pro`<br>`gpt-5.5`<br>`gpt-5`<br>`gpt-5-mini`<br>`gpt-5-nano`<br>`gpt-4.1`<br>`gpt-4.1-mini`<br>`gpt-4.1-nano`<br>`o4-mini`<br>`o3`<br>`o1-pro`<br>`o1` |
| `images` | Image(s) facultative(s) à utiliser comme contexte pour le modèle. Pour inclure plusieurs images, vous pouvez utiliser le nœud Batch Images | IMAGE | Non | - |
| `fichiers` | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud OpenAI Chat Input Files | OPENAI_INPUT_FILES | Non | - |
| `options_avancées` | Configuration facultative pour le modèle. Accepte les entrées du nœud OpenAI Chat Advanced Options | OPENAI_CHAT_CONFIG | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------------|
| `output_text` | La réponse textuelle générée par le modèle OpenAI | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/fr.md)

---
**Source fingerprint (SHA-256):** `25bb3648a4e1ea5668486375153ac4c96b542082c88958d4f62b93adf1db5b2a`
