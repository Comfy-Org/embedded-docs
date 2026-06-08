## Aperçu

Ce nœud effectue une estimation de profondeur sur des images panoramiques équirectangulaires. Il fonctionne en divisant le panorama en 12 vues en perspective, en exécutant le modèle d'estimation de profondeur MoGe sur chaque vue, puis en fusionnant les résultats en une seule carte de profondeur complète pour le panorama d'origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `moge_model` | Le modèle MoGe à utiliser pour l'inférence. | MOGE_MODEL | Oui |  |
| `image` | Image panoramique équirectangulaire (tout rapport hauteur/largeur). | IMAGE | Oui |  |
| `resolution_level` | Niveau de détail par vue. Des valeurs plus élevées produisent des cartes de profondeur plus détaillées (par défaut : 9). | INT | Oui | 0 à 9 |
| `split_resolution` | Résolution de chaque vue en perspective après division du panorama (par défaut : 512). | INT | Oui | 256 à 1024 |
| `merge_resolution` | Résolution du côté long de la carte de profondeur équirectangulaire finale fusionnée (par défaut : 1920). | INT | Oui | 256 à 8192 |
| `batch_size` | Nombre de vues en perspective à traiter dans chaque lot d'inférence. Le nombre total de vues est de 12 (par défaut : 4). | INT | Oui | 1 à 12 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `moge_geometry` | Un dictionnaire contenant la géométrie estimée : `points` (nuage de points 3D), `depth` (carte de profondeur), `mask` (masque de zone valide) et `image` (l'image d'entrée). | MOGE_GEOMETRY |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/fr.md)

---
**Source fingerprint (SHA-256):** `3a701e3679bc35cd5fddc54868ac9c4bc9b4e23a5b97bbf61e46b7309e43600b`
