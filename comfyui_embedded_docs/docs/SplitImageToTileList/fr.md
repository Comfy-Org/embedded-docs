> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageToTileList/fr.md)

Le nœud **Diviser l'image en liste de tuiles** divise une seule image d'entrée en une série de sections rectangulaires plus petites et se chevauchant, appelées tuiles. Il crée une liste groupée de ces tuiles, qui peuvent être traitées individuellement par d'autres nœuds. La taille de chaque tuile et le degré de chevauchement entre elles peuvent être spécifiés.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à diviser en tuiles. |
| `largeur_tuile` | INT | Oui | 64 à 1048576 | La largeur de chaque tuile de sortie en pixels (par défaut : 1024). |
| `hauteur_tuile` | INT | Oui | 64 à 1048576 | La hauteur de chaque tuile de sortie en pixels (par défaut : 1024). |
| `chevauchement` | INT | Oui | 0 à 4096 | Le nombre de pixels de chevauchement entre les tuiles adjacentes (par défaut : 128). |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `image` | IMAGE | Une liste groupée contenant toutes les tuiles d'image individuelles. |

---
**Source fingerprint (SHA-256):** `26991a325b7b9358cd7338348e93c57695b1ed1aa1983962794f889c94c34547`
