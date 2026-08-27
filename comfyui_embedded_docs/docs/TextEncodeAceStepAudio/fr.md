# TextEncodeAceStepAudio

Le nœud TextEncodeAceStepAudio traite les entrées de texte pour le conditionnement audio en combinant les tags et les paroles en tokens, puis en les encodant avec une force de paroles ajustable. Il prend un modèle CLIP ainsi que des descriptions textuelles et des paroles, les tokenise ensemble et génère des données de conditionnement adaptées aux tâches de génération audio. Le nœud permet d'ajuster finement l'influence des paroles via un paramètre de force qui contrôle leur impact sur la sortie finale.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour la tokenisation et l'encodage | CLIP | Oui | - |
| `balises` | Tags ou descriptions textuels pour le conditionnement audio (prend en charge les entrées multilignes et les invites dynamiques) | STRING | Oui | - |
| `paroles` | Texte des paroles pour le conditionnement audio (prend en charge les entrées multilignes et les invites dynamiques) | STRING | Oui | - |
| `force_des_paroles` | Contrôle la force de l'influence des paroles sur la sortie de conditionnement (par défaut : 1.0, pas : 0.01) | FLOAT | Oui | 0.0 - 10.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `conditioning` | Les données de conditionnement encodées contenant les tokens de texte traités avec la force de paroles appliquée | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/fr.md)

---
**Source fingerprint (SHA-256):** `2226c9f25dd26bf454bcce2e298d6d261dace5a9bbed164a2fcf0e1204d7c3f4`
