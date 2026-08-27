# Inférence panorama MoGe

## Aperçu

Ce nœud effectue une estimation de profondeur sur des images panoramiques équirectangulaires. Il divise le panorama en 12 vues en perspective, exécute le modèle d'estimation de profondeur MoGe sur chaque vue, puis fusionne les résultats de chaque vue en une seule carte de profondeur couvrant l'ensemble du panorama.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `moge_model` | Le modèle MoGe à utiliser pour l'inférence. | MOGE_MODEL | Oui |  |
| `image` | Panorama équirectangulaire (format quelconque). Le nœud n'accepte qu'une seule image ; passer un lot d'images génère une erreur. Seuls les 3 premiers canaux de couleur (RVB) sont utilisés. | IMAGE | Oui |  |
| `resolution_level` | Niveau de détail par vue (0 = plus rapide, 9 = le plus détaillé) (par défaut : 9). | INT | Oui | 0 à 9 |
| `split_resolution` | Résolution de chaque division en perspective (par défaut : 512). | INT | Oui | 256 à 1024 |
| `merge_resolution` | Résolution du côté long de la carte de distance équirectangulaire fusionnée (par défaut : 1920). | INT | Oui | 256 à 8192 |
| `batch_size` | Vues par lot d'inférence (12 divisions au total) (par défaut : 4). | INT | Oui | 1 à 12 |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `moge_geometry` | Un dictionnaire contenant la géométrie estimée : `points` (nuage de points 3D), `depth` (carte de profondeur), `mask` (masque de zone valide) et `image` (l'image d'entrée). | MOGE_GEOMETRY |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/fr.md)

---
**Source fingerprint (SHA-256):** `d35b6d42a5bb17c184bc56fe3867d3a183017084dc81649c0663a9fba2362770`
