Ce nœud génère des réponses textuelles à partir d’un modèle OpenAI. Il envoie votre invite textuelle (et éventuellement des images ou fichiers) à un modèle OpenAI et renvoie la réponse textuelle générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `invite` | Saisies textuelles du modèle, utilisées pour générer une réponse (par défaut : vide) | STRING | Oui | - |
| `conserver_contexte` | Ce paramètre est obsolète et n’a aucun effet (par défaut : False) | BOOLEAN | Oui | - |
| `modèle` | Le modèle utilisé pour générer la réponse | COMBO | Oui | Plusieurs modèles OpenAI disponibles |
| `images` | Image(s) facultative(s) à utiliser comme contexte pour le modèle. Pour inclure plusieurs images, vous pouvez utiliser le nœud Batch Images | IMAGE | Non | - |
| `fichiers` | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud OpenAI Chat Input Files | OPENAI_INPUT_FILES | Non | - |
| `options_avancées` | Configuration facultative pour le modèle. Accepte les entrées du nœud OpenAI Chat Advanced Options | OPENAI_CHAT_CONFIG | Non | - |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output_text` | La réponse textuelle générée par le modèle OpenAI | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/fr.md)

---
**Source fingerprint (SHA-256):** `ea66b58b23305b0d97bfc76cc39cfdfe8e01b70edcbfd60c2c640a07ad507ee6`
