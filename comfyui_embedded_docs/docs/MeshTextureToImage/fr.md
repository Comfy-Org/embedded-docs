# MeshTextureToImage

Ce nœud extrait les textures cuites d'un maillage et les renvoie sous forme d'images séparées : couleur de base, métallique, rugosité, occlusion et carte des normales. Les canaux de texture qui n'ont pas été cuits reviennent avec des valeurs neutres par défaut — blanc pour l'occlusion et bleu plat pour la carte des normales.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage dont les textures cuites sont extraites. Le maillage doit avoir une texture de couleur de base ; les maillages qui n'ont que des couleurs de sommet (par exemple après un nœud PaintMesh) ne contiennent pas de texture et provoquent une erreur. | MESH | Oui | — |

Remarque : Le maillage doit avoir une texture de couleur de base cuite. Si ce n'est pas le cas, le nœud génère une erreur et recommande d'exécuter BakeTextureFromVoxel d'abord. Lorsque la texture métallique-rugosité est manquante, les sorties `metallic` et `roughness` sont noires (0). La sortie `occlusion` est blanche à moins que le maillage ne contienne une occlusion ambiante cuite. La sortie `normal_map` est un bleu neutre et plat lorsqu'aucune carte des normales n'a été cuite.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `base_color` | La texture de couleur de base du maillage sous forme d'image. | IMAGE |
| `metallic` | Le canal métallique de la texture occlusion-rugosité-métallique du maillage, sous forme d'image en niveaux de gris. Le noir (0) signifie non métallique, le blanc (1) signifie entièrement métallique. Noir lorsque la texture est manquante. | IMAGE |
| `roughness` | Le canal de rugosité de la texture occlusion-rugosité-métallique du maillage, sous forme d'image en niveaux de gris. Noir lorsque la texture est manquante. | IMAGE |
| `occlusion` | Le canal d'occlusion ambiante de la texture occlusion-rugosité-métallique du maillage, sous forme d'image en niveaux de gris. Blanc (pas d'occlusion) lorsque l'occlusion ambiante n'a pas été cuite. | IMAGE |
| `normal_map` | La texture de carte des normales du maillage. Une carte des normales neutre et plate (0,5, 0,5, 1,0, apparaissant comme un bleu plat) lorsqu'aucune carte des normales n'a été cuite. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshTextureToImage/fr.md)

---
**Source fingerprint (SHA-256):** `775fd50601ed9ebfc48abf1832c58acbac0f48b5faaebb5f7f46ae4a501278c4`
