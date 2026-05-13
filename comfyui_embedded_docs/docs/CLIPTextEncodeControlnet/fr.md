> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/fr.md)

Ce document a été généré par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/en.md)

Le nœud CLIPTextEncodeControlnet traite une entrée textuelle à l'aide d'un modèle CLIP et la combine avec des données de conditionnement existantes pour produire un conditionnement enrichi destiné aux applications controlnet. Il tokenise le texte d'entrée, l'encode via le modèle CLIP, puis ajoute les embeddings résultants aux données de conditionnement fournies sous forme de paramètres d'attention croisée pour controlnet.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `clip` | CLIP | Oui | - | Le modèle CLIP utilisé pour la tokenisation et l'encodage du texte |
| `conditioning` | CONDITIONING | Oui | - | Données de conditionnement existantes à enrichir avec les paramètres controlnet |
| `text` | STRING | Oui | - | Texte d'entrée à traiter par le modèle CLIP. Prend en charge le texte multiligne et les invites dynamiques |

**Remarque :** Ce nœud nécessite les trois entrées (`clip`, `conditioning` et `text`) pour fonctionner correctement. L'entrée `text` prend en charge les invites dynamiques et le texte multiligne pour un traitement flexible du texte.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `CONDITIONING` | CONDITIONING | Données de conditionnement enrichies avec les paramètres d'attention croisée controlnet ajoutés (`cross_attn_controlnet` et `pooled_output_controlnet`) dérivés de l'encodage CLIP du texte |

---
**Source fingerprint (SHA-256):** `dd6f68d822cc38e27c826b634c938d62e07b075e18a0f46f80b462aecca0b70b`
