# ColorTransfer

Le nœud ColorTransfer ajuste la palette de couleurs d'une image cible pour correspondre aux couleurs d'une image de référence. Il utilise différents algorithmes mathématiques pour analyser et transférer les caractéristiques chromatiques, telles que la luminosité, le contraste et la distribution des teintes, de la référence vers la cible. Cela est utile pour créer une cohérence visuelle entre plusieurs images ou appliquer un étalonnage chromatique spécifique.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image_target` | Image(s) à laquelle/auxquelles appliquer la transformation de couleurs. | IMAGE | Oui | - |
| `image_ref` | Image(s) de référence dont les couleurs doivent être reproduites. | IMAGE | Oui | - |
| `method` | L'algorithme de transfert de couleurs à utiliser. | COMBO | Oui | `"reinhard_lab"`<br>`"mkl_lab"`<br>`"histogram"` |
| `source_stats` | Détermine comment les statistiques de couleurs sont calculées à partir de la ou des images source (cible). | DYNAMICCOMBO | Oui | `"per_frame"`<br>`"uniform"`<br>`"target_frame"` |
| `strength` | L'intensité de l'effet de transfert de couleurs. Une valeur de 1.0 applique la transformation complète, tandis que 0.0 renvoie l'image originale. Par défaut : 1.0 | FLOAT | Oui | 0.0 à 10.0 |

**Détails des paramètres :**
*   **Options de `source_stats` :**
    *   **`per_frame`** : Chaque image d'un lot est mise en correspondance individuellement avec `image_ref`.
    *   **`uniform`** : Les statistiques de couleurs sont regroupées sur toutes les images sources pour créer une base de référence unique, qui est ensuite mise en correspondance avec `image_ref`.
    *   **`target_frame`** : Utilise une image choisie du lot cible comme base de référence pour calculer la transformation vers `image_ref`. Cette transformation est ensuite appliquée uniformément à toutes les images, ce qui préserve les différences de couleurs relatives entre elles. Lorsque cette option est sélectionnée, un paramètre supplémentaire `target_index` devient disponible.
*   **`target_index`** (apparaît lorsque `source_stats` est `"target_frame"`) : L'indice de l'image (à partir de 0) utilisé comme base de référence source pour calculer la transformation. Par défaut : 0. Doit être compris entre 0 et 10000.

**Contraintes :**
*   Si `strength` est réglé sur 0.0 ou si `image_ref` est `None`, le nœud renvoie l'`image_target` originale sans traitement.
*   Lorsque `source_stats` est réglé sur `"target_frame"`, `target_index` doit être un indice valide dans le lot de `image_target`. S'il dépasse le nombre d'images, la dernière image est utilisée.
*   Pour la méthode `histogram` avec `source_stats` réglé sur `"per_frame"`, si la taille du lot de `image_ref` est supérieure à 1, chaque image cible est mise en correspondance avec l'image de référence correspondante par indice. Si le lot de référence ne contient qu'une seule image, celle-ci est utilisée pour toutes les images cibles.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `image` | La ou les images résultantes après l'application du transfert de couleurs. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorTransfer/fr.md)

---
**Source fingerprint (SHA-256):** `93a8447def4d2263a8a859c0474de694e6567dc6d32377032c2ddae2420bb10c`
