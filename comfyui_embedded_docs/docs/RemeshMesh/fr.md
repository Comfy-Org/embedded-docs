# RemeshMesh

### Remesh Mesh

Remesh Mesh reconstruit un maillage avec une tessellation propre et uniforme en échantillonnant un champ de distance à bande étroite autour de la surface d'origine et en l'extrayant par Dual Contouring. Cela normalise une topologie désordonnée, non-manifold ou auto-intersectante, et doit être exécuté avant Decimate Mesh pour atteindre un nombre exact de faces. Le traitement s'exécute sur le périphérique de calcul actif et le maillage de sortie reste soudé.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Le maillage d'entrée à remailler. | MESH | Oui | — |
| `resolution` | Résolution de la grille de voxels (densité de sortie). 256 ~ 100k faces, 512 ~ 1M. Pour un nombre exact de faces, suivez avec Decimate Mesh. (défaut : 512) | INT | Oui | 32 - 2048 |
| `sign_mode` | Mode de distance signée utilisé pour l'extraction de surface. « udf » est robuste aux entrées désordonnées/non-manifold ; « sdf » produit une surface unique propre avec récupération des caractéristiques nettes par QEF (fonction d'erreur quadratique), mais nécessite un enroulement cohérent. La sélection d'un mode révèle ses sous-options spécifiques. (défaut : « udf ») | DYNAMIC_COMBO | Oui | « udf »<br>« sdf » |
| `band` | Largeur de bande étroite en unités de voxels. En mode UDF, décale également la surface. (avancé, défaut : 1.0) | FLOAT | Oui | 0.5 - 4.0 |
| `project_back` | Interpoler linéairement les sommets vers la surface d'origine (0 = DC pur, 1 = aligné sur la surface). (avancé, défaut : 0.0) | FLOAT | Oui | 0.0 - 1.0 |
| `fix_poles` | Réduire les paires de sommets de valence 3 (artefact de jonction en T du DC). (avancé, défaut : false) | BOOLEAN | Oui | true / false |
| `smooth_iters` | Itérations de lissage Taubin (0 = désactivé). 2-3 nettoie les artefacts en escalier du DC ; des valeurs plus élevées sur-lissent les arêtes QEF. (défaut : 0) | INT | Oui | 0 - 20 |
| `drop_small_components` | Supprimer les composants dont le nombre de faces est inférieur à cette fraction de celui du plus grand. 0 désactive. (avancé, défaut : 0.01) | FLOAT | Oui | 0.0 - 0.5 |
| `precluster_max_verts` | Plafonner le nombre de sommets d'entrée avant les requêtes de champ ; les entrées supérieures sont d'abord décimées par regroupement jusqu'à cette valeur. Évite les dépassements de mémoire (OOM) sur les grands maillages. (avancé, défaut : 20 000 000) | INT | Oui | 0 - 100 000 000 |

### Entrées du mode « udf »

Ces paramètres apparaissent lorsque `sign_mode` est défini sur `"udf"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `qef` | Placement des doubles sommets par QEF (fonction d'erreur quadratique) pour des arêtes plus nettes. (défaut : false) | BOOLEAN | Non | true / false |
| `drop_inverted_components` | Supprimer les composants fermés à normales vers l'intérieur (volume négatif) — la coque interne de l'UDF. (défaut : false) | BOOLEAN | Non | true / false |
| `drop_enclosed_components` | Supprimer les composants à l'intérieur de la boîte englobante du plus grand qui échouent à un raycast point-dans-maillage. Désactiver pour les pièces imbriquées légitimes. (défaut : false) | BOOLEAN | Non | true / false |

### Entrées du mode « sdf »

Ces paramètres apparaissent lorsque `sign_mode` est défini sur `"sdf"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `qef` | Placement des doubles sommets par QEF (fonction d'erreur quadratique) (récupère les caractéristiques nettes) par rapport au centroïde de croisement d'arête. (défaut : true) | BOOLEAN | Non | true / false |
| `manifold` | Dual Contouring manifold : 1 à 4 doubles sommets/voxel pour les cas multi-feuilles. Plus lent. (défaut : false) | BOOLEAN | Non | true / false |

Remarque : l'option `qef` a une valeur par défaut différente selon le mode sélectionné — false en mode « udf », true en mode « sdf ». Lorsque `precluster_max_verts` est supérieur à 0 et que le maillage d'entrée a plus de sommets que cette valeur, le maillage est décimé par regroupement jusqu'à cette cible avant les requêtes de champ. Après le traitement, le nœud affiche la variation du nombre de faces entre l'entrée et la sortie sur le nœud (par exemple, « faces : 1.23M → 200K (-84%) »).

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `mesh` | Le maillage remaillé avec une tessellation uniforme et une topologie soudée. Les couleurs de sommets sont préservées si elles sont présentes sur l'entrée ; les UV, normales et tangentes ne sont pas reportés. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/fr.md)

---
**Source fingerprint (SHA-256):** `33b9603aad2aa8f4122dab75aa9d60caa0ab7ed81300461f3b773bb997251d99`
