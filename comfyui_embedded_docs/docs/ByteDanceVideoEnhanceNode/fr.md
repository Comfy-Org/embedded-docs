# ByteDance vCube Video Enhance

Ce nœud effectue une montée en résolution et restaure des vidéos à l'aide de ByteDance vCube. Il peut augmenter la résolution jusqu'à 8K, supprimer les artefacts de compression et le bruit, améliorer les couleurs et la netteté, et éventuellement interpoler les images pour obtenir une fréquence d'images plus élevée. La vidéo est téléversée vers le service vCube, traitée avec le préréglage d'amélioration sélectionné, puis renvoyée sous la forme d'un fichier vidéo amélioré.

## Entrées

### Entrées communes

Ces entrées sont toujours visibles.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `vidéo` | Vidéo à améliorer. La résolution source doit être au maximum de 2560x1440 (2K) ; la taille de sortie est définie par l'entrée de résolution. | VIDEO | Oui | Au maximum 2560x1440 (2K) |
| `tool_version` | 'standard' équilibre la vitesse et la qualité avec plus de 10 algorithmes d'amélioration. 'professional' utilise plus de 30 algorithmes pour une restauration de niveau cinématographique, prend environ 3 fois plus de temps et coûte 10 fois plus cher. | DYNAMIC_COMBO | Oui | "standard"<br>"professional" |
| `résolution` | Résolution de sortie. Le côté court est défini sur le niveau choisi et le côté long suit le rapport d'aspect de la source. 'source' conserve la taille source, 'custom' définit le côté court en pixels. Les sources plus larges ou plus hautes qu'environ 2,2:1 sont facturées un niveau de résolution supérieur. | DYNAMIC_COMBO | Oui | "720p"<br>"1080p"<br>"2k"<br>"4k"<br>"8k"<br>"source"<br>"custom" |
| `fps` | Fréquence d'images de sortie. Une fréquence plus élevée que celle de la source active l'interpolation d'images par IA ; une fréquence plus faible supprime des images. 'source' conserve la fréquence source, jusqu'à 120 fps. Les fréquences supérieures à 30 fps coûtent 2x, et supérieures à 60 fps, 4x. (par défaut : "source") | COMBO | Oui | "source" (par défaut)<br>Fréquences d'images numériques jusqu'à 120 fps |
| `bitrate_level` | Débit binaire cible du fichier livré, mis à l'échelle selon la résolution et la fréquence d'images de sortie. (par défaut : "medium") | COMBO | Oui | "low"<br>"medium"<br>"high" |

### Entrées standard

Affichées lorsque `tool_version` est défini sur "standard".

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `scene` | Préréglage adapté au contenu : 'aigc' pour les séquences générées par IA, 'common' pour la vidéo générale, 'ugc' pour les clips de téléphone compressés, 'short_series' pour les drames avec des visages, 'old_film' pour les séquences d'archives rayées ou vacillantes. (par défaut : "aigc") | COMBO | Oui | "aigc"<br>"common"<br>"ugc"<br>"short_series"<br>"old_film" |
| `enhance_style` | 'hd' applique une amélioration plus nette ; 'natural' réduit la force pour un rendu plus doux et moins accentué. (par défaut : "hd") | COMBO | Oui | "hd"<br>"natural" |

### Entrées professionnelles

Affichées lorsque `tool_version` est défini sur "professional".

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `enhance_style` | 'hd' applique une amélioration plus nette ; 'natural' réduit la force pour un rendu plus doux et moins accentué. (par défaut : "hd") | COMBO | Oui | "hd"<br>"natural" |

### Entrées de résolution personnalisée

Affichées lorsque `resolution` est défini sur "custom".

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `short_side` | Côté court de la sortie en pixels ; le côté long suit le rapport d'aspect de la source. (par défaut : 1080) | INT | Oui | Valeur par défaut 1080 ; limitée par les limites minimale et maximale du côté court de vCube |

### Remarques

- La vidéo source doit être au maximum de 2560x1440 (2K). Les vidéos plus grandes sont rejetées et doivent être réduites avant l'amélioration.
- La durée de la vidéo source est limitée à la durée maximale prise en charge par le service vCube.
- Lorsque `tool_version` est "standard", `scene` et `enhance_style` sont tous deux disponibles. Lorsqu'il est "professional", seul `enhance_style` est disponible.
- Lorsque `resolution` est "custom", la valeur `short_side` est requise. Les préréglages de résolution et "source" n'utilisent pas `short_side`.
- Lorsque `resolution` est "source" et que le côté court de la source est au moins égal à la limite minimale de côté court, la sortie conserve la résolution source.
- Lorsque `fps` est "source", la fréquence d'images de sortie correspond à celle de la source, jusqu'à 120 fps.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo améliorée, mise à l'échelle et restaurée à la résolution et à la fréquence d'images demandées. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceVideoEnhanceNode/fr.md)

---
**Source fingerprint (SHA-256):** `bfdd55ce12cabd6e6504129084e86dcf96abd8db4ff64abbe5974c0da7a42bda`
