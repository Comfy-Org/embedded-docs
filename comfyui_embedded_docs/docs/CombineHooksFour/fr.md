# CombineHooksFour

Le nœud **Combine Hooks [4]** fusionne jusqu'à quatre groupes de hooks distincts en un seul groupe combiné. Il accepte toute combinaison des quatre entrées de hooks disponibles et les combine à l'aide du système d'assemblage de hooks de ComfyUI. Cela permet de consolider plusieurs configurations de hooks pour un traitement rationalisé dans les workflows avancés.

## Entrées

| Paramètre | Description | Type de données | Type d'entrée | Valeur par défaut | Plage |
| --- | --- | --- | --- | --- | --- |
| `hooks_A` | Premier groupe de hooks à combiner | HOOKS | optionnelle | Aucun | - |
| `hooks_B` | Deuxième groupe de hooks à combiner | HOOKS | optionnelle | Aucun | - |
| `hooks_C` | Troisième groupe de hooks à combiner | HOOKS | optionnelle | Aucun | - |
| `hooks_D` | Quatrième groupe de hooks à combiner | HOOKS | optionnelle | Aucun | - |

**Remarque :** Les quatre entrées de hooks sont optionnelles. Le nœud ne combine que les groupes de hooks fournis et renvoie un groupe de hooks vide si aucune entrée n'est connectée.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `HOOKS` | Groupe de hooks combiné contenant toutes les configurations de hooks fournies | HOOKS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksFour/fr.md)

---
**Source fingerprint (SHA-256):** `92a8038e7b5a7491afcbd48830a1e278fe4d697321fb874821ebf7edd09d5815`
