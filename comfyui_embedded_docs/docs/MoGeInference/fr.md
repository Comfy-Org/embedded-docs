# Inférence MoGe

Exécutez MoGe sur une seule image pour estimer la profondeur et la géométrie. Ce nœud traite une image d’entrée via le modèle MoGe pour générer un nuage de points 3D, une carte de profondeur, les paramètres intrinsèques de la caméra, un masque et des normales de surface.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `moge_model` | Le modèle MoGe à utiliser pour l’inférence. | MOGE_MODEL | Oui | N/A |
| `image` | L’image d’entrée pour l’estimation de la profondeur et de la géométrie. Seuls les trois premiers canaux de couleur (RVB) sont utilisés. | IMAGE | Oui | N/A |
| `resolution_level` | Contrôle la résolution de traitement. 0 est le plus rapide, 9 offre le plus de détails. (défaut : 9) | INT | Oui | 0 à 9 |
| `fov_x_degrees` | (Avancé) Champ de vision horizontal de la caméra source en degrés. Définit la distance focale utilisée pour déprojeter la carte de profondeur en 3D. Réglez sur 0.0 pour retrouver automatiquement le champ de vision à partir des points prédits. (défaut : 0.0) | FLOAT | Oui | 0.0 à 170.0 |
| `batch_size` | Images par appel d’inférence. Réduisez cette valeur si vous manquez de mémoire sur une longue vidéo ou un ensemble d’images. (défaut : 4) | INT | Oui | 1 à 64 |
| `force_projection` | (Avancé) Force la projection des points prédits. (défaut : True) | BOOLEAN | Oui | True/False |
| `apply_mask` | (Avancé) Définit les pixels masqués (ciel ou invalides) à l’infini dans les sorties de points et de profondeur afin que les outils de maillage puissent les ignorer. Désactivez pour conserver la géométrie prédite brute partout ; le masque est toujours renvoyé séparément. (défaut : True) | BOOLEAN | Oui | True/False |

Remarque : lorsque l’`image` d’entrée contient plus de frames que `batch_size`, le nœud les traite en plusieurs appels d’inférence et combine les résultats en une seule géométrie de sortie.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `moge_geometry` | Un dictionnaire contenant la géométrie estimée. Il inclut l’`image` d’origine et peut contenir `points` (nuage de points 3D), `depth` (carte de profondeur), `intrinsics` (matrice des paramètres intrinsèques de la caméra), `mask` (masque identifiant les pixels valides) et `normal` (normales de surface). | MOGE_GEOMETRY |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/fr.md)

---
**Source fingerprint (SHA-256):** `59f6b8b1ab65147a47f5dc7ebee7b965a5ab37c6a0843a2c80d50c767ad98db4`
