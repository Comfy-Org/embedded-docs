# DecimateMesh

DecimateMesh simplifie un maillage 3D pour atteindre un nombre de faces cible en utilisant la simplification par métrique d'erreur quadrique (QEM), et exécute le calcul sur l'appareil de calcul actif. Le mode de placement `"midpoint"` est le préréglage fidèle à cumesh offrant la meilleure qualité tout en préservant les fines caractéristiques telles que les cheveux, tandis que `"qem"` place les sommets à la position optimale QEM avec des contrôles facultatifs de ligne et d'arête de caractéristique. Le maillage de sortie reste soudé.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage 3D à simplifier. | MESH | Oui | - |
| `target_face_count` | Nombre maximal de faces cible. 0 désactive. (défaut : 200000) | INT | Oui | 0 à 50000000 |
| `placement_mode` | midpoint : fidèle à cumesh (recommandé). qem : placement optimal QEM. (défaut : `"midpoint"`) | DYNAMIC_COMBO | Oui | `"midpoint"`<br>`"qem"` |

### Entrées Midpoint

Le mode de placement `"midpoint"` n'expose pas de sous-paramètres supplémentaires ; il utilise le préréglage de placement midpoint par défaut.

### Entrées QEM

Les sous-paramètres suivants n'apparaissent dans l'interface que lorsque `placement_mode` est défini sur `"qem"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `line_quadric_weight` | Poids de quadrique de ligne par arête ; préserve les crêtes/vallées marquées. 0 = désactivé. (défaut : 0.0) | FLOAT | Non | 0.0 à 100.0 |
| `feature_edge_quadric_weight` | Poids quadrique supplémentaire sur les arêtes de caractéristique dièdres (plis). 0 = désactivé. (défaut : 0.0) | FLOAT | Non | 0.0 à 1000.0 |
| `feature_edge_min_dihedral_deg` | Angle dièdre minimal (en degrés) pour qu'une arête soit considérée comme une arête de caractéristique. (défaut : 30.0) | FLOAT | Non | 0.0 à 180.0 |
| `clamp_v_to_edge` | Projeter la position optimale QEM sur le segment d'arête contractée. (défaut : true) | BOOLEAN | Non | `true`<br>`false` |

Remarque : La décimation est ignorée lorsque `target_face_count` est 0 ou lorsque le maillage a déjà moins de faces que la cible. Le nœud affiche un résumé de la réduction de faces sur lui-même, par exemple `faces: 1.23M → 200K (-84%)`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mesh` | Le maillage simplifié avec le nombre de faces réduit ; la connectivité reste soudée. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DecimateMesh/fr.md)

---
**Source fingerprint (SHA-256):** `55336e5b52e27d940e5402ecd74fd0ac847a1c6acd35955eccf72aab8ed940f9`
