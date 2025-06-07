Ce nœud se spécialise dans la fusion de deux modèles CLIP selon un ratio spécifié, mélangeant efficacement leurs caractéristiques. Il applique sélectivement des patches d'un modèle à un autre, en excluant des composants spécifiques comme les IDs de position et l'échelle des logits, pour créer un modèle hybride qui combine les caractéristiques des deux modèles sources.

## Entrées

| Paramètre | Comfy dtype | Description |
|-----------|-------------|-------------|
| `clip1`   | `CLIP`      | Le premier modèle CLIP à fusionner. Il sert de modèle de base pour le processus de fusion. |
| `clip2`   | `CLIP`      | Le second modèle CLIP à fusionner. Ses patches clés, à l'exception des IDs de position et de l'échelle des logits, sont appliqués au premier modèle selon le ratio spécifié. |
| `ratio`   | `FLOAT`     | Détermine la proportion de caractéristiques du second modèle à intégrer dans le premier modèle. Un ratio de 1.0 signifie adopter entièrement les caractéristiques du second modèle, tandis que 0.0 conserve uniquement les caractéristiques du premier modèle. |

## Sorties

| Paramètre | Comfy dtype | Description |
|-----------|-------------|-------------|
| `clip`    | `CLIP`      | Le modèle CLIP fusionné résultant, incorporant des caractéristiques des deux modèles d'entrée selon le ratio spécifié. |
