# Inférence MoGe

Exécutez MoGe sur des images pour estimer la profondeur et la géométrie. Ce nœud traite une image d’entrée avec le modèle MoGe afin de générer un nuage de points 3D, une carte de profondeur, les paramètres intrinsèques de la caméra, un masque et les normales de surface.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `moge_model` | Le modèle MoGe à utiliser pour l’inférence. | MOGE_MODEL | Oui | N/A |
| `image` | L’image d’entrée pour l’estimation de la profondeur et de la géométrie. Seuls les trois premiers canaux de couleur (RVB) sont utilisés. | IMAGE | Oui | N/A |
| `resolution_level` | Contrôle la résolution de traitement. 0 = le plus rapide, 9 = le plus détaillé. (par défaut : 9) | INT | Oui | 0 à 9 |
| `fov_x_degrees` | (Avancé) Champ de vision horizontal de la caméra source. Définit la distance focale utilisée pour déprojeter la carte de profondeur en 3D. 0 = récupération automatique à partir des points prédits. (par défaut : 0.0) | FLOAT | Oui | 0.0 à 170.0 (pas 0.1) |
| `batch_size` | Nombre d’images par appel d’inférence. Réduisez cette valeur en cas de saturation mémoire (OOM) sur une longue vidéo / un long ensemble d’images. (par défaut : 4) | INT | Oui | 1 à 64 |
| `force_projection` | (Avancé) Force la projection des points prédits. (par défaut : True) | BOOLEAN | Oui | True/False |
| `apply_mask` | (Avancé) Définit les pixels masqués (ciel / invalides) à inf dans les points et la profondeur afin que le maillage les élimine. Désactivez cette option pour conserver la géométrie prédite brute partout ; le masque est toujours renvoyé séparément. (par défaut : True) | BOOLEAN | Oui | True/False |
| `refine_steps` | (Avancé) MoGe-3 uniquement : passes d’affinage volumétrique sparse sur la profondeur prédite. Davantage de passes affinent les détails fins et les bords à un coût approximativement linéaire. 0 désactive l’affinage. Ignoré par MoGe-1 / MoGe-2. (par défaut : 3) | INT | Oui | 0 à 8 |

Remarque : lorsque l’image d’entrée `image` contient plus d’images que `batch_size`, le nœud les traite en plusieurs appels d’inférence et combine les résultats en une géométrie de sortie unique.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `moge_geometry` | Un dictionnaire contenant la géométrie estimée. Il inclut l’image d’origine (`image`) et peut contenir `points` (nuage de points 3D), `depth` (carte de profondeur), `intrinsics` (matrice des paramètres intrinsèques de la caméra), `mask` (masque identifiant les pixels valides) et `normal` (normales de surface). | MOGE_GEOMETRY |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/fr.md)

---
**Source fingerprint (SHA-256):** `10f3399d9b6bc4ff8a940c940f538a8ec8f38a15e7d65f162499c5ab264fad65`
