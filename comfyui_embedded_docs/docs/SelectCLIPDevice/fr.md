Voici la traduction en français de la documentation du nœud SelectCLIPDevice :

## Aperçu

Le nœud Select CLIP Device vous permet de choisir sur quel périphérique (CPU ou GPU spécifique) l'encodeur de texte CLIP s'exécute. Par défaut, le périphérique est attribué par le chargeur de modèle, mais vous pouvez le remplacer pour utiliser le CPU ou un GPU particulier. Si le périphérique demandé n'existe pas sur votre machine, le nœud transmet simplement le CLIP sans modification et enregistre un message au lieu de générer une erreur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | L'encodeur de texte CLIP à attribuer à un périphérique spécifique. | CLIP | Oui |  |
| `device` | Le périphérique sur lequel placer l'encodeur de texte CLIP. `"default"` restaure le périphérique attribué par le chargeur. `"cpu"` verrouille à la fois le périphérique de chargement et de déchargement sur le CPU. `"gpu:N"` verrouille le périphérique de chargement sur le Nième GPU disponible (par défaut : `"default"`). | COMBO | Oui | `"default"`<br>`"cpu"`<br>`"gpu:0"`<br>`"gpu:1"`<br>`"gpu:2"`<br>`"gpu:3"`<br>`"gpu:4"`<br>`"gpu:5"`<br>`"gpu:6"`<br>`"gpu:7"` |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `clip` | L'encodeur de texte CLIP attribué au périphérique sélectionné, ou le CLIP original transmis sans modification si le périphérique demandé n'est pas disponible. | CLIP |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectCLIPDevice/fr.md)

---
**Source fingerprint (SHA-256):** `92af94d9f5eea27095cc008debdf7339d26888a0e2cc8bd71ae9c9ba8718eb01`
