> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksFour/fr.md)

Le nœud Combine Hooks [4] fusionne jusqu'à quatre groupes de hooks distincts en un seul groupe de hooks combiné. Il prend n'importe quelle combinaison des quatre entrées de hooks disponibles et les combine en utilisant le système de combinaison de hooks de ComfyUI. Cela vous permet de consolider plusieurs configurations de hooks pour un traitement rationalisé dans les workflows avancés.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `hooks_A` | HOOKS | optionnel | Aucun | - | Premier groupe de hooks à combiner |
| `hooks_B` | HOOKS | optionnel | Aucun | - | Deuxième groupe de hooks à combiner |
| `hooks_C` | HOOKS | optionnel | Aucun | - | Troisième groupe de hooks à combiner |
| `hooks_D` | HOOKS | optionnel | Aucun | - | Quatrième groupe de hooks à combiner |

**Remarque :** Les quatre entrées de hooks sont optionnelles. Le nœud combinera uniquement les groupes de hooks qui sont fournis et retournera un groupe de hooks vide si aucune entrée n'est connectée.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `HOOKS` | HOOKS | Groupe de hooks combiné contenant toutes les configurations de hooks fournies |
