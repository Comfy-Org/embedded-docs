> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSubtract/fr.md)

Le nœud CLIPMergeSubtract effectue une fusion de modèles en soustrayant les poids d'un modèle CLIP d'un autre. Il crée un nouveau modèle CLIP en clonant le premier modèle puis en soustrayant les patches clés du second modèle, avec un multiplicateur ajustable pour contrôler l'intensité de la soustraction. Cela permet un mélange de modèles finement ajusté en supprimant des caractéristiques spécifiques du modèle de base.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `clip1` | CLIP | Oui | - | Le modèle CLIP de base qui sera cloné et modifié |
| `clip2` | CLIP | Oui | - | Le modèle CLIP dont les patches clés seront soustraits du modèle de base |
| `multiplier` | FLOAT | Oui | -10.0 à 10.0 | Contrôle l'intensité de l'opération de soustraction (par défaut : 1.0) |

**Note :** Le nœud exclut les paramètres `.position_ids` et `.logit_scale` de l'opération de soustraction, quelle que soit la valeur du multiplicateur.

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `clip` | CLIP | Le modèle CLIP résultant après soustraction des poids du second modèle du premier |
