# CLIPTextEncodeControlnet

Le nœud `CLIPTextEncodeControlnet` traite une entrée de texte à l'aide d'un modèle CLIP et la combine avec des données de conditionnement existantes pour produire un conditionnement enrichi destiné aux applications controlnet. Il tokenise le texte d'entrée, l'encode via le modèle CLIP, puis ajoute les embeddings obtenus aux données de conditionnement fournies, en tant que paramètres controlnet d'attention croisée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour la tokenisation et l'encodage du texte | CLIP | Oui | - |
| `conditioning` | Données de conditionnement existantes à enrichir avec les paramètres controlnet | CONDITIONING | Oui | - |
| `text` | Texte d'entrée à traiter par le modèle CLIP. Prend en charge le texte multiligne et les invites dynamiques | STRING | Oui | - |

**Remarque :** Ce nœud nécessite les trois entrées (`clip`, `conditioning` et `text`) pour fonctionner correctement. L'entrée `text` prend en charge les invites dynamiques et le texte multiligne pour un traitement flexible du texte. Ce nœud est marqué comme expérimental.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Données de conditionnement enrichies, avec les paramètres controlnet d'attention croisée (`cross_attn_controlnet` et `pooled_output_controlnet`) dérivés de l'encodage du texte par CLIP | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/fr.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
