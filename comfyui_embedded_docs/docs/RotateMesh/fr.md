# RotateMesh

Faites pivoter un maillage 3D autour des axes du monde en utilisant soit des angles d'Euler XYZ (en degrés), soit un quaternion. La rotation est appliquée aux sommets du maillage, et les normales ainsi que les tangentes sont également pivotées afin que l'éclairage et l'ombrage restent corrects.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mode` | Le mode de rotation à utiliser. `"euler_xyz"` applique la rotation selon les angles X, puis Y, puis Z autour des axes du monde (en degrés). `"quaternion"` utilise un quaternion (w, x, y, z) qui est automatiquement normalisé. | DYNAMIC_COMBO | Oui | `"euler_xyz"`<br>`"quaternion"` |
| `mesh` | Le maillage 3D à faire pivoter. | MESH | Oui | — |

### Entrées euler_xyz

Ces entrées apparaissent lorsque `mode` est défini sur `"euler_xyz"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `angle_x` | Rotation autour de l'axe X en degrés. (défaut : 0.0) | FLOAT | Non | -360.0 à 360.0 (pas : 0.1) |
| `angle_y` | Rotation autour de l'axe Y en degrés. (défaut : 0.0) | FLOAT | Non | -360.0 à 360.0 (pas : 0.1) |
| `angle_z` | Rotation autour de l'axe Z en degrés. (défaut : 0.0) | FLOAT | Non | -360.0 à 360.0 (pas : 0.1) |

### Entrées quaternion

Ces entrées apparaissent lorsque `mode` est défini sur `"quaternion"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `qw` | Composante W du quaternion (w, x, y, z). (défaut : 1.0) | FLOAT | Non | -1.0 à 1.0 (pas : 0.001) |
| `qx` | Composante X du quaternion (w, x, y, z). (défaut : 0.0) | FLOAT | Non | -1.0 à 1.0 (pas : 0.001) |
| `qy` | Composante Y du quaternion (w, x, y, z). (défaut : 0.0) | FLOAT | Non | -1.0 à 1.0 (pas : 0.001) |
| `qz` | Composante Z du quaternion (w, x, y, z). (défaut : 0.0) | FLOAT | Non | -1.0 à 1.0 (pas : 0.001) |

**Remarque :** Lorsque `mode` est `"euler_xyz"` et que les trois angles sont à 0.0, ou lorsque `mode` est `"quaternion"` et que le quaternion est l'identité (1, 0, 0, 0), le maillage est renvoyé inchangé. Le quaternion est automatiquement normalisé avant utilisation ; si sa magnitude est trop proche de zéro, le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mesh` | Le maillage pivoté. Les sommets sont pivotés et les normales sont pivotées en tant que directions. Les tangentes voient leurs composantes X, Y, Z pivotées tandis que la composante W (chiralité) reste inchangée. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RotateMesh/fr.md)

---
**Source fingerprint (SHA-256):** `38b120a3f719264d1269275ecfefa145b507c688735e4a461bb89517c697674f`
