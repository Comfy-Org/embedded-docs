# Rendre le maillage

Ce nœud effectue le rendu d'un maillage 3D en image 2D par lancer de rayons sur une vue unique. Il peut produire en sortie le maillage texturé, les couleurs de sommets, une surface ombrée unie, les normales de surface ou la profondeur. La caméra et la transformation de modèle facultative peuvent provenir d'une visionneuse Load3D / Preview3D ; si aucune caméra n'est connectée, une vue de face par défaut est cadrée automatiquement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage 3D à rendre. | MESH | Oui | — |
| `mode` | Ce qu'il faut rendre. auto : texture si présente, sinon `vertex colors`, sinon rendu ombré type argile. (par défaut : `"auto"`) | COMBO | Oui | `"auto"`<br>`"texture"`<br>`"vertex colors"`<br>`"solid"`<br>`"normal"`<br>`"depth"` |
| `width` | Largeur de l'image rendue en pixels. (par défaut : 1024) | INT | Oui | 64 à 4096 (pas de 8) |
| `height` | Hauteur de l'image rendue en pixels. (par défaut : 1024) | INT | Oui | 64 à 4096 (pas de 8) |
| `background` | Couleur d'arrière-plan utilisée pour les pixels que le maillage ne couvre pas. (par défaut : `#000000`) | COLOR | Oui | — |
| `model_3d_info` | Transformation du modèle issue de la même visionneuse Load3D / Preview3D. Connectez-la avec `camera_info` pour correspondre au cadrage de la visionneuse. | LOAD3D_MODEL_INFO | Non | — |
| `camera_info` | Caméra issue d'une visionneuse Load3D / Preview3D ou d'un nœud Create Camera Info. Si aucune n'est connectée, une vue de face par défaut est cadrée automatiquement. | LOAD3D_CAMERA | Non | — |

Remarque : seul le premier élément d'un maillage en lot est rendu — si le lot de maillages contient plus d'un élément, le nœud journalise un avertissement et utilise le premier. Le mode `texture` exige que le maillage possède à la fois une texture et des UV, et le mode `vertex colors` exige des couleurs de sommets ; si les données du mode sélectionné ne sont pas disponibles, le nœud revient au rendu `solid`. Le mode `normal` utilise les normales de sommets lissées du maillage lorsqu'elles sont présentes, sinon la normale par face. En mode `depth`, les surfaces les plus proches apparaissent plus claires (proche = blanc) et les pixels non couverts par le maillage restent noirs. Les entrées `model_3d_info` et `camera_info` sont conçues pour être connectées ensemble depuis la même visionneuse Load3D / Preview3D afin que le rendu corresponde au cadrage de la visionneuse.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image rendue du maillage. | IMAGE |
| `mask` | Un masque qui vaut 1.0 là où le maillage a été rendu et 0.0 ailleurs. | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderMesh/fr.md)

---
**Source fingerprint (SHA-256):** `d23e85a904520eb2dfed899eb3e6a9cf45c980df00c034503687ac4eccc66ac4`
