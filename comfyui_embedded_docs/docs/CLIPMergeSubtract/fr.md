# CLIPMergeSubtract

Le nœud CLIPMergeSubtract effectue la fusion de modèles en soustrayant les poids d'un modèle CLIP d'un autre. Il crée un nouveau modèle CLIP en clonant le premier modèle puis en soustrayant les patches clés du second modèle, avec un multiplicateur ajustable pour contrôler la force de la soustraction. Cela permet un mélange de modèles finement ajusté en supprimant des caractéristiques spécifiques du modèle de base.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip1` | Le modèle CLIP de base qui sera cloné et modifié | CLIP | Oui | - |
| `clip2` | Le modèle CLIP dont les patches clés seront soustraits du modèle de base | CLIP | Oui | - |
| `multiplier` | Contrôle la force de l'opération de soustraction (par défaut : 1.0) | FLOAT | Oui | -10.0 à 10.0 (pas : 0.01) |

**Remarque :** Le nœud exclut les paramètres `.position_ids` et `.logit_scale` de l'opération de soustraction, quelle que soit la valeur du multiplicateur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `clip` | Le modèle CLIP résultant après soustraction des poids du second modèle au premier | CLIP |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSubtract/fr.md)

---
**Source fingerprint (SHA-256):** `62a8cf719c34d9e2b7321f6eeb03c881f0767fd36b80e25e74feff4c0a29045e`
