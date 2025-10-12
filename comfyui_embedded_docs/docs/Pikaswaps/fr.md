> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaswaps/fr.md)

Le nœud Pika Swaps vous permet de remplacer des objets ou des régions dans votre vidéo par de nouvelles images. Vous pouvez définir les zones à remplacer en utilisant soit un masque, soit des coordonnées, et le nœud remplacera de manière transparente le contenu spécifié tout au long de la séquence vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Oui | - | La vidéo dans laquelle remplacer un objet. |
| `image` | IMAGE | Oui | - | L'image utilisée pour remplacer l'objet masqué dans la vidéo. |
| `mask` | MASK | Oui | - | Utilisez le masque pour définir les zones de la vidéo à remplacer. |
| `prompt_text` | STRING | Oui | - | Prompt textuel décrivant le remplacement souhaité. |
| `negative_prompt` | STRING | Oui | - | Prompt textuel décrivant ce qu'il faut éviter dans le remplacement. |
| `seed` | INT | Oui | 0 à 4294967295 | Valeur de seed aléatoire pour des résultats cohérents. |

**Note :** Ce nœud nécessite que tous les paramètres d'entrée soient fournis. La `video`, l'`image` et le `mask` fonctionnent ensemble pour définir l'opération de remplacement, où le masque spécifie les zones de la vidéo qui seront remplacées par l'image fournie.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo traitée avec l'objet ou la région spécifiée remplacé(e). |