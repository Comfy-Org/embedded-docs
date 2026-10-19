# Clarity AI Crystal Video Upscale

Effectuez la mise à l’échelle d’une vidéo avec Crystal Video Upscaler de Clarity AI, un upscaler haute fidélité qui reste fidèle à la source. Le clip est téléversé, mis à l’échelle selon le facteur que vous définissez, puis renvoyé sous forme de vidéo. La sortie est limitée à 9 mégapixels par image (par exemple 4000x2250) et à 360 mégapixels-secondes par clip ; ainsi, les clips volumineux ou longs sont renvoyés à une résolution inférieure à celle demandée par le facteur.

La sélection d’un `model` révèle les paramètres spécifiques à ce modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser. La sélection d’un modèle révèle les paramètres qui lui sont spécifiques : `video` et `scale_factor`. | DYNAMIC_COMBO | Oui | `"crystal-video-upscaler"` |
| `video` | La vidéo à mettre à l’échelle. | VIDEO | Oui | N/A |
| `scale_factor` | Facteur par lequel multiplier la largeur et la hauteur de la vidéo. La sortie est limitée à 9 mégapixels par image et à 360 mégapixels-secondes par clip ; les vidéos volumineuses ou longues sont donc mises à l’échelle dans une moindre mesure, et le facteur est de nouveau réduit lorsqu’il ferait dépasser 5120 pixels à un côté (par défaut : 2.0). | FLOAT | Oui | 1.0 à 200.0 (pas de 0.1) |

**Remarque :** Le clip peut mesurer au maximum 5120 pixels de chaque côté et au maximum 9 mégapixels par image. La durée maximale dépend de la taille de l’image et de la fréquence d’images : elle correspond à 360 mégapixels-secondes divisés par les pixels de l’image et par la fréquence d’images arrondie au multiple de 30 fps supérieur ; un clip 1080p à 30 fps peut donc durer jusqu’à environ 173 secondes. Les clips à plus de 30 fps coûtent 2 fois plus, à plus de 60 fps 3 fois plus, et ainsi de suite.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo mise à l’échelle. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClarityCrystalVideoUpscaleNode/fr.md)

---
**Source fingerprint (SHA-256):** `ca44ed6591474421edaf7e4e99e6da62e0c2e4e66964b7dac51d45758150aaa8`
