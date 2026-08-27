# CLIPTextEncodeControlnet

Le nœud CLIPTextEncodeControlnet traite une invite de texte à l'aide d'un modèle CLIP et combine l'encodage de texte résultant avec les données de conditionnement existantes. Il ajoute les plongements dérivés du texte à chaque entrée de conditionnement comme paramètres d'attention croisée controlnet, produisant une sortie de conditionnement enrichie pour les applications controlnet.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour la tokenisation et l'encodage du texte | CLIP | Oui | - |
| `conditioning` | Données de conditionnement existantes à combiner avec l'encodage de texte CLIP | CONDITIONING | Oui | - |
| `text` | L'invite de texte à traiter par le modèle CLIP. Prend en charge le texte multiligne et les invites dynamiques | STRING | Oui | - |

**Remarque :** Les trois entrées (`clip`, `conditioning` et `text`) sont requises pour que ce nœud fonctionne. L'entrée `text` prend en charge le texte multiligne et les invites dynamiques pour un traitement flexible du texte. Ce nœud est marqué comme expérimental dans le code source.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Données de conditionnement enrichies avec les paramètres d'attention croisée controlnet ajoutés (`cross_attn_controlnet` et `pooled_output_controlnet`) dérivés de l'encodage de texte CLIP | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/fr.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
