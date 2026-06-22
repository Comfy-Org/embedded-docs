# Recraft Style - Infinite Style Library

Ce nœud vous permet de sélectionner un style depuis la bibliothèque de styles infinie de Recraft en utilisant un UUID préexistant. Il récupère les informations du style en fonction de l'identifiant fourni et le retourne pour une utilisation dans d'autres nœuds Recraft.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `style_id` | UUID du style provenant de la bibliothèque de styles infinie. | STRING | Oui | Tout UUID valide |

**Remarque :** L'entrée `style_id` ne peut pas être vide. Si une chaîne vide est fournie, le nœud lèvera une exception.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `recraft_style` | L'objet de style sélectionné depuis la bibliothèque de styles infinie de Recraft | STYLEV3 |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3InfiniteStyleLibrary/fr.md)

---
**Source fingerprint (SHA-256):** `37d7d9eff1232cc17912c6fca908dc5b8c404c0b6cf0a36e8fecc837ff2a1eea`
