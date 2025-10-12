> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksEight/fr.md)

Le nœud Combine Hooks [8] fusionne jusqu'à huit groupes de hooks différents en un seul groupe de hooks combiné. Il prend plusieurs entrées de hooks et les combine en utilisant la fonctionnalité de combinaison de hooks de ComfyUI. Cela vous permet de consolider plusieurs configurations de hooks pour un traitement rationalisé dans les workflows avancés.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `hooks_A` | HOOKS | optionnel | Aucun | - | Premier groupe de hooks à combiner |
| `hooks_B` | HOOKS | optionnel | Aucun | - | Deuxième groupe de hooks à combiner |
| `hooks_C` | HOOKS | optionnel | Aucun | - | Troisième groupe de hooks à combiner |
| `hooks_D` | HOOKS | optionnel | Aucun | - | Quatrième groupe de hooks à combiner |
| `hooks_E` | HOOKS | optionnel | Aucun | - | Cinquième groupe de hooks à combiner |
| `hooks_F` | HOOKS | optionnel | Aucun | - | Sixième groupe de hooks à combiner |
| `hooks_G` | HOOKS | optionnel | Aucun | - | Septième groupe de hooks à combiner |
| `hooks_H` | HOOKS | optionnel | Aucun | - | Huitième groupe de hooks à combiner |

**Remarque :** Tous les paramètres d'entrée sont optionnels. Le nœud combinera uniquement les groupes de hooks qui sont fournis, en ignorant ceux qui sont laissés vides. Vous pouvez fournir entre un et huit groupes de hooks pour la combinaison.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `HOOKS` | HOOKS | Un seul groupe de hooks combiné contenant toutes les configurations de hooks fournies |
