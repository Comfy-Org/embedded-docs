> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/fr.md)

Voici la traduction en français de la documentation du nœud Resolution Selector :

Le nœud Resolution Selector calcule la largeur et la hauteur en pixels d'une image en fonction d'un rapport hauteur/largeur choisi et d'une résolution totale cible en mégapixels. Il est utile pour générer des dimensions cohérentes pour d'autres nœuds, tels que le nœud Empty Latent Image. Les dimensions de sortie sont toujours arrondies au multiple de 8 le plus proche.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `ratio d'aspect` | COMBO | Oui | `"SQUARE"`<br>`"PORTRAIT_2_3"`<br>`"PORTRAIT_3_4"`<br>`"PORTRAIT_9_16"`<br>`"LANDSCAPE_3_2"`<br>`"LANDSCAPE_4_3"`<br>`"LANDSCAPE_16_9"` | Le rapport hauteur/largeur pour les dimensions de sortie (par défaut : `"SQUARE"`). |
| `mégapixels` | FLOAT | Oui | 0,1 - 16,0 | Nombre total de mégapixels cible. 1,0 MP ≈ 1024×1024 pour un rapport hauteur/largeur carré (par défaut : 1,0). |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `hauteur` | INT | La largeur calculée en pixels, qui est un multiple de 8. |
| `height` | INT | La hauteur calculée en pixels, qui est un multiple de 8. |

---
**Source fingerprint (SHA-256):** `221d38fa72c9989e06b706d33fd3e0dc4caa0f741dd2931864c58a6bd7f52613`
