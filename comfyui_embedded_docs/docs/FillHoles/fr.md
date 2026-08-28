# FillHoles

Ce nœud comble les trous d'un maillage 3D en détectant les arêtes de bordure ouvertes et en créant de nouvelles faces pour les fermer. Il s'exécute sur le GPU, préserve la géométrie et les UV existants, et peut traiter des maillages simples, des listes de maillages ou des lots de maillages.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage 3D à traiter. Accepte un maillage unique, une liste de maillages ou un maillage par lots. | MESH | Oui | - |
| `max_perimeter` | Périmètre maximal des trous à combler. 0 désactive. (défaut : 0.03) | FLOAT | Oui | 0.0 à aucune limite supérieure |
| `weld_epsilon_rel` | Tolérance de pré-soudage (fraction de la diagonale de la boîte englobante) ; la détection des bordures nécessite des sommets soudés. 0 ignore. (défaut : 1e-5) | FLOAT | Oui | 0.0 à aucune limite supérieure |
| `max_vertices` | Limite du nombre de sommets de bordure par cycle ; l'éventail de centroïde ne fonctionne que pour les petits trous quasi plans. Conservez ≤16. (défaut : 16) | INT | Oui | 3 à 1024 |
| `fill_chains` | Comble également les chaînes ouvertes (pas seulement les cycles). Bruité ; DÉSACTIVÉ pour correspondre à cumesh. (défaut : False) | BOOLEAN | Oui | True ou False |

Remarque : Lorsque `weld_epsilon_rel` est supérieur à 0, le nœud pré-soude les sommets en double avant de détecter les trous. La tolérance de soudage démarre à la fraction donnée de la diagonale de la boîte englobante et augmente automatiquement en doublant jusqu'à ce que le maillage soit considéré comme soudé ou que la tolérance atteigne un plafond de 1e-2. Les trous comportant plus de 8 sommets de bordure utilisent un remplissage en éventail de centroïde (insertion d'un nouveau sommet central), tandis que les trous plus petits utilisent un remplissage en éventail de sommets qui réutilise un sommet de bordure existant.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mesh` | Le maillage avec les trous comblés, correspondant au format du lot d'entrée. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FillHoles/fr.md)

---
**Source fingerprint (SHA-256):** `c0fd7f0c2d6eea098efb1dcfd80eaa52997e185b9c442b483f75318eea082196`
