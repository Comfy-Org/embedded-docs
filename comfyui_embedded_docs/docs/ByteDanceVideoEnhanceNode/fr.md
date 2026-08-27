# ByteDanceVideoEnhanceNode

Ce nœud agrandit et restaure des vidéos à l’aide de ByteDance vCube. Il peut augmenter la résolution jusqu’à 8K, supprimer les artefacts de compression et le bruit, améliorer la couleur et la netteté, et éventuellement interpoler les images pour obtenir une cadence plus élevée. La vidéo est téléversée sur le service vCube, traitée avec le préréglage d’amélioration sélectionné, puis renvoyée sous forme de fichier vidéo amélioré.

## Entrées

### Entrées communes

Ces entrées sont toujours visibles.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | Vidéo à améliorer. La résolution source doit être au maximum de 2560x1440 (2K) ; la taille de sortie est définie par l’entrée de résolution. | VIDEO | Oui | Au maximum 2560x1440 (2K) |
| `tool_version` | « standard » équilibre vitesse et qualité avec 10+ algorithmes d’amélioration. « professional » utilise 30+ algorithmes pour une restauration de qualité cinéma, prend environ 3x plus de temps et coûte 10x plus cher. | DYNAMIC_COMBO | Oui | "standard"<br>"professional" |
| `resolution` | Résolution de sortie. Le petit côté est défini au niveau choisi et le grand côté suit le ratio d’aspect de la source. « source » conserve la taille source, « custom » définit le petit côté en pixels. Les sources plus larges ou plus hautes qu’environ 2.2:1 sont facturées un palier de résolution au-dessus. | DYNAMIC_COMBO | Oui | "720p"<br>"1080p"<br>"2k"<br>"4k"<br>"8k"<br>"source"<br>"custom" |
| `fps` | Cadence de sortie. Une cadence supérieure à la source permet l’interpolation d’images par IA ; une cadence inférieure supprime des images. « source » conserve la cadence source, jusqu’à 120 fps. Les cadences au-dessus de 30 fps coûtent 2x, au-dessus de 60 fps 4x. (défaut : "source") | COMBO | Oui | "source" (défaut)<br>Cadences numériques jusqu’à 120 fps |
| `bitrate_level` | Débit binaire cible du fichier livré, adapté à la résolution et à la cadence de sortie. (défaut : "medium") | COMBO | Oui | "low"<br>"medium"<br>"high" |

### Entrées standard

Affichées lorsque `tool_version` est défini sur « standard ».

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `scene` | Préréglage adapté au contenu : « aigc » pour les séquences générées par IA, « common » pour les vidéos générales, « ugc » pour les clips téléphoniques compressés, « short_series » pour les drames avec visages, « old_film » pour les images d’archives rayées ou papillotantes. (défaut : "aigc") | COMBO | Oui | "aigc"<br>"common"<br>"ugc"<br>"short_series"<br>"old_film" |
| `enhance_style` | « hd » applique une amélioration plus nette ; « natural » réduit l’intensité pour un rendu plus doux et moins accentué. (défaut : "hd") | COMBO | Oui | "hd"<br>"natural" |

### Entrées professionnelles

Affichées lorsque `tool_version` est défini sur « professional ».

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `enhance_style` | « hd » applique une amélioration plus nette ; « natural » réduit l’intensité pour un rendu plus doux et moins accentué. (défaut : "hd") | COMBO | Oui | "hd"<br>"natural" |

### Entrées de résolution personnalisée

Affichées lorsque `resolution` est défini sur « custom ».

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `short_side` | Petit côté de la sortie en pixels ; le grand côté suit le ratio d’aspect de la source. (défaut : 1080) | INT | Oui | Défaut 1080 ; limité par les limites minimale et maximale du petit côté de vCube |

### Remarques

- La vidéo source doit être au maximum de 2560x1440 (2K). Les vidéos plus grandes sont rejetées et doivent être réduites avant l’amélioration.
- La durée de la vidéo source est limitée à la durée maximale prise en charge par le service vCube.
- Lorsque `tool_version` est défini sur « standard », `scene` et `enhance_style` sont tous deux disponibles. Lorsqu’il est défini sur « professional », seul `enhance_style` est disponible.
- Lorsque `resolution` est défini sur « custom », la valeur `short_side` est requise. Les préréglages de résolution et « source » n’utilisent pas `short_side`.
- Lorsque `resolution` est défini sur « source », la sortie conserve la résolution source.
- Lorsque `fps` est défini sur « source », la cadence de sortie correspond à la cadence source, jusqu’à 120 fps.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo améliorée, agrandie et restaurée à la résolution et à la cadence demandées. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceVideoEnhanceNode/fr.md)

---
**Source fingerprint (SHA-256):** `bfdd55ce12cabd6e6504129084e86dcf96abd8db4ff64abbe5974c0da7a42bda`
