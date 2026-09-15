# Déplier les UV du maillage

Génère un atlas UV pour un maillage 3D. La surface du maillage est divisée en chartes, chaque charte est aplatie en deux dimensions, et les chartes aplaties sont empaquetées dans un atlas UV [0,1]. Les sommets situés sur les coutures de chartes sont dupliqués (une copie par charte, même position, coordonnées UV propres), de sorte que le maillage de sortie peut contenir plus de sommets que le maillage d'entrée, et le nombre de faces de sortie peut différer de celui de l'entrée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `maillage` | Le maillage d'entrée à déplier. Accepte un maillage unique ou un lot de maillages ; les lots sont traités un élément à la fois. | MESH | Oui | — |
| `segmenteur` | Algorithme de découpage en chartes à utiliser. `pec` : découpage rapide par effondrement d'arêtes parallèles sur GPU. `adaptive` : CPU, plus lent. (par défaut : "pec") | COMBO | Oui | "pec"<br>"adaptive" |
| `résolution` | Résolution cible de l'atlas pour la mise à l'échelle automatique de la densité de texels (0 = ajuster au contenu). (par défaut : 1024) | INT | Oui | 0 à 8192 (pas 256) |
| `marge` | Marge de texels entre les chartes. (par défaut : 1) | INT | Oui | 0 à 16 |
| `weld_distance` | Rayon de fusion des sommets coïncidents, exprimé comme une fraction de l'étendue du maillage (0 = automatique). Augmentez à ~0.001 si vous obtenez des chartes par triangle (entrée non soudée). (par défaut : 0.0) | FLOAT | Oui | 0.0 à 1.0 (pas 0.0001) |

Remarque : si le maillage d'entrée contient des sommets non soudés, le nœud peut avertir que l'adjacence des faces est faible et produire des chartes UV par face ; augmenter `weld_distance` fusionne les sommets coïncidents avant le dépliage. Les faces dégénérées (faces qui réutilisent le même index de sommet) sont supprimées pendant le traitement.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mesh` | Le maillage d'entrée avec un atlas UV généré dans la plage [0,1]. Les sommets de couture sont dupliqués, donc le nombre de sommets de sortie peut dépasser celui de l'entrée. Les couleurs de sommets et la texture du maillage d'entrée sont préservées. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnwrapMesh/fr.md)

---
**Source fingerprint (SHA-256):** `fcab6f0b621693d862ee74b5ec498498d2f1f247a66f478704377598a6b39388`
