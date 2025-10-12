> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/fr.md)

Ce nœud génère des réponses textuelles à partir d'un modèle OpenAI. Il vous permet d'avoir des conversations avec le modèle d'IA en envoyant des invites textuelles et en recevant des réponses générées. Le nœud prend en charge les conversations multi-tours où il peut mémoriser le contexte précédent, et il peut également traiter des images et des fichiers comme contexte supplémentaire pour le modèle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Entrées textuelles pour le modèle, utilisées pour générer une réponse (par défaut : vide) |
| `persist_context` | BOOLEAN | Oui | - | Conserver le contexte de conversation entre les appels pour une conversation multi-tours (par défaut : True) |
| `model` | COMBO | Oui | Plusieurs modèles OpenAI disponibles | Le modèle OpenAI à utiliser pour générer les réponses |
| `images` | IMAGE | Non | - | Image(s) optionnelle(s) à utiliser comme contexte pour le modèle. Pour inclure plusieurs images, vous pouvez utiliser le nœud Batch Images (par défaut : None) |
| `files` | OPENAI_INPUT_FILES | Non | - | Fichier(s) optionnel(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud OpenAI Chat Input Files (par défaut : None) |
| `advanced_options` | OPENAI_CHAT_CONFIG | Non | - | Configuration optionnelle pour le modèle. Accepte les entrées du nœud OpenAI Chat Advanced Options (par défaut : None) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output_text` | STRING | La réponse textuelle générée par le modèle OpenAI |