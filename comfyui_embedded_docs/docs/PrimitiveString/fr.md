> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveString/fr.md)

Le nœud String fournit un moyen simple de saisir et de transmettre des données textuelles dans votre flux de travail. Il prend une chaîne de texte en entrée et renvoie la même chaîne inchangée, ce qui le rend utile pour fournir des entrées textuelles à d'autres nœuds qui nécessitent des paramètres de type chaîne.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `value` | STRING | Oui | Tout texte | La chaîne de texte à transmettre à travers le nœud |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | STRING | La même chaîne de texte qui a été fournie en entrée |