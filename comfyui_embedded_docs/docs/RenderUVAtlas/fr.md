# RenderUVAtlas

Rend la disposition UV d'un maillage sous forme d'image. Chaque région UV connectée (chart) est remplie d'une couleur distincte, et les limites des charts sont soulignées en noir sur un fond gris foncé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage 3D dont la disposition UV sera rendue. Le maillage doit avoir des coordonnées UV ; sinon, une erreur est levée. | MESH | Oui | - |
| `resolution` | La largeur et la hauteur, en pixels, de l'image rendue (par défaut : 1024). | INT | Oui | 64 à 4096 (pas de 64) |

Remarque : Si le maillage n'a pas de coordonnées UV, le nœud lève l'erreur « mesh has no UVs to render. Run UnwrapMesh first. » Si le maillage contient une dimension de lot (UV 3D ou tableaux de faces), seul le premier élément du lot est rendu.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image de l'atlas UV rendue, avec chaque chart coloré et les arêtes des limites de charts soulignées en noir. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderUVAtlas/fr.md)

---
**Source fingerprint (SHA-256):** `b462101036418350390ffed621e583c6de14d5ea34d1e427342dc44ec3fd1922`
