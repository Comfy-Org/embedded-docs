> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooks/fr.md)

Le nœud Combine Hooks [2] fusionne deux groupes de hooks en un seul groupe combiné. Il prend deux entrées de hooks optionnelles et les combine en utilisant la fonctionnalité de combinaison de hooks de ComfyUI. Cela vous permet de consolider plusieurs configurations de hooks pour un traitement rationalisé.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `hooks_A` | HOOKS | Optionnel | Aucun | - | Premier groupe de hooks à combiner |
| `hooks_B` | HOOKS | Optionnel | Aucun | - | Deuxième groupe de hooks à combiner |

**Remarque :** Les deux entrées sont optionnelles, mais au moins un groupe de hooks doit être fourni pour que le nœud fonctionne. Si un seul groupe de hooks est fourni, il sera retourné inchangé.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `hooks` | HOOKS | Groupe de hooks combiné contenant tous les hooks des deux groupes d'entrée |