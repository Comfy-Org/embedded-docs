# Compose Camera Angle Prompt

Ce nœud choisit un angle de caméra autour d'un sujet et transforme ce choix en deux éléments : une structure `camera_info` que les nœuds 3D peuvent rendre, et une description de plan en anglais simple que vous pouvez coller dans un prompt. Le sujet se trouve à l'origine de la scène, où les nœuds 3D en aval centrent leurs modèles, de sorte que l'angle que vous choisissez ici correspond à l'aperçu.

Utilisez-le pour cadrer un rendu avant la génération, ou pour décrire un point de vue tel que `front view eye-level shot medium shot` pour un modèle d'image ou de vidéo. L'aperçu 3D dans le nœud montre la position résultante de la caméra.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `horizontal_angle` | Azimut autour du sujet en degrés : 0 correspond à l'avant, 90 au côté droit et 180 à l'arrière. (par défaut : 0) | INT | Oui | 0 à 360 |
| `vertical_angle` | Élévation en degrés. Les valeurs négatives regardent vers le haut depuis le bas, les valeurs positives regardent vers le bas depuis le haut. (par défaut : 0) | INT | Oui | -30 à 60 |
| `zoom` | Zoom de l'objectif sur le sujet : 0 correspond à un plan large, 10 à un gros plan. La valeur est également reportée dans `camera_info.zoom`. (par défaut : 5.0) | FLOAT | Oui | 0.0 à 10.0 (pas de 0.1) |
| `image` | Image de référence facultative, affichée sur la face avant du cube du sujet dans l'aperçu 3D. | IMAGE | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `camera_info` | Informations de caméra pour les nœuds 3D : position, cible de visée, facteur de zoom, type de caméra et champ de vision. La caméra conserve un champ de vision fixe de 35 degrés et est placée à 6 unités de la cible. | LOAD3DCAMERA |
| `prompt` | Brève description de plan construite à partir de l'angle, de l'élévation et de la distance, par exemple `front view eye-level shot medium shot`. | STRING |

## Termes de description de plan

La sortie `prompt` combine un terme de chaque groupe ci-dessous. Les valeurs sont d'abord contraintes aux plages des widgets.

- L'angle horizontal est divisé en huit secteurs de 45 degrés : `front view`, `front-right quarter view`, `right side view`, `back-right quarter view`, `back view`, `back-left quarter view`, `left side view`, `front-left quarter view`.
- L'angle vertical devient `low-angle shot` en dessous de -15 degrés, `eye-level shot` en dessous de 15, `elevated shot` en dessous de 45, et `high-angle shot` à partir de 45 degrés.
- Le zoom devient `wide shot` en dessous de 2, `medium shot` en dessous de 6, et `close-up` à partir de 6.

Le facteur `camera_info.zoom` met à l'échelle la valeur du widget sur 1.0 à 1.875, donc un zoom de 0 donne 1.0 et un zoom de 10 donne 1.875.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CameraAngle/fr.md)

---
**Source fingerprint (SHA-256):** `8ed2cd186bc6ca02dbc8da006b2e9156245ef691a2257f286f6e32ffa480fd5d`
