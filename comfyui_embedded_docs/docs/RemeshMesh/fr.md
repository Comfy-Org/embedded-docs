# Re-maillage du maillage (DC à bande étroite)

Remesh Mesh reconstruit un maillage avec une tessellation propre et uniforme en échantillonnant un champ de distance à bande étroite autour de la surface d'origine et en l'extrayant avec Dual Contouring. Cela normalise une topologie désordonnée, non-manifold ou auto-intersectée, et est destiné à être exécuté avant Decimate Mesh pour atteindre un nombre exact de faces. Le traitement s'exécute sur le périphérique de calcul actif et le maillage de sortie reste soudé.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `maillage` | Le maillage d'entrée à remailler. | MESH | Oui | — |
| `résolution` | Résolution de la grille de voxels (densité de sortie). 256 ~ 100k faces, 512 ~ 1M. Pour un nombre exact de faces, faites suivre avec Decimate Mesh. (par défaut : 512) | INT | Oui | 32 - 2048 |
| `sign_mode` | Mode d'extraction de surface. « udf » est robuste aux entrées désordonnées/non-manifold ; « sdf » produit une surface unique propre avec récupération des arêtes vives par QEF (Quadratic Error Function), mais nécessite un enroulement cohérent. « solid » construit un solide étanche unique à partir d'une entrée désordonnée : une coupe de graphe globale intérieur/extérieur (CelloCut) supprime les doubles enveloppes et ferme les petits trous. Plus lent. La sélection d'un mode révèle ses sous-options spécifiques. (par défaut : « udf ») | DYNAMIC_COMBO | Oui | "udf"<br>"sdf"<br>"solid" |
| `bande` | Largeur de la bande étroite en unités de voxel. En mode UDF, décale également la surface. En mode solid, il s'agit du rayon de fermeture : les plis sont adoucis et les trous comblés à cette taille, la surface se situe à un demi-voxel vers l'extérieur. (avancé, par défaut : 1.0) | FLOAT | Oui | 0.5 - 4.0 |
| `project_back` | Interpole linéairement les sommets vers la surface d'origine (0 = DC pur, 1 = accroché). (avancé, par défaut : 0.0) | FLOAT | Oui | 0.0 - 1.0 |
| `fix_poles` | Fusionne les paires de sommets de valence 3 (artefact de jonction en T du DC). (avancé, par défaut : false) | BOOLEAN | Oui | true / false |
| `smooth_iters` | Itérations de lissage de Taubin (0 = désactivé). 2-3 nettoie les artefacts en escalier du DC ; une valeur plus élevée lisse excessivement les arêtes QEF. (par défaut : 0) | INT | Oui | 0 - 20 |
| `drop_small_components` | Supprime les composants dont le nombre de faces est inférieur à cette fraction de celui du plus grand. 0 désactive. (avancé, par défaut : 0.01) | FLOAT | Oui | 0.0 - 0.5 |
| `precluster_max_verts` | Plafonne le nombre de sommets d'entrée avant les requêtes de champ ; les entrées au-dessus de cette valeur sont d'abord décimées par cluster à ce niveau. Évite les OOM sur les maillages volumineux. (avancé, par défaut : 20,000,000) | INT | Oui | 0 - 100,000,000 |

### Entrées du mode « udf »

Ces paramètres apparaissent lorsque `sign_mode` est défini sur `"udf"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `qef` | Placement des sommets par QEF (Quadratic Error Function) : arêtes vives sur une entrée à surfaces dures, plis irréguliers sur une entrée organique. (avancé, par défaut : false) | BOOLEAN | Non | true / false |
| `drop_inverted_components` | Supprime les composants fermés à normale entrante (volume négatif) — la coque interne de l'UDF. (avancé, par défaut : false) | BOOLEAN | Non | true / false |
| `drop_enclosed_components` | Supprime les composants à l'intérieur de la bbox du plus grand qui échouent à un lancer de rayon point-dans-maillage. Désactivez pour des parties imbriquées légitimes. (avancé, par défaut : false) | BOOLEAN | Non | true / false |

### Entrées du mode « sdf »

Ces paramètres apparaissent lorsque `sign_mode` est défini sur `"sdf"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `qef` | Placement des sommets doubles par QEF (Quadratic Error Function) (récupère les arêtes vives) par rapport au centroïde de croisement d'arêtes. (par défaut : true) | BOOLEAN | Non | true / false |
| `manifold` | Dual Contouring manifold : 1-4 sommets doubles/voxel pour les cas multi-feuillets. Plus lent. (par défaut : false) | BOOLEAN | Non | true / false |

### Entrées du mode « solid »

Ces paramètres apparaissent lorsque `sign_mode` est défini sur `"solid"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `fill` | Coût de la fermeture d'une ouverture par rapport au suivi de la surface. Plus la valeur est basse, plus les ouvertures fermées sont grandes (0 pose un couvercle sur une tasse) ; plus elle est haute, plus seuls les petits trous et fissures sont fermés. (par défaut : 20.0) | FLOAT | Non | 0.0 - 1000.0 |
| `qef` | Placement des sommets par QEF (Quadratic Error Function) : arêtes vives sur une entrée à surfaces dures, plis irréguliers sur une entrée organique. (avancé, par défaut : false) | BOOLEAN | Non | true / false |

Remarque : L'option `qef` a une valeur par défaut différente selon le mode sélectionné — false en mode « udf » et « solid », true en mode « sdf ». Lorsque `precluster_max_verts` est supérieur à 0 et que le maillage d'entrée a plus de sommets que cette valeur, le maillage est décimé par cluster jusqu'à cette cible avant les requêtes de champ. Après le traitement, le nœud affiche la variation du nombre de faces entre l'entrée et la sortie sur le nœud (par exemple, « faces: 1.23M → 200K (-84%) »).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mesh` | Le maillage remaillé avec une tessellation uniforme et une topologie soudée. Les couleurs des sommets sont préservées lorsqu'elles sont présentes sur l'entrée ; les coordonnées UV, les normales et les tangentes ne sont pas transférées. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/fr.md)

---
**Source fingerprint (SHA-256):** `d2869c681e0485f5946a53f0582188ded2183ecd741ea1ff6a591932b18b5abe`
