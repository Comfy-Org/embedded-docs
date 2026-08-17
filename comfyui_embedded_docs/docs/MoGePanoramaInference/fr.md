# Inférence panorama MoGe

Ce nœud effectue l'estimation de profondeur sur des images panoramiques équirectangulaires. Il fonctionne en divisant le panorama en 12 vues en perspective, en exécutant le modèle d'estimation de profondeur MoGe sur chaque vue, puis en fusionnant les résultats en une seule carte de profondeur complète pour le panorama d'origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `moge_model` | Le modèle MoGe à utiliser pour l'inférence. | MOGE_MODEL | Oui |  |
| `image` | Panorama équirectangulaire (format quelconque). Accepte une seule image. | IMAGE | Oui |  |
| `resolution_level` | Niveau de détail par vue (0 = plus rapide, 9 = plus détaillé). Par défaut : 9. | INT | Oui | 0 à 9 |
| `split_resolution` | Résolution de chaque division en perspective. Par défaut : 512. | INT | Oui | 256 à 1024 |
| `merge_resolution` | Résolution du côté long de la carte de distance équirectangulaire fusionnée. Par défaut : 1920. | INT | Oui | 256 à 8192 |
| `batch_size` | Vues par lot d'inférence (12 divisions au total). Par défaut : 4. | INT | Oui | 1 à 12 |

Remarque : Ce nœud accepte une seule image. Le passage d'un lot d'images provoque une erreur. Le panorama est toujours divisé en 12 vues en perspective ; `batch_size` contrôle uniquement le nombre de ces vues traitées par lot d'inférence.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `moge_geometry` | Un dictionnaire contenant la géométrie estimée : `points` (nuage de points 3D), `depth` (carte de profondeur), `mask` (masque de zone valide) et `image` (l'image d'entrée). | MOGE_GEOMETRY |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/fr.md)

---
**Source fingerprint (SHA-256):** `d35b6d42a5bb17c184bc56fe3867d3a183017084dc81649c0663a9fba2362770`
