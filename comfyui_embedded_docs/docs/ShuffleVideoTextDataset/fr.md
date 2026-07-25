# Mélanger les paires Vidéo-Texte

Ce nœud mélange aléatoirement l'ordre des paires vidéo-texte, en conservant chaque vidéo appariée avec son texte correspondant. Il prend deux listes de même longueur et applique la même permutation aléatoire aux deux, garantissant que les appariements d'origine sont préservés après le mélange.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `vidéos` | Liste des vidéos à mélanger. | VIDEO | Oui | Liste d'éléments vidéo |
| `textes` | Liste des textes à mélanger. | STRING | Oui | Liste de chaînes de texte |
| `graine` | Graine aléatoire pour contrôler l'ordre de mélange (par défaut : 0). | INT | Oui | 0 à 18446744073709551615 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `vidéos` | Vidéos mélangées dans le nouvel ordre aléatoire. | VIDEO |
| `textes` | Textes mélangés dans le même nouvel ordre que les vidéos. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoTextDataset/fr.md)

---
**Source fingerprint (SHA-256):** `33b763a6d48ca1036d5267139f90eadb3b2080a02fa57ce5bcae6087a077efa1`
