> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3InfiniteStyleLibrary/fr.md)

Ce nœud vous permet de sélectionner un style depuis la bibliothèque de styles infinie de Recraft en utilisant un UUID préexistant. Il récupère les informations du style en fonction de l'identifiant fourni et le retourne pour une utilisation dans d'autres nœuds Recraft.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `style_id` | STRING | Oui | Tout UUID valide | UUID du style provenant de la bibliothèque de styles infinie. |

**Remarque :** L'entrée `style_id` ne peut pas être vide. Si une chaîne vide est fournie, le nœud lèvera une exception.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `recraft_style` | STYLEV3 | L'objet de style sélectionné depuis la bibliothèque de styles infinie de Recraft |

---
**Source fingerprint (SHA-256):** `37d7d9eff1232cc17912c6fca908dc5b8c404c0b6cf0a36e8fecc837ff2a1eea`
