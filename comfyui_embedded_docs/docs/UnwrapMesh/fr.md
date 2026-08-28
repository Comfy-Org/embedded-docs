# UnwrapMesh

Génère un atlas UV pour un maillage 3D. La surface est découpée en îlots (charts), chaque îlot est aplati en deux dimensions, et les résultats sont regroupés dans un atlas UV [0,1]. Les sommets sur les coutures des îlots sont dupliqués, le maillage de sortie peut donc contenir plus de sommets que le maillage d'entrée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `maillage` | Le maillage d'entrée à déplier. Accepte un maillage unique ou un lot de maillages. | MESH | Oui | — |
| `segmenteur` | Algorithme de découpage en îlots à utiliser. pec : découpage rapide par effondrement d'arêtes parallèles sur GPU. adaptive : CPU, plus lent. (défaut : "pec") | COMBO | Oui | "pec"<br>"adaptive" |
| `résolution` | Résolution cible de l'atlas pour l'auto-échelle de la densité de texels (0 = ajuster au contenu). (défaut : 1024) | INT | Oui | 0 à 8192 (pas de 256) |
| `marge` | Remplissage (padding) en texels entre les îlots. (défaut : 1) | INT | Oui | 0 à 16 |
| `weld_distance` | Rayon de fusion des sommets coïncidents en fraction de l'étendue du maillage (0 = auto). Augmentez à ~0.001 si vous obtenez des îlots par triangle (entrée non soudée). (défaut : 0.0) | FLOAT | Oui | 0.0 à 1.0 (pas de 0.0001) |

Remarque : si le maillage d'entrée contient des sommets non soudés (triangle soup), le nœud peut avertir que l'adjacence des faces est faible et produire des îlots UV par face ; augmenter `weld_distance` fusionne les sommets coïncidents avant le dépliage.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `maillage` | Le maillage d'entrée avec un atlas UV généré dans [0,1]. Les sommets de couture sont dupliqués, le nombre de sommets de sortie peut donc dépasser celui de l'entrée. Les couleurs de sommets et la texture du maillage d'entrée sont conservées. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnwrapMesh/fr.md)

---
**Source fingerprint (SHA-256):** `cf0dbbe43df507921e6e9795b42d5cb5691ccc2ae98a8bb17e02e3928ea0b815`
