> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksFour/fr.md)

Le nœud **Combine Hooks [4]** fusionne jusqu'à quatre groupes de hooks distincts en un seul groupe combiné. Il accepte toute combinaison des quatre entrées de hooks disponibles et les combine à l'aide du système d'assemblage de hooks de ComfyUI. Cela permet de consolider plusieurs configurations de hooks pour un traitement rationalisé dans les workflows avancés.

## Entrées

| Paramètre | Type de données | Type d'entrée | Valeur par défaut | Plage | Description |
|-----------|-----------------|---------------|-------------------|-------|-------------|
| `hooks_A` | HOOKS | optionnelle | Aucun | - | Premier groupe de hooks à combiner |
| `hooks_B` | HOOKS | optionnelle | Aucun | - | Deuxième groupe de hooks à combiner |
| `hooks_C` | HOOKS | optionnelle | Aucun | - | Troisième groupe de hooks à combiner |
| `hooks_D` | HOOKS | optionnelle | Aucun | - | Quatrième groupe de hooks à combiner |

**Remarque :** Les quatre entrées de hooks sont optionnelles. Le nœud ne combine que les groupes de hooks fournis et renvoie un groupe de hooks vide si aucune entrée n'est connectée.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `HOOKS` | HOOKS | Groupe de hooks combiné contenant toutes les configurations de hooks fournies |

---
**Source fingerprint (SHA-256):** `92a8038e7b5a7491afcbd48830a1e278fe4d697321fb874821ebf7edd09d5815`
