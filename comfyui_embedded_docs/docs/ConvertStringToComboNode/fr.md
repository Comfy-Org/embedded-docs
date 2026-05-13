> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConvertStringToComboNode/fr.md)

Le nœud Convert String to Combo prend une chaîne de texte en entrée et la convertit en type de données Combo. Cela vous permet d'utiliser une valeur textuelle comme sélection pour d'autres nœuds nécessitant une entrée de type Combo. Il transmet simplement la chaîne de caractères inchangée, mais en modifie le type de données.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `string` | STRING | Oui | N/A | La chaîne de texte à convertir en type Combo. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | COMBO | La chaîne d'entrée, désormais formatée en tant que type de données Combo. |

---
**Source fingerprint (SHA-256):** `37bd7db5a5ce2657db30a3a24da90c1c1e5c4a3f7089b4d03a0528b7770e9fe1`
