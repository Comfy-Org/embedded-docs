> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/fr.md)

Le nœud TextGenerateLTX2Prompt est une version spécialisée d'un nœud de génération de texte. Il prend un prompt texte de l'utilisateur et le formate automatiquement avec des instructions système spécifiques avant de l'envoyer à un modèle de langage pour amélioration ou complétion. Le nœud peut fonctionner dans deux modes : texte uniquement ou avec une référence d'image, en utilisant des prompts système différents pour chaque cas.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Oui | | Le modèle CLIP utilisé pour l'encodage du texte. |
| `prompt` | STRING | Oui | | Le texte brut fourni par l'utilisateur qui sera amélioré ou complété. |
| `max_length` | INT | Oui | | Le nombre maximum de jetons que le modèle de langage est autorisé à générer. |
| `sampling_mode` | COMBO | Oui | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` | La stratégie d'échantillonnage utilisée pour sélectionner le jeton suivant lors de la génération de texte. |
| `image` | IMAGE | Non | | Une image d'entrée optionnelle. Lorsqu'elle est fournie, le nœud utilise un prompt système différent qui inclut un espace réservé pour le contexte de l'image. |

**Note :** Le comportement du nœud change en fonction de la présence de l'entrée `image`. Si une image est fournie, le prompt généré sera formaté pour une tâche image-à-vidéo. Si aucune image n'est fournie, le formatage sera pour une tâche texte-à-vidéo.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | STRING | La chaîne de texte améliorée ou complétée générée par le modèle de langage. |