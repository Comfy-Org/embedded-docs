# Décimer le maillage

Simplifie un maillage 3D à un nombre cible de faces en utilisant la simplification QEM (quadric error metric), en exécutant le calcul sur le périphérique de calcul actif. Le mode de placement `"midpoint"` est le préréglage fidèle à cumesh qui offre la meilleure qualité tout en préservant les caractéristiques fines telles que les cheveux, tandis que `"qem"` place les sommets à la position optimale QEM avec des contrôles optionnels des lignes et des arêtes caractéristiques. Le maillage de sortie reste soudé.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage 3D à simplifier. | MESH | Oui | - |
| `target_face_count` | Nombre maximal cible de faces. 0 désactive. (par défaut : 200000) | INT | Oui | 0 à 50000000 |
| `placement_mode` | midpoint : fidèle à cumesh (recommandé). qem : placement optimal QEM. (par défaut : `"midpoint"`) | DYNAMIC_COMBO | Oui | `"midpoint"`<br>`"qem"` |

### Entrées Midpoint

Le mode de placement `"midpoint"` n'expose aucun sous-paramètre supplémentaire ; il utilise le préréglage de placement midpoint par défaut.

### Entrées QEM

Les sous-paramètres suivants n'apparaissent dans l'interface que lorsque `placement_mode` est défini sur `"qem"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `line_quadric_weight` | Poids de quadrique de ligne par arête ; préserve les crêtes/vallées nettes. 0 = désactivé. (par défaut : 0.0) | FLOAT | Non | 0.0 à 100.0 |
| `feature_edge_quadric_weight` | Poids de quadrique supplémentaire sur les arêtes caractéristiques dièdres (plis). 0 = désactivé. (par défaut : 0.0) | FLOAT | Non | 0.0 à 1000.0 |
| `feature_edge_min_dihedral_deg` | Angle dièdre minimal (en degrés) pour qu'une arête soit considérée comme une arête caractéristique. (par défaut : 30.0) | FLOAT | Non | 0.0 à 180.0 |
| `clamp_v_to_edge` | Projette la position optimale QEM sur le segment d'arête contractée. (par défaut : true) | BOOLEAN | Non | `true`<br>`false` |

Remarque : La décimation est ignorée lorsque `target_face_count` vaut 0 ou lorsque le maillage ne contient déjà pas plus de faces que la cible. Le nœud affiche un résumé de la réduction de faces sur lui-même, par exemple `faces: 1.23M → 200K (-84%)`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mesh` | Le maillage simplifié avec le nombre de faces réduit ; la connectivité reste soudée. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DecimateMesh/fr.md)

---
**Source fingerprint (SHA-256):** `55336e5b52e27d940e5402ecd74fd0ac847a1c6acd35955eccf72aab8ed940f9`
