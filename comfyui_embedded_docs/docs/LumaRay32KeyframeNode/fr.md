# Luma Ray 3.2 Image Clé

Ce nœud ancre une image guide à une position spécifique sur la chronologie de la vidéo de sortie de Luma Ray 3.2. Connectez ce nœud à l'entrée « keyframes » du nœud Luma Ray 3.2 Keyframes to Video, et chaînez plusieurs keyframes ensemble en connectant l'entrée optionnelle « keyframes ».

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | Image guide à placer au moment choisi de la vidéo de sortie. | IMAGE | Oui | - |
| `position` | Comment placer cette image sur la chronologie de la vidéo de sortie. | DYNAMIC_COMBO | Oui | "Fraction of duration (0.0-1.0)"<br>"Absolute time (seconds)" |
| `keyframes` | Keyframes antérieurs optionnels à chaîner avec ce keyframe. | LUMA_RAY32_KEYFRAME | Non | - |

### Entrées Fraction of duration (0.0-1.0)

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `fraction` | Où, dans la vidéo de sortie, cette image s'applique (0.0 = début, 1.0 = fin). Par défaut : 0.0. | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |

### Entrées Absolute time (seconds)

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `seconds` | Temps en secondes depuis le début de la vidéo de sortie où cette image s'applique. Par défaut : 0.0. | FLOAT | Oui | 0.0 à 10.0 (pas : 0.1) |

Le paramètre `position` détermine quelle valeur est utilisée pour placer l'image sur la chronologie. Seul le sous-paramètre correspondant à l'option sélectionnée est affiché et utilisé : `fraction` pour « Fraction of duration (0.0-1.0) » et `seconds` pour « Absolute time (seconds) ».

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `keyframes` | Une chaîne de keyframes qui inclut le nouveau keyframe combiné aux éventuels keyframes antérieurs optionnels. | LUMA_RAY32_KEYFRAME |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframeNode/fr.md)

---
**Source fingerprint (SHA-256):** `b49d879888e6e83d6937068e799ea583ed5c90284e829ac496821eea330fe9c7`
