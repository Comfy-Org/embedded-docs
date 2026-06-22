# CLIPMergeSubtract

Voici la traduction en français de la documentation du nœud CLIPMergeSubtract :

Le nœud CLIPMergeSubtract effectue une fusion de modèles en soustrayant les poids d'un modèle CLIP d'un autre. Il crée un nouveau modèle CLIP en clonant le premier modèle, puis en soustrayant les correctifs de clés du second modèle, avec un multiplicateur ajustable pour contrôler l'intensité de la soustraction. Cela permet un mélange fin des modèles en supprimant des caractéristiques spécifiques du modèle de base.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip1` | Le modèle CLIP de base qui sera cloné et modifié | CLIP | Oui | - |
| `clip2` | Le modèle CLIP dont les correctifs de clés seront soustraits du modèle de base | CLIP | Oui | - |
| `multiplier` | Contrôle l'intensité de l'opération de soustraction (par défaut : 1.0) | FLOAT | Oui | -10.0 à 10.0 |

**Remarque :** Le nœud exclut les paramètres `.position_ids` et `.logit_scale` de l'opération de soustraction, quelle que soit la valeur du multiplicateur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `clip` | Le modèle CLIP résultant après soustraction des poids du second modèle du premier | CLIP |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSubtract/fr.md)

---
**Source fingerprint (SHA-256):** `3136cf509fcbfa291af8f820928a6cc14de7a586f953af0ada9bea949b437d86`
