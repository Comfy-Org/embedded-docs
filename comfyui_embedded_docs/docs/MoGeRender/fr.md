> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/fr.md)

Voici la traduction en français de la documentation du nœud MoGeRender, conformément à vos règles :

## Aperçu

Ce nœud prend un paquet MOGE_GEOMETRY (produit par un nœud d'estimation de profondeur/normale MoGe) et le restitue dans un format d'image standard. Vous pouvez choisir de générer une carte de profondeur, une carte de profondeur colorée, une carte de normales ou un masque.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `moge_geometry` | MOGE_GEOMETRY | Oui | N/D | Le paquet de données géométriques provenant d'un nœud d'estimation MoGe. |
| `sortie` | COMBO | Oui | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` | Le type d'image à générer à partir des données géométriques. DirectX vs OpenGL contrôle la convention du canal vert de la carte de normales. DirectX : vert = -Y vers le bas (Unreal). OpenGL : vert = +Y vers le haut (Blender, Substance, Unity, glTF). (par défaut : "depth") |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `IMAGE` | IMAGE | L'image générée sous forme d'un lot de tenseurs RVB. Le contenu dépend du mode `sortie` : une carte de profondeur en niveaux de gris, une carte de profondeur colorée, une carte de normales ou un masque. |

---
**Source fingerprint (SHA-256):** `45ba499e746ce46f9b6f7773e3218bcf80ad2e8d65940b38e248cc2f20c8b2fe`
