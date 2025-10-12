> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreSca/fr.md)

Le nœud FreSca applique une mise à l'échelle dépendante de la fréquence au guidage pendant le processus d'échantillonnage. Il sépare le signal de guidage en composantes basse fréquence et haute fréquence en utilisant un filtrage de Fourier, puis applique différents facteurs d'échelle à chaque plage de fréquence avant de les recombiner. Cela permet un contrôle plus nuancé sur la façon dont le guidage affecte différents aspects de la sortie générée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle auquel appliquer la mise à l'échelle fréquentielle |
| `échelle_basse` | FLOAT | Non | 0-10 | Facteur d'échelle pour les composantes basse fréquence (par défaut : 1.0) |
| `échelle_haute` | FLOAT | Non | 0-10 | Facteur d'échelle pour les composantes haute fréquence (par défaut : 1.25) |
| `seuil_fréquence` | INT | Non | 1-10000 | Nombre d'indices de fréquence autour du centre à considérer comme basse fréquence (par défaut : 20) |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `modèle` | MODEL | Le modèle modifié avec une mise à l'échelle dépendante de la fréquence appliquée à sa fonction de guidage |