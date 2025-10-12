> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/fr.md)

Le nœud ModelSamplingLTXV applique des paramètres d'échantillonnage avancés à un modèle en fonction du nombre de tokens. Il calcule une valeur de décalage en utilisant une interpolation linéaire entre les valeurs de décalage de base et maximale, le calcul dépendant du nombre de tokens dans le latent d'entrée. Le nœud crée ensuite une configuration d'échantillonnage de modèle spécialisée et l'applique au modèle d'entrée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle d'entrée auquel appliquer les paramètres d'échantillonnage |
| `décalage_max` | FLOAT | Non | 0.0 à 100.0 | La valeur de décalage maximale utilisée dans le calcul (par défaut : 2.05) |
| `décalage_base` | FLOAT | Non | 0.0 à 100.0 | La valeur de décalage de base utilisée dans le calcul (par défaut : 0.95) |
| `latent` | LATENT | Non | - | Entrée latente optionnelle utilisée pour déterminer le nombre de tokens pour le calcul du décalage |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `modèle` | MODEL | Le modèle modifié avec les paramètres d'échantillonnage appliqués |