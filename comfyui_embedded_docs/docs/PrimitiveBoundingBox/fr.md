# Boîte englobante

Le nœud PrimitiveBoundingBox crée une zone rectangulaire simple définie par sa position et sa taille. Il prend les coordonnées X et Y pour le coin supérieur gauche, ainsi que les valeurs de largeur et de hauteur, et génère une structure de données de type bounding box utilisable par d'autres nœuds dans un workflow.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `x` | La coordonnée X du coin supérieur gauche de la boîte englobante (par défaut : 0). | INT | Oui | 0 à 16384 |
| `y` | La coordonnée Y du coin supérieur gauche de la boîte englobante (par défaut : 0). | INT | Oui | 0 à 16384 |
| `width` | La largeur de la boîte englobante (par défaut : 512). | INT | Oui | 1 à 16384 |
| `height` | La hauteur de la boîte englobante (par défaut : 512). | INT | Oui | 1 à 16384 |

Remarque : Toutes les valeurs maximales suivent la constante MAX_RESOLUTION de ComfyUI, qui définit la plus grande dimension d'image acceptée par le nœud.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `bounding_box` | Une structure de données contenant les propriétés `x`, `y`, `width` et `height` du rectangle défini. | BOUNDING_BOX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/fr.md)

---
**Source fingerprint (SHA-256):** `dc50286b09b8aaf7ff21eb699b9a04317f099b3deedb6cb7d4a1ec7668edeb97`
