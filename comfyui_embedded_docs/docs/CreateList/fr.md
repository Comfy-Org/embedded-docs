> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/fr.md)

Le nœud Créer une Liste combine plusieurs entrées en une seule liste séquentielle. Il accepte un nombre quelconque d'entrées du même type de données et les concatène dans l'ordre de connexion. Ce nœud est utile pour préparer des lots de données, comme des images ou du texte, à traiter par d'autres nœuds dans un workflow.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `input_*` | Variable | Oui | Toute | Un nombre variable d'emplacements d'entrée. Vous pouvez ajouter d'autres entrées en cliquant sur l'icône plus (+). Toutes les entrées doivent être du même type de données (par exemple, toutes IMAGE ou toutes STRING). |

**Remarque :** Le nœud créera automatiquement de nouveaux emplacements d'entrée à mesure que vous connectez des éléments. Toutes les entrées connectées doivent partager le même type de données pour que le nœud fonctionne correctement.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `list` | Variable | Une liste unique contenant tous les éléments des entrées connectées, concaténés dans l'ordre de leur fourniture. Le type de données de sortie correspond au type de données d'entrée. |

---
**Source fingerprint (SHA-256):** `d0e10c4d1186e694a72b18407c34cc1df74f77d02c989b507af75594c1a0794e`
