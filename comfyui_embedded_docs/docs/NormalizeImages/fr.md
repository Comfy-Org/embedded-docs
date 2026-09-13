# Normaliser les images

Ce nœud normalise les couleurs d'une image d'entrée en ajustant ses valeurs de pixels selon une moyenne et un écart-type spécifiés. La moyenne est soustraite de chaque pixel, puis le résultat est divisé par l'écart-type, ce qui est une étape courante pour standardiser les données d'image avant d'autres traitements.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `image` | Image d'entrée à normaliser. | IMAGE | Oui | - |
| `mean` | Valeur moyenne pour la normalisation (par défaut : 0.5). | FLOAT | Non | 0.0 - 1.0 |
| `std` | Écart-type pour la normalisation (par défaut : 0.5). | FLOAT | Non | 0.001 - 1.0 |

Les paramètres `mean` et `std` contrôlent la normalisation appliquée à l'image d'entrée. La valeur par défaut des deux paramètres est 0.5.

Remarque : Si l'image d'entrée possède un canal alpha (transparence), ce canal n'est pas normalisé. Il est copié tel quel vers la sortie, car le canal alpha stocke la transparence plutôt que la couleur.

Remarque : Le nœud fonctionne avec n'importe quelle taille de lot, donc plusieurs images peuvent être traitées en même temps.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `image` | Image résultante après application du processus de normalisation. Les valeurs des pixels sont ajustées à l'aide de la moyenne et de l'écart-type spécifiés, et le canal alpha (s'il est présent) est préservé. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/fr.md)

---
**Source fingerprint (SHA-256):** `30c0587265754842ff7d1e5f339fc934b58d59bb3ba18716c2a1f9679f2d561d`
