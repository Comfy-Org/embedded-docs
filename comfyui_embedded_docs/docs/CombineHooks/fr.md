> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooks/fr.md)

Le nœud Combine Hooks [2] fusionne deux groupes de hooks en un seul groupe combiné. Il prend deux entrées de hooks optionnelles et les combine à l'aide de la fonctionnalité de combinaison de hooks de ComfyUI. Cela permet de consolider plusieurs configurations de hooks pour un traitement simplifié.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `hooks_A` | HOOKS | Non | - | Premier groupe de hooks à combiner |
| `hooks_B` | HOOKS | Non | - | Second groupe de hooks à combiner |

**Remarque :** Les deux entrées sont optionnelles, mais au moins un groupe de hooks doit être fourni pour que le nœud fonctionne. Si un seul groupe de hooks est fourni, il sera retourné inchangé.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `hooks` | HOOKS | Groupe de hooks combiné contenant tous les hooks des deux groupes d'entrée |

---
**Source fingerprint (SHA-256):** `558ceef1cebedd0b7e045b7d1eb1afa4316ea6a3c35f982968af132dca164126`
