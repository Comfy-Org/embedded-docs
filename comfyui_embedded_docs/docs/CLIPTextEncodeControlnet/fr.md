# CLIPTextEncodeControlnet

Le nœud CLIP Text Encode (Controlnet) encode une invite textuelle avec un modèle CLIP et ajoute l'encodage textuel résultant aux données de conditionnement existantes. Il stocke les plongements de texte en tant que paramètres d'attention croisée controlnet à l'intérieur de chaque entrée de conditionnement, de sorte que le conditionnement renvoyé transporte ces informations controlnet supplémentaires.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour la tokenisation et l'encodage du texte | CLIP | Oui | - |
| `conditioning` | Données de conditionnement existantes à combiner avec l'encodage textuel CLIP | CONDITIONING | Oui | - |
| `text` | L'invite textuelle à traiter par le modèle CLIP. Prend en charge le texte multiligne et les invites dynamiques | STRING | Oui | - |

**Remarque :** Les trois entrées (`clip`, `conditioning` et `text`) sont requises pour que ce nœud fonctionne. L'entrée `text` prend en charge le texte multiligne et les invites dynamiques pour un traitement de texte flexible. Ce nœud est marqué comme expérimental dans le code source.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Données de conditionnement améliorées avec les paramètres d'attention croisée controlnet ajoutés (`cross_attn_controlnet` et `pooled_output_controlnet`) issus de l'encodage textuel CLIP | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/fr.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
