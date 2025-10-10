> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaReferenceNode/fr.md)

Ce nœud contient une image et une valeur de poids pour utilisation avec le nœud Luma Generate Image. Il crée une chaîne de référence qui peut être transmise à d'autres nœuds Luma pour influencer la génération d'image. Le nœud peut soit démarrer une nouvelle chaîne de référence, soit s'ajouter à une chaîne existante.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | Image à utiliser comme référence. |
| `weight` | FLOAT | Oui | 0.0 - 1.0 | Poids de la référence d'image (par défaut : 1.0). |
| `luma_ref` | LUMA_REF | Non | - | Chaîne de référence Luma existante optionnelle à laquelle s'ajouter. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `luma_ref` | LUMA_REF | La chaîne de référence Luma contenant l'image et le poids. |