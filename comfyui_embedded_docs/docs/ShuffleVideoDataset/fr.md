# Mélanger la liste de vidéos

Ce nœud prend une liste de vidéos et les réorganise aléatoirement. Il utilise une graine aléatoire pour garantir un mélange reproductible, de sorte que la même graine produise toujours le même ordre de sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `vidéos` | Liste des vidéos à mélanger. | VIDEO | Oui | List of video inputs |
| `graine` | Graine aléatoire pour le mélange (par défaut : 0). | INT | Non | 0 to 18446744073709551615 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `vidéos` | Liste mélangée de vidéos dans un ordre aléatoire. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoDataset/fr.md)

---
**Source fingerprint (SHA-256):** `0bd32b664197d3bbd4c53f65e29ef38fba836579f07f05cb7fb85f3b8a1024ac`
