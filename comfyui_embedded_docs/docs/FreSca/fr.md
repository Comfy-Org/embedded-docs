Le nœud FreSca applique une mise à l'échelle dépendante de la fréquence au guidage pendant le processus d'échantillonnage. Il sépare le signal de guidage en composantes basse fréquence et haute fréquence à l'aide d'un filtrage de Fourier, puis applique différents facteurs d'échelle à chaque plage de fréquence avant de les recomposer. Cela permet un contrôle plus nuancé de la manière dont le guidage affecte les différents aspects de la sortie générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel appliquer la mise à l'échelle de fréquence | MODEL | Oui | - |
| `échelle_basse` | Facteur d'échelle pour les composantes basse fréquence (par défaut : 1.0) | FLOAT | Non | 0 - 10 |
| `échelle_haute` | Facteur d'échelle pour les composantes haute fréquence (par défaut : 1.25) | FLOAT | Non | 0 - 10 |
| `seuil_fréquence` | Nombre d'indices de fréquence autour du centre à considérer comme basse fréquence (par défaut : 20) | INT | Non | 1 - 10000 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle modifié avec une mise à l'échelle dépendante de la fréquence appliquée à sa fonction de guidage | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreSca/fr.md)

---
**Source fingerprint (SHA-256):** `254a28847e082739f80c9637d9657ef618d40db1862b6856c1cda22436438ded`
