> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceMeshVisualize/fr.md)

Voici la traduction en français de la documentation du nœud MediaPipeFaceMeshVisualize :

## Aperçu

Dessine les points de repère du visage et les lignes de connexion (un maillage facial) sur une image d'entrée. Ce nœud utilise les données de repères produites par un nœud de détection faciale pour visualiser les caractéristiques faciales détectées, telles que les yeux, le nez, la bouche et le contour du visage.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `face_landmarks` | FACE_LANDMARKS | Oui | | Les données de repères faciaux provenant d'un nœud de détection. |
| `image` | IMAGE | Non | | L'image sur laquelle dessiner le maillage. Si non connectée, un canevas noir de la même taille que le résultat de la détection sera utilisé. |
| `connections` | COMBO | Oui | `"all"`<br>`"fill"`<br>`"custom"` | Détermine les parties du maillage facial à dessiner. `"all"` dessine le maillage complet (ovale, yeux, sourcils, lèvres, iris, nez). `"fill"` dessine un polygone plein de l'ovale du visage (masque de silhouette). `"custom"` vous permet d'activer ou désactiver chaque caractéristique individuellement. (par défaut : `"all"`) |
| `color` | COLOR | Oui | | La couleur des lignes et des points du maillage. (par défaut : `#00ff00`) |
| `thickness` | INT | Oui | 0 à 8 | L'épaisseur des lignes du maillage en pixels. Mettre cette valeur à 0 désactive le dessin des lignes. (par défaut : 1) |
| `point_size` | INT | Oui | 0 à 16 | Le rayon des points de repère en pixels. Mettre cette valeur à 0 désactive le dessin des points. (par défaut : 2) |

**Remarque sur le paramètre `connections` :** Lorsque `"custom"` est sélectionné, des entrées booléennes supplémentaires apparaissent pour chaque caractéristique faciale (par exemple, `face_oval`, `lips`, `left_eye`, `right_eye`, `left_eyebrow`, `right_eyebrow`, `left_iris`, `right_iris`, `nose`, `tesselation`). Seules les caractéristiques que vous activez seront dessinées.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `IMAGE` | IMAGE | L'image d'entrée avec le maillage des repères faciaux dessiné dessus. |

---
**Source fingerprint (SHA-256):** `fb5437d73378b0c8daa68669c2e19058ccb7133ed68fc51c8d4c5bab8662f243`
