> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/fr.md)

Le nœud PrimitiveBoundingBox crée une zone rectangulaire simple définie par sa position et sa taille. Il prend les coordonnées X et Y pour le coin supérieur gauche, ainsi que les valeurs de largeur et hauteur, et produit une structure de données de boîte englobante pouvant être utilisée par d'autres nœuds dans un workflow.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `x` | INT | Oui | 0 à 8192 | Coordonnée X du coin supérieur gauche de la boîte englobante (par défaut : 0). |
| `y` | INT | Oui | 0 à 8192 | Coordonnée Y du coin supérieur gauche de la boîte englobante (par défaut : 0). |
| `width` | INT | Oui | 1 à 8192 | Largeur de la boîte englobante (par défaut : 512). |
| `height` | INT | Oui | 1 à 8192 | Hauteur de la boîte englobante (par défaut : 512). |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `bounding_box` | BOUNDING_BOX | Structure de données contenant les propriétés `x`, `y`, `width` et `height` du rectangle défini. |

---
**Source fingerprint (SHA-256):** `715f1a2bd650ecd6ba2ea3c1d54636bc32dff4fb4aec8f088ee9b0994809412c`
