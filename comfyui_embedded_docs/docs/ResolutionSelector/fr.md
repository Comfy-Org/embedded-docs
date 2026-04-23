> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/fr.md)

Le nœud Resolution Selector calcule la largeur et la hauteur en pixels d'une image en fonction d'un rapport d'aspect choisi et d'une résolution totale cible en mégapixels. Il est utile pour générer des dimensions cohérentes pour d'autres nœuds, comme le nœud Empty Latent Image. Les dimensions de sortie sont toujours arrondies au multiple de 8 le plus proche.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `aspect_ratio` | COMBO | Oui | `"SQUARE"`<br>`"PORTRAIT_2_3"`<br>`"PORTRAIT_3_4"`<br>`"PORTRAIT_9_16"`<br>`"LANDSCAPE_3_2"`<br>`"LANDSCAPE_4_3"`<br>`"LANDSCAPE_16_9"` | Le rapport d'aspect pour les dimensions de sortie (par défaut : `"SQUARE"`). |
| `megapixels` | FLOAT | Oui | 0.1 - 16.0 | Résolution totale cible en mégapixels. 1,0 MP ≈ 1024×1024 pour un rapport d'aspect carré (par défaut : 1.0). |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `width` | INT | La largeur calculée en pixels, qui est un multiple de 8. |
| `height` | INT | La hauteur calculée en pixels, qui est un multiple de 8. |