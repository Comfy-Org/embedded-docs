# Créer les Informations de Caméra

Le nœud Créer les Informations de Caméra construit une structure d'informations de caméra pour le rendu 3D. Il prend en charge trois modes pour définir la caméra : orbite (lacet/tangage/distance autour d'une cible), regarder_vers (position explicite dans le monde) et quaternion (position plus rotation). Le système de coordonnées est droitier avec Y comme axe vertical.

## Entrées

| Paramètre | Description | Type de Données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mode` | Comment définir la caméra : angles d'orbite, une position explicite, ou une position + quaternion. | COMBO | Oui | `"orbit"`<br>`"look_at"`<br>`"quaternion"` |
| `target_x` | Point de visée (pivot d'orbite / cible). En mode orbite, le déplacer permet de panoramiquer/translater toute la caméra. Ignoré en mode quaternion. Par défaut à l'origine. (défaut : 0.0) | FLOAT | Non | -1000.0 à 1000.0 |
| `target_y` | Composante Y du point cible. (défaut : 0.0) | FLOAT | Non | -1000.0 à 1000.0 |
| `target_z` | Composante Z du point cible. (défaut : 0.0) | FLOAT | Non | -1000.0 à 1000.0 |
| `roll` | Roulis de la caméra autour de l'axe de vue, en degrés. (défaut : 0.0) | FLOAT | Non | -180.0 à 180.0 |
| `fov` | Champ de vision vertical en degrés. (défaut : 35.0) | FLOAT | Non | 1.0 à 120.0 |
| `zoom` | Zoom numérique (multiplicateur de distance focale). Les valeurs supérieures à 1 zooment sans déplacer la caméra. (défaut : 1.0) | FLOAT | Non | 0.01 à 100.0 |
| `camera_type` | Projection utilisée par Render Splat : perspective (raccourci) ou orthographique (parallèle). (défaut : "perspective") | COMBO | Non | `"perspective"`<br>`"orthographic"` |

### Paramètres Spécifiques au Mode

Lorsque `mode` est réglé sur `"orbit"`, les paramètres suivants deviennent disponibles :

| Paramètre | Description | Type de Données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `yaw` | Angle de rotation horizontale autour de la cible. (défaut : 35.0) | FLOAT | Oui | -360.0 à 360.0 |
| `pitch` | Angle de rotation verticale autour de la cible. (défaut : 30.0) | FLOAT | Oui | -89.0 à 89.0 |
| `distance` | Distance de la caméra par rapport à la cible. (défaut : 4.0) | FLOAT | Oui | 0.01 à 1000.0 |

Lorsque `mode` est réglé sur `"look_at"`, les paramètres suivants deviennent disponibles :

| Paramètre | Description | Type de Données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `position_x` | Position de la caméra dans l'espace monde (droitier, Y vers le haut). (défaut : 4.0) | FLOAT | Oui | -1000.0 à 1000.0 |
| `position_y` | Composante Y de la position de la caméra. (défaut : 4.0) | FLOAT | Oui | -1000.0 à 1000.0 |
| `position_z` | Composante Z de la position de la caméra. (défaut : 4.0) | FLOAT | Oui | -1000.0 à 1000.0 |

Lorsque `mode` est réglé sur `"quaternion"`, les paramètres suivants deviennent disponibles :

| Paramètre | Description | Type de Données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `position_x` | Position de la caméra dans l'espace monde (droitier, Y vers le haut). (défaut : 4.0) | FLOAT | Oui | -1000.0 à 1000.0 |
| `position_y` | Composante Y de la position de la caméra. (défaut : 4.0) | FLOAT | Oui | -1000.0 à 1000.0 |
| `position_z` | Composante Z de la position de la caméra. (défaut : 4.0) | FLOAT | Oui | -1000.0 à 1000.0 |
| `quat_x` | Composante X du quaternion de rotation mondiale de la caméra. (défaut : 0.0) | FLOAT | Oui | -1.0 à 1.0 |
| `quat_y` | Composante Y du quaternion de rotation mondiale de la caméra. (défaut : 0.0) | FLOAT | Oui | -1.0 à 1.0 |
| `quat_z` | Composante Z du quaternion de rotation mondiale de la caméra. (défaut : 0.0) | FLOAT | Oui | -1.0 à 1.0 |
| `quat_w` | Quaternion de rotation mondiale de la caméra (three.js : regarde vers le -Z local). Normalisé automatiquement. (défaut : 1.0) | FLOAT | Oui | -1.0 à 1.0 |

**Remarque :** Les paramètres `target_x`, `target_y` et `target_z` sont ignorés lorsque `mode` est réglé sur `"quaternion"`. En mode `"orbit"`, ces paramètres de cible définissent le point pivot autour duquel la caméra orbite.

## Sorties

| Nom de Sortie | Description | Type de Données |
|---------------|-------------|-----------------|
| `camera_info` | Structure d'informations de caméra contenant la position, la rotation, le champ de vision, le zoom et le type de projection pour le rendu 3D. | LOAD3DCAMERA |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateCameraInfo/fr.md)

---
**Source fingerprint (SHA-256):** `577c114130f72b753d5f15775fe05b3e1e734f5865cca32c576d042583f8e873`
