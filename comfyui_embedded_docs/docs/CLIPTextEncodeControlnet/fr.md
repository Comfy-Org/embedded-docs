> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/fr.md)

Le nœud CLIPTextEncodeControlnet traite le texte d'entrée à l'aide d'un modèle CLIP et le combine avec des données de conditionnement existantes pour créer une sortie de conditionnement améliorée destinée aux applications controlnet. Il tokenise le texte d'entrée, l'encode via le modèle CLIP et ajoute les embeddings résultants aux données de conditionnement fournies en tant que paramètres controlnet d'attention croisée.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | Requis | - | - | Le modèle CLIP utilisé pour la tokenisation et l'encodage du texte |
| `conditioning` | CONDITIONING | Requis | - | - | Données de conditionnement existantes à enrichir avec les paramètres controlnet |
| `text` | STRING | Multiligne, Prompts Dynamiques | - | - | Texte d'entrée à traiter par le modèle CLIP |

**Remarque :** Ce nœud nécessite à la fois les entrées `clip` et `conditioning` pour fonctionner correctement. L'entrée `text` prend en charge les prompts dynamiques et le texte multiligne pour un traitement flexible du texte.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Données de conditionnement améliorées avec des paramètres d'attention croisée controlnet ajoutés |