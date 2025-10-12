> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/fr.md)

Le nœud SamplingPercentToSigma convertit une valeur de pourcentage d'échantillonnage en une valeur sigma correspondante en utilisant les paramètres d'échantillonnage du modèle. Il prend une valeur de pourcentage entre 0,0 et 1,0 et la mappe à la valeur sigma appropriée dans la planification de bruit du modèle, avec des options pour retourner soit le sigma calculé, soit les valeurs sigma maximum/minimum réelles aux limites.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle contenant les paramètres d'échantillonnage utilisés pour la conversion |
| `sampling_percent` | FLOAT | Oui | 0,0 à 1,0 | Le pourcentage d'échantillonnage à convertir en sigma (par défaut : 0,0) |
| `return_actual_sigma` | BOOLEAN | Oui | - | Retourne la valeur sigma réelle au lieu de la valeur utilisée pour les vérifications d'intervalle. Cela n'affecte que les résultats à 0,0 et 1,0. (par défaut : False) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `sigma_value` | FLOAT | La valeur sigma convertie correspondant au pourcentage d'échantillonnage d'entrée |