> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/fr.md)

Le nœud LotusConditioning fournit des embeddings de conditionnement pré-calculés pour le modèle Lotus. Il utilise un encodeur figé avec un conditionnement nul et retourne des embeddings d'invite codés en dur pour obtenir une parité avec l'implémentation de référence sans nécessiter d'inférence ou le chargement de fichiers tensoriels volumineux. Ce nœud produit un tenseur de conditionnement fixe qui peut être utilisé directement dans le pipeline de génération.

## Entrées

| Paramètre | Type de données | Obligatoire | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| *Aucune entrée* | - | - | - | Ce nœud n'accepte aucun paramètre d'entrée. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Les embeddings de conditionnement pré-calculés pour le modèle Lotus, contenant des embeddings d'invite fixes et un dictionnaire vide. |