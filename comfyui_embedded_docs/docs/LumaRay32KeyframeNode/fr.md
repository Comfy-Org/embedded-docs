# LumaRay32KeyframeNode

Ce nœud ancre une image guide à une position spécifique sur la timeline de la vidéo de sortie de Luma Ray 3.2. Connectez ce nœud à l'entrée `keyframes` du nœud Luma Ray 3.2 Keyframes to Video, et enchaînez plusieurs images clés en connectant l'entrée optionnelle `keyframes`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | Image guide à placer au moment choisi de la vidéo de sortie. | IMAGE | Oui | - |
| `position` | Comment placer cette image sur la timeline de la vidéo de sortie. | COMBO | Oui | "Fraction de la durée (0.0-1.0)"<br>"Temps absolu (secondes)" |
| `keyframes` | Images clés antérieures optionnelles à enchaîner avec celle-ci. | LUMA_RAY32_KEYFRAME | Non | - |

Lorsque "Fraction de la durée (0.0-1.0)" est sélectionné pour le paramètre `position`, vous pouvez spécifier une valeur `fraction` (par défaut : 0.0, plage : 0.0 à 1.0, pas : 0.01) qui détermine à quel moment de la vidéo de sortie cette image s'applique (0.0 = début, 1.0 = fin).

Lorsque "Temps absolu (secondes)" est sélectionné pour le paramètre `position`, vous pouvez spécifier une valeur `seconds` (par défaut : 0.0, plage : 0.0 à 10.0, pas : 0.1) qui détermine le temps en secondes depuis le début de la vidéo de sortie où cette image s'applique.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `keyframes` | Une chaîne d'images clés qui inclut la nouvelle image clé combinée avec toutes les images clés antérieures optionnelles. | LUMA_RAY32_KEYFRAME |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframeNode/fr.md)

---
**Source fingerprint (SHA-256):** `b49d879888e6e83d6937068e799ea583ed5c90284e829ac496821eea330fe9c7`
