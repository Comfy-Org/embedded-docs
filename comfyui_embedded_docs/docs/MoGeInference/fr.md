# Inférence MoGe

Exécutez MoGe sur une image unique pour estimer la profondeur et la géométrie. Ce nœud traite une image d'entrée via le modèle MoGe pour générer un nuage de points 3D, une carte de profondeur, les paramètres intrinsèques de la caméra, un masque et les normales de surface.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `moge_model` | Le modèle MoGe à utiliser pour l'inférence. | MOGE_MODEL | Oui | N/A |
| `image` | L'image d'entrée pour l'estimation de la profondeur et de la géométrie. Seuls les canaux RVB sont utilisés ; le canal alpha est ignoré. | IMAGE | Oui | N/A |
| `resolution_level` | Contrôle la résolution de traitement. 0 est le plus rapide, 9 fournit le plus de détails. (défaut : 9) | INT | Oui | 0 à 9 |
| `fov_x_degrees` | (Avancé) Champ de vision horizontal de la caméra source en degrés. Définit la distance focale utilisée pour déprojeter la carte de profondeur en 3D. Réglez sur 0.0 pour récupérer automatiquement le champ de vision à partir des points prédits. (défaut : 0.0) | FLOAT | Oui | 0.0 to 170.0 |
| `batch_size` | Nombre d'images traitées par appel d'inférence. Réduisez cette valeur en cas de manque de mémoire lors du traitement de vidéos longues ou de grands ensembles d'images. (défaut : 4) | INT | Oui | 1 à 64 |
| `force_projection` | (Avancé) Force la projection des points prédits. (défaut : True) | BOOLEAN | Oui | True/False |
| `apply_mask` | (Avancé) Lorsque activé, définit les pixels masqués (ciel ou invalides) sur l'infini dans les sorties de points et de profondeur. Cela aide les outils de maillage à ignorer ces zones. Désactivez pour conserver la géométrie brute prédite partout ; le masque est toujours retourné séparément. (défaut : True) | BOOLEAN | Oui | True/False |

Remarque : L'entrée `image` peut contenir plusieurs images. Le nœud les traite par groupes de `batch_size` et combine les résultats en une seule sortie.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `moge_geometry` | Un dictionnaire contenant la géométrie estimée. Il inclut toujours l'`image` d'entrée (uniquement les canaux RVB) et peut contenir `points` (nuage de points 3D), `depth` (carte de profondeur), `intrinsics` (matrice des paramètres intrinsèques de la caméra), `mask` (masque identifiant les pixels valides) et `normal` (normales de surface). | MOGE_GEOMETRY |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/fr.md)

---
**Source fingerprint (SHA-256):** `59f6b8b1ab65147a47f5dc7ebee7b965a5ab37c6a0843a2c80d50c767ad98db4`
