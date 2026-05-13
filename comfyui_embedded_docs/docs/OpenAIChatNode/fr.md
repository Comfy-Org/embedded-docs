> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/fr.md)

Ce nœud génère des réponses textuelles à partir d’un modèle OpenAI. Il envoie votre invite textuelle (et éventuellement des images ou fichiers) à un modèle OpenAI et renvoie la réponse textuelle générée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `invite` | STRING | Oui | - | Saisies textuelles du modèle, utilisées pour générer une réponse (par défaut : vide) |
| `conserver_contexte` | BOOLEAN | Oui | - | Ce paramètre est obsolète et n’a aucun effet (par défaut : False) |
| `modèle` | COMBO | Oui | Plusieurs modèles OpenAI disponibles | Le modèle utilisé pour générer la réponse |
| `images` | IMAGE | Non | - | Image(s) facultative(s) à utiliser comme contexte pour le modèle. Pour inclure plusieurs images, vous pouvez utiliser le nœud Batch Images |
| `fichiers` | OPENAI_INPUT_FILES | Non | - | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud OpenAI Chat Input Files |
| `options_avancées` | OPENAI_CHAT_CONFIG | Non | - | Configuration facultative pour le modèle. Accepte les entrées du nœud OpenAI Chat Advanced Options |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `output_text` | STRING | La réponse textuelle générée par le modèle OpenAI |

---
**Source fingerprint (SHA-256):** `ea66b58b23305b0d97bfc76cc39cfdfe8e01b70edcbfd60c2c640a07ad507ee6`
