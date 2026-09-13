# MoGe Render

Ce nœud prend un paquet MOGE_GEOMETRY (produit par un nœud d'estimation de profondeur/normales MoGe) et le rend dans un format d'image standard. Vous pouvez choisir de produire une carte de profondeur, une carte de profondeur colorée, une carte de normales ou un masque.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Le paquet de données géométriques provenant d'un nœud d'estimation MoGe. | MOGE_GEOMETRY | Oui | N/A |
| `output` | Le type d'image à rendre à partir des données de géométrie. `depth` produit une carte de profondeur en niveaux de gris, `depth_colored` produit une carte de profondeur colorée, `normal_opengl` et `normal_directx` produisent des cartes de normales, et `mask` produit un masque. DirectX vs OpenGL contrôle la convention du canal vert des cartes de normales. DirectX : vert = -Y vers le bas (Unreal). OpenGL : vert = +Y vers le haut (Blender, Substance, Unity, glTF). (par défaut : "depth") | COMBO | Oui | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

**Remarque :** Le paquet de géométrie doit contenir des données correspondant au mode `output` choisi. Les modes `depth` et `depth_colored` nécessitent des données de profondeur dans le paquet. Les modes `normal_opengl` et `normal_directx` nécessitent des données de normales, ou des données de points à partir desquelles les normales sont dérivées. Le mode `mask` nécessite des données de masque. Si les données requises sont absentes, le nœud déclenche une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | L'image rendue sous forme de lot de tenseurs RGB. Le contenu dépend du mode `output` : une carte de profondeur en niveaux de gris, une carte de profondeur colorée, une carte de normales ou un masque converti en RGB. La taille du lot de sortie correspond à la taille du lot de géométrie d'entrée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/fr.md)

---
**Source fingerprint (SHA-256):** `ca602f7a7d6eb1b1d00986459621d94ecf9331266ff1d3ce7bb759d24448a346`
