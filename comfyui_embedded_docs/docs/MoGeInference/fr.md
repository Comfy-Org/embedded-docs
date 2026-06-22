# Inférence MoGe

Voici la traduction en français de la documentation du nœud ComfyUI **MoGeInference** :

## Aperçu

Exécute MoGe sur une seule image pour estimer la profondeur et la géométrie. Ce nœud traite une image d'entrée via le modèle MoGe pour générer un nuage de points 3D, une carte de profondeur, les paramètres intrinsèques de la caméra, un masque et des normales de surface.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `moge_model` | Le modèle MoGe à utiliser pour l'inférence. | MOGE_MODEL | Oui | N/A |
| `image` | L'image d'entrée pour l'estimation de la profondeur et de la géométrie. | IMAGE | Oui | N/A |
| `resolution_level` | Contrôle la résolution de traitement. 0 est le plus rapide, 9 offre le plus de détails. (par défaut : 9) | INT | Oui | 0 à 9 |
| `fov_x_degrees` | Champ de vision horizontal de la caméra source en degrés. Définit la distance focale utilisée pour projeter la carte de profondeur en 3D. Réglez sur 0.0 pour récupérer automatiquement le champ de vision à partir des points prédits. (par défaut : 0.0) | FLOAT | Oui | 0.0 à 170.0 |
| `batch_size` | Nombre d'images traitées par appel d'inférence. Réduisez cette valeur si vous manquez de mémoire lors du traitement de longues vidéos ou de grands ensembles d'images. (par défaut : 4) | INT | Oui | 1 à 64 |
| `force_projection` | (Avancé) Force la projection des points prédits. (par défaut : Vrai) | BOOLEAN | Oui | Vrai/Faux |
| `apply_mask` | Lorsqu'il est activé, définit les pixels masqués (ciel ou invalides) à l'infini dans les sorties de points et de profondeur. Cela aide les outils de maillage à ignorer ces zones. Désactivez pour conserver la géométrie brute prédite partout ; le masque est toujours renvoyé séparément. (par défaut : Vrai) | BOOLEAN | Oui | Vrai/Faux |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `moge_geometry` | Un dictionnaire contenant la géométrie estimée. Il inclut l'`image` d'origine et peut contenir `points` (nuage de points 3D), `depth` (carte de profondeur), `intrinsics` (matrice des paramètres intrinsèques de la caméra), `mask` (masque identifiant les pixels valides) et `normal` (normales de surface). | MOGE_GEOMETRY |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/fr.md)

---
**Source fingerprint (SHA-256):** `5213b280513850eeef2e22ae723ebb015789109435e28ddd79f91f9a4b4a1e79`
