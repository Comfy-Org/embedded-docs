> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitAudioChannels/fr.md)

Le nœud SplitAudioChannels sépare un audio stéréo en canaux gauche et droit individuels. Il prend en entrée un audio stéréo avec deux canaux et produit en sortie deux flux audio distincts, un pour le canal gauche et un pour le canal droit.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Oui | - | L'entrée audio stéréo à séparer en canaux |

**Remarque :** L'audio d'entrée doit avoir exactement deux canaux (stéréo). Le nœud générera une erreur si l'audio d'entrée n'a qu'un seul canal.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `left` | AUDIO | L'audio du canal gauche séparé |
| `right` | AUDIO | L'audio du canal droit séparé |
