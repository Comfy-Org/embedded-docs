# RemeshMesh

Remesh Mesh reconstruit un maillage avec une tessellation propre et uniforme en échantillonnant un champ de distance à bande étroite autour de la surface d’origine, puis en l’extrayant avec Dual Contouring. Cette opération normalise les topologies désordonnées, non-manifold ou auto-intersectantes, et est destinée à être exécutée avant Decimate Mesh pour atteindre un nombre exact de faces. Le traitement s’exécute sur le périphérique de calcul actif et le maillage de sortie reste soudé.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `maillage` | Le maillage d’entrée à remailler. | MESH | Oui | — |
| `résolution` | Résolution de la grille de voxels (densité de sortie). 256 ~ 100 000 faces, 512 ~ 1 million. Pour un nombre exact de faces, utilisez ensuite Decimate Mesh. (par défaut : 512) | INT | Oui | 32 - 2048 |
| `sign_mode` | Mode de distance signée utilisé pour l’extraction de surface. « udf » est robuste aux entrées désordonnées/non-manifold ; « sdf » produit une surface unique et propre avec récupération des arêtes vives par QEF (Quadratic Error Function), mais nécessite une orientation cohérente des faces. La sélection d’un mode révèle ses sous-options spécifiques. (par défaut : « udf ») | DYNAMIC_COMBO | Oui | "udf"<br>"sdf" |
| `bande` | Largeur de bande étroite en unités de voxel. En mode UDF, cette valeur décale également la surface. (avancé, par défaut : 1.0) | FLOAT | Oui | 0.5 - 4.0 |
| `project_back` | Interpole linéairement les sommets vers la surface d’origine (0 = DC pur, 1 = aligné). (avancé, par défaut : 0.0) | FLOAT | Oui | 0.0 - 1.0 |
| `fix_poles` | Fusionne les paires de sommets de valence 3 (artefact de jonction en T du DC). (avancé, par défaut : false) | BOOLEAN | Oui | true / false |
| `smooth_iters` | Itérations de lissage Taubin (0 = désactivé). 2 ou 3 nettoient les artefacts en escalier du DC ; des valeurs plus élevées lissent excessivement les arêtes QEF. (par défaut : 0) | INT | Oui | 0 - 20 |
| `drop_small_components` | Supprime les composantes dont le nombre de faces est inférieur à cette fraction de celui de la plus grande composante. 0 désactive. (avancé, par défaut : 0.01) | FLOAT | Oui | 0.0 - 0.5 |
| `precluster_max_verts` | Plafonne le nombre de sommets d’entrée avant les requêtes de champ ; les entrées supérieures à cette valeur sont d’abord décimées par regroupement jusqu’à cette cible. Évite les dépassements de mémoire (OOM) sur les maillages énormes. (avancé, par défaut : 20,000,000) | INT | Oui | 0 - 100,000,000 |

### Entrées du mode « udf »

Ces paramètres apparaissent lorsque `sign_mode` est défini sur `"udf"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `qef` | Placement des sommets duaux par QEF (Quadratic Error Function) pour des arêtes plus nettes. (par défaut : false) | BOOLEAN | Non | true / false |
| `drop_inverted_components` | Supprime les composantes fermées à normales entrantes (volume négatif) — la coque interne UDF. (par défaut : false) | BOOLEAN | Non | true / false |
| `drop_enclosed_components` | Supprime les composantes situées dans la boîte englobante de la plus grande qui échouent à un test de rayon point-dans-maillage. Désactivez cette option pour les pièces imbriquées légitimes. (par défaut : false) | BOOLEAN | Non | true / false |

### Entrées du mode « sdf »

Ces paramètres apparaissent lorsque `sign_mode` est défini sur `"sdf"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `qef` | Placement des sommets duaux par QEF (Quadratic Error Function) (récupère les arêtes vives) plutôt que centroïde d’intersection d’arête. (par défaut : true) | BOOLEAN | Non | true / false |
| `manifold` | Dual Contouring manifold : 1 à 4 sommets duaux par voxel pour les cas multi-feuillets. Plus lent. (par défaut : false) | BOOLEAN | Non | true / false |

Remarque : l’option `qef` a une valeur par défaut différente selon le mode sélectionné — false en mode « udf », true en mode « sdf ». Lorsque `precluster_max_verts` est supérieur à 0 et que le maillage d’entrée possède plus de sommets que cette valeur, le maillage est décimé par regroupement jusqu’à cette cible avant les requêtes de champ. Après le traitement, le nœud affiche la variation du nombre de faces entre l’entrée et la sortie (par exemple, « faces : 1.23M → 200K (-84 %) »).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mesh` | Le maillage remaillé avec une tessellation uniforme et une topologie soudée. Les couleurs de sommets sont conservées lorsqu’elles sont présentes sur l’entrée ; les UV, normales et tangentes ne sont pas transférés. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/fr.md)

---
**Source fingerprint (SHA-256):** `33b9603aad2aa8f4122dab75aa9d60caa0ab7ed81300461f3b773bb997251d99`
