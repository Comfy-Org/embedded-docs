# Recraft Style - Logo Raster

Ce nœud sélectionne le style raster de logo et un sous-style pour générer des images de logo. Il est spécialisé dans la création de conceptions de logo avec des traitements visuels basés sur le raster.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `sous-style` | Le sous-style raster de logo spécifique à appliquer pour la génération de logo | STRING | Oui | `"bold"`<br>`"minimal"`<br>`"vibrant"`<br>`"handdrawn"`<br>`"geometric"`<br>`"vintage"`<br>`"neon"`<br>`"gradient"`<br>`"flat"`<br>`"outline"`<br>`"mascot"`<br>`"badge"`<br>`"abstract"`<br>`"retro"`<br>`"modern"`<br>`"playful"`<br>`"luxury"`<br>`"tech"`<br>`"nature"`<br>`"food"`<br>`"sport"`<br>`"fashion"`<br>`"music"`<br>`"travel"`<br>`"education"`<br>`"health"`<br>`"finance"`<br>`"realestate"`<br>`"nonprofit"` |

Remarque : Un sous-style doit toujours être sélectionné ; il n'y a pas d'option « none ».

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `recraft_style` | La configuration de style Recraft sélectionnée, incluant le style raster de logo et le sous-style choisi | CUSTOM |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3LogoRaster/fr.md)

---
**Source fingerprint (SHA-256):** `59c3af980261d2b20b6d401980639c6bbc3a8b7c4e2370ca048ccb07535b10e7`
