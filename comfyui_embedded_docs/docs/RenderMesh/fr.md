# RenderMesh

```markdown
Ce nœud transforme un maillage 3D en image 2D en lançant des rayons depuis une seule vue. Il peut produire le maillage texturé, les couleurs de sommets, une surface ombrée unie, les normales de surface ou la profondeur. La caméra et la transformation facultative du modèle peuvent provenir d’un visualiseur Load3D / Preview3D ; si aucune caméra n’est connectée, une vue de face par défaut est automatiquement cadrée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage 3D à rendre. | MESH | Oui | — |
| `mode` | Ce qui doit être rendu. auto : texture si présente, sinon couleurs de sommets, sinon argile ombrée. (défaut : "auto") | COMBO | Oui | `"auto"`<br>`"texture"`<br>`"vertex colors"`<br>`"solid"`<br>`"normal"`<br>`"depth"` |
| `width` | Largeur de l’image rendue en pixels. (défaut : 1024) | INT | Oui | 64 à 4096 (pas de 8) |
| `height` | Hauteur de l’image rendue en pixels. (défaut : 1024) | INT | Oui | 64 à 4096 (pas de 8) |
| `background` | Couleur de fond utilisée pour les pixels non couverts par le maillage. (défaut : "#000000") | COLOR | Oui | — |
| `model_3d_info` | Transformation du modèle provenant du même visualiseur Load3D / Preview3D. Connectez-la avec `camera_info` pour correspondre au cadrage du visualiseur. | LOAD3D_MODEL_INFO | Non | — |
| `camera_info` | Caméra provenant d’un visualiseur Load3D / Preview3D ou d’un nœud Create Camera Info. Si aucune n’est connectée, une vue de face par défaut est automatiquement cadrée. | LOAD3D_CAMERA | Non | — |

Remarque : seul le premier élément d’un maillage par lots est rendu — si le lot de maillages contient plus d’un élément, le nœud journalise un avertissement et utilise le premier. Le mode `texture` nécessite que le maillage possède à la fois une texture et des UV, et le mode `vertex colors` nécessite des couleurs de sommets ; si les données pour le mode sélectionné ne sont pas disponibles, le nœud revient au rendu ombré uni. `model_3d_info` et `camera_info` sont destinés à être connectés ensemble depuis le même visualiseur Load3D / Preview3D afin que le rendu corresponde au cadrage du visualiseur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L’image rendue du maillage. | IMAGE |
| `mask` | Un masque qui vaut 1.0 là où le maillage a été rendu et 0.0 ailleurs. | MASK |
```

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderMesh/fr.md)

---
**Source fingerprint (SHA-256):** `d23e85a904520eb2dfed899eb3e6a9cf45c980df00c034503687ac4eccc66ac4`
