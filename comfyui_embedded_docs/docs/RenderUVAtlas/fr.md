# Rendre l’atlas UV

Rend la disposition UV d’un maillage sous forme d’image. Chaque région UV connectée (chart) est remplie d’une couleur distincte, et les arêtes de délimitation des charts sont tracées en noir sur un fond gris foncé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage 3D dont la disposition UV sera rendue. Le maillage doit avoir des coordonnées UV ; sinon, le nœud renvoie l’erreur « mesh has no UVs to render. Run UnwrapMesh first. » | MESH | Oui | - |
| `resolution` | La largeur et la hauteur, en pixels, de l’image carrée rendue (par défaut : 1024). | INT | Oui | 64 à 4096 (pas de 64) |

Remarque : Si le maillage contient une dimension de lot (tableaux UV ou de faces 3D), seul le premier élément du lot est rendu.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L’image de l’atlas UV rendue, retournée sous forme de lot d’une seule image. Chaque chart UV est coloré, et les arêtes de délimitation des charts sont contourées en noir. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderUVAtlas/fr.md)

---
**Source fingerprint (SHA-256):** `b462101036418350390ffed621e583c6de14d5ea34d1e427342dc44ec3fd1922`
