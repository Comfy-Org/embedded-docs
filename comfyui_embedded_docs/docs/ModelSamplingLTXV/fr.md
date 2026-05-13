> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/fr.md)

Le nœud ModelSamplingLTXV applique des paramètres d'échantillonnage avancés à un modèle en fonction du nombre de jetons. Il calcule une valeur de décalage à l'aide d'une interpolation linéaire entre les valeurs de décalage de base et maximale, le calcul dépendant du nombre de jetons dans l'entrée latente. Le nœud crée ensuite une configuration d'échantillonnage de modèle spécialisée et l'applique au modèle d'entrée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle d'entrée auquel appliquer les paramètres d'échantillonnage |
| `max_shift` | FLOAT | Oui | 0,0 à 100,0 | La valeur de décalage maximale utilisée dans le calcul d'interpolation linéaire (par défaut : 2,05) |
| `base_shift` | FLOAT | Oui | 0,0 à 100,0 | La valeur de décalage de base utilisée dans le calcul d'interpolation linéaire (par défaut : 0,95) |
| `latent` | LATENT | Non | - | Entrée latente facultative utilisée pour déterminer le nombre de jetons pour le calcul du décalage. Si elle n'est pas fournie, un nombre de jetons par défaut de 4096 est utilisé |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `model` | MODEL | Le modèle modifié avec les paramètres d'échantillonnage appliqués |

---
**Source fingerprint (SHA-256):** `2325754df1b2541a6adbdebecefde92e08535af0e179d7444093a61eb35cb24c`
