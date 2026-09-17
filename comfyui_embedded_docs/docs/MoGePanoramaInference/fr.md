# Inférence panorama MoGe

Ce nœud effectue une estimation de profondeur sur des images panoramiques équirectangulaires. Il divise le panorama en 12 vues en perspective, exécute le modèle d'estimation de profondeur MoGe sur chaque vue, puis fusionne les résultats par vue en une seule carte de profondeur couvrant l'ensemble du panorama. Les normales prédites et l'échelle métrique par vue sont ignorées, car les échelles par vue ne s'aligneraient pas à travers les coutures de chevauchement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `moge_model` | Le modèle MoGe à utiliser pour l'inférence. | MOGE_MODEL | Oui |  |
| `image` | Panorama équirectangulaire (tout format d'image). Le nœud accepte uniquement une seule image ; passer un lot d'images déclenche une erreur. Seuls les 3 premiers canaux de couleur (RVB) sont utilisés. | IMAGE | Oui |  |
| `resolution_level` | Niveau de détail par vue (0 = le plus rapide, 9 = le plus détaillé) (par défaut : 9). | INT | Oui | 0 à 9 |
| `split_resolution` | Résolution de chaque découpe en perspective (par défaut : 512). | INT | Oui | 256 à 1024 |
| `merge_resolution` | Résolution du côté long de la carte de distance équirectangulaire fusionnée (par défaut : 1920). | INT | Oui | 256 à 8192 |
| `batch_size` | Vues par lot d'inférence (12 découpes au total) (par défaut : 4). | INT | Oui | 1 à 12 |
| `refine_steps` | MoGe-3 uniquement : passes de raffinement volumétrique clairsemé sur la profondeur prédite. Davantage de passes affinent les détails fins et les contours à un coût approximativement linéaire. 0 désactive le raffinement. Ignoré par MoGe-1 / MoGe-2 (par défaut : 3). | INT | Oui | 0 à 8 |

**Remarques :**

- L'entrée doit être une image unique. Si `image` contient plus d'une image dans le lot, le nœud déclenche une erreur.
- `merge_resolution` est traité comme une taille maximale du côté long. Si le panorama est plus petit que cette valeur, la carte fusionnée est produite à la taille du panorama d'origine au lieu d'être agrandie. Le résultat fusionné est redimensionné à la résolution du panorama d'origine avant d'être renvoyé.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `moge_geometry` | Un dictionnaire contenant la géométrie estimée : `points` (nuage de points 3D), `depth` (carte de profondeur), `mask` (masque de zone valide) et `image` (l'image d'entrée). | MOGE_GEOMETRY |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/fr.md)

---
**Source fingerprint (SHA-256):** `7f21452d035b2fe9d30b0cd15ddad10916439492b1d682a8b28f1a79e375df58`
