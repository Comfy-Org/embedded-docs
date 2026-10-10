# Clarity AI Crystal Upscale

Agrandissez une image avec Crystal Upscaler de Clarity AI, un upscaler haute fidélité qui reste fidèle à l’original tout en restaurant les visages, la peau et les textures fines. L’image est envoyée à l’API de Clarity AI et le résultat agrandi est renvoyé sous forme d’image.

La sélection d’un `model` révèle les paramètres spécifiques à ce modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser. La sélection d’un modèle révèle les paramètres qui lui sont propres : `image`, `scale_factor` et `creativity`. | DYNAMIC_COMBO | Oui | `"crystal-upscaler"` |
| `image` | L’image à agrandir. Doit contenir exactement une image ; les lots d’images ne sont pas pris en charge. | IMAGE | Oui | N/A |
| `scale_factor` | Facteur par lequel multiplier la largeur et la hauteur de l’image. La sortie est limitée à 100 mégapixels (valeur par défaut : 2.0). | FLOAT | Oui | 1.0 à 200.0 (pas de 0.1) |
| `creativity` | Des valeurs plus élevées permettent au modèle de reconstruire davantage de détails au lieu de préserver strictement l’original. N’a aucun effet sur les images dont le côté le plus court est de 256 pixels ou moins (valeur par défaut : 0). | INT | Oui | 0 à 10 |

**Remarque :** L’image d’entrée doit être d’au moins 2x2 pixels. La sortie est plafonnée à 100 mégapixels et 65535 pixels par côté ; un résultat plus grand déclenche une erreur, utilisez donc une image plus petite ou un `scale_factor` plus faible.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L’image agrandie. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClarityCrystalUpscaleNode/fr.md)

---
**Source fingerprint (SHA-256):** `38c90cf7054a93477ee63c356c3fdf8ba38c7edaf1a337da7ac366cd9d746d9e`
