> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSubtract/fr.md)

Le nœud CLIPSubtract effectue une opération de soustraction entre deux modèles CLIP. Il prend le premier modèle CLIP comme base et soustrait les patches clés du second modèle CLIP, avec un multiplicateur optionnel pour contrôler l'intensité de la soustraction. Cela permet un mélange de modèles finement ajusté en supprimant des caractéristiques spécifiques d'un modèle à l'aide d'un autre.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `clip1` | CLIP | Requis | - | - | Le modèle CLIP de base qui sera modifié |
| `clip2` | CLIP | Requis | - | - | Le modèle CLIP dont les patches clés seront soustraits du modèle de base |
| `multiplier` | FLOAT | Requis | 1.0 | -10.0 à 10.0, pas 0.01 | Contrôle l'intensité de l'opération de soustraction |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Le modèle CLIP résultant après l'opération de soustraction |