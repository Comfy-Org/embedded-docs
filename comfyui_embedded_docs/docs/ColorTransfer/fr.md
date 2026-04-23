> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorTransfer/fr.md)

Le nœud ColorTransfer ajuste la palette de couleurs d'une image cible pour correspondre aux couleurs d'une image de référence. Il utilise différents algorithmes mathématiques pour analyser et transférer les caractéristiques de couleur, telles que la luminosité, le contraste et la distribution des teintes, de la référence vers la cible. Cela est utile pour créer une cohérence visuelle entre plusieurs images ou pour appliquer une étalonnage couleur spécifique.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image_target` | IMAGE | Oui | - | Image(s) à laquelle/auxquelles appliquer la transformation de couleur. |
| `image_ref` | IMAGE | Non | - | Image(s) de référence pour l'ajustement des couleurs. Si non fournie, le traitement est ignoré et l'image cible est retournée inchangée. |
| `method` | COMBO | Oui | `"reinhard_lab"`<br>`"mkl_lab"`<br>`"histogram"` | L'algorithme de transfert de couleur à utiliser. |
| `source_stats` | DYNAMICCOMBO | Oui | `"per_frame"`<br>`"uniform"`<br>`"target_frame"` | Détermine comment les statistiques de couleur sont calculées à partir de(s) image(s) source (cible). |
| `strength` | FLOAT | Oui | 0.0 à 10.0 | L'intensité de l'effet de transfert de couleur. Une valeur de 1.0 applique la transformation complète, tandis que 0.0 retourne l'image originale. Par défaut : 1.0 |

**Détails des paramètres :**
*   **Options de `source_stats` :**
    *   **`per_frame`** : Chaque image d'un lot est ajustée individuellement à l'`image_ref`.
    *   **`uniform`** : Les statistiques de couleur sont regroupées sur toutes les images sources pour créer une base de référence unique, qui est ensuite ajustée à l'`image_ref`.
    *   **`target_frame`** : Utilise une image choisie du lot cible comme base de référence pour calculer la transformation vers l'`image_ref`. Cette transformation est ensuite appliquée uniformément à toutes les images, ce qui préserve les différences de couleur relatives entre elles. Lorsque cette option est sélectionnée, un paramètre supplémentaire `target_index` devient disponible.
*   **`target_index`** (apparaît lorsque `source_stats` est `"target_frame"`) : L'index de l'image (commençant à 0) utilisé comme base de référence source pour calculer la transformation. Par défaut : 0. Doit être compris entre 0 et 10000.

**Contraintes :**
*   Si `image_ref` n'est pas fournie ou si `strength` est réglé sur 0.0, le nœud retourne l'`image_target` originale sans traitement.
*   Lorsque `source_stats` est réglé sur `"target_frame"`, le `target_index` doit être un index valide dans le lot d'`image_target`. S'il dépasse le nombre d'images, la dernière image est utilisée.
*   Pour la méthode `histogram` avec `source_stats` réglé sur `"per_frame"`, si la taille du lot d'`image_ref` est supérieure à 1, chaque image cible est ajustée à l'image de référence correspondante par index. Si le lot de référence n'a qu'une seule image, elle est utilisée pour toutes les images cibles.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'(les) image(s) résultante(s) après l'application du transfert de couleur. |