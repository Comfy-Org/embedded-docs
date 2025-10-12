> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/fr.md)

Le nœud TextEncodeAceStepAudio traite les entrées textuelles pour le conditionnement audio en combinant les tags et paroles en tokens, puis les encode avec une force de paroles ajustable. Il prend un modèle CLIP ainsi que des descriptions textuelles et des paroles, les tokenise ensemble et génère des données de conditionnement adaptées aux tâches de génération audio. Le nœud permet d'ajuster finement l'influence des paroles via un paramètre de force qui contrôle leur impact sur le résultat final.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Oui | - | Le modèle CLIP utilisé pour la tokenisation et l'encodage |
| `tags` | STRING | Oui | - | Tags textuels ou descriptions pour le conditionnement audio (prend en charge l'entrée multiligne et les invites dynamiques) |
| `lyrics` | STRING | Oui | - | Texte des paroles pour le conditionnement audio (prend en charge l'entrée multiligne et les invites dynamiques) |
| `lyrics_strength` | FLOAT | Non | 0.0 - 10.0 | Contrôle la force de l'influence des paroles sur la sortie de conditionnement (par défaut : 1.0, pas : 0.01) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Les données de conditionnement encodées contenant les tokens textuels traités avec la force des paroles appliquée |