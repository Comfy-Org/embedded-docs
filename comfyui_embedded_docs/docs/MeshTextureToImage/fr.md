# MeshTextureToImage

Ce nœud extrait les textures cuites d’un maillage et les renvoie sous forme d’images distinctes : couleur de base, metallic, rugosité, occlusion et carte de normales. Les canaux de texture non cuits reviennent avec des valeurs neutres par défaut — blanc pour l’occlusion et bleu plat pour la carte de normales.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage dont les textures cuites sont extraites. Le maillage doit posséder une texture de couleur de base ; les maillages qui n’ont que des couleurs de sommets (par exemple après un nœud PaintMesh) ne contiennent pas de texture et provoquent une erreur. | MESH | Oui | — |

Remarque : le maillage doit avoir une texture de couleur de base cuite. À défaut, le nœud génère une erreur et recommande d’exécuter d’abord BakeTextureFromVoxel. Lorsque la texture metallic-roughness est manquante, les sorties `metallic` et `roughness` sont noires (0). La sortie `occlusion` est blanche sauf si le maillage contient une occlusion ambiante cuite. La sortie `normal_map` est un bleu neutre plat lorsqu’aucune carte de normales n’a été cuite.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `base_color` | La texture de couleur de base du maillage sous forme d’image. | IMAGE |
| `metallic` | Le canal metallic de la texture occlusion-roughness-metallic du maillage, sous forme d’image en niveaux de gris. Noir (0) signifie non métallique, blanc (1) signifie entièrement métallique. Noir lorsque la texture est manquante. | IMAGE |
| `roughness` | Le canal de rugosité de la texture occlusion-roughness-metallic du maillage, sous forme d’image en niveaux de gris. Noir lorsque la texture est manquante. | IMAGE |
| `occlusion` | Le canal d’occlusion ambiante de la texture occlusion-roughness-metallic du maillage, sous forme d’image en niveaux de gris. Blanc (pas d’occlusion) lorsque l’occlusion ambiante n’a pas été cuite. | IMAGE |
| `normal_map` | La texture de carte de normales du maillage. Une carte de normales neutre et plate (0,5, 0,5, 1,0, apparaissant comme un bleu plat) lorsqu’aucune carte de normales n’a été cuite. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshTextureToImage/fr.md)

---
**Source fingerprint (SHA-256):** `775fd50601ed9ebfc48abf1832c58acbac0f48b5faaebb5f7f46ae4a501278c4`
