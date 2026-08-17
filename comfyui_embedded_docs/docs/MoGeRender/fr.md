# MoGe Render

## Vue d'ensemble

Ce nœud prend un paquet MOGE_GEOMETRY (produit par un nœud d'estimation de profondeur/normales MoGe) et le convertit en une image standard. Vous pouvez choisir de générer une carte de profondeur, une carte de profondeur colorée, une carte de normales ou un masque.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Le paquet de données géométriques provenant d'un nœud d'estimation MoGe. | MOGE_GEOMETRY | Oui | N/A |
| `output` | Le type d'image à générer à partir des données géométriques. DirectX vs OpenGL contrôle la convention du canal vert de la carte de normales. DirectX : vert = -Y vers le bas (Unreal). OpenGL : vert = +Y vers le haut (Blender, Substance, Unity, glTF). (par défaut : "depth") | COMBO | Oui | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

**Remarque :** Le mode `output` sélectionné détermine quelles données doivent être présentes dans `moge_geometry` :
- `depth` et `depth_colored` nécessitent des données de profondeur. La profondeur est convertie en une carte de disparité normalisée (1/profondeur) en utilisant un écrêtage aux percentiles 0,1/99,9.
- `normal_opengl` et `normal_directx` nécessitent des données de normales, ou des données de points à partir desquelles les normales peuvent être dérivées. Le nœud génère une erreur si aucune de ces données n'est présente.
- `mask` nécessite des données de masque.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | L'image rendue sous forme d'un lot de tenseurs RGB. Le contenu dépend du mode `output` : une carte de profondeur en niveaux de gris, une carte de profondeur colorée, une carte de normales ou un masque. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/fr.md)

---
**Source fingerprint (SHA-256):** `ca602f7a7d6eb1b1d00986459621d94ecf9331266ff1d3ce7bb759d24448a346`
