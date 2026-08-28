# ModèleÉchantillonnageLTXV

Le nœud ModelSamplingLTXV applique des paramètres d'échantillonnage avancés à un modèle en fonction du nombre de jetons. Il calcule une valeur de décalage à l'aide d'une interpolation linéaire entre les valeurs de décalage de base et maximale, ce calcul dépendant du nombre de jetons dans le latent d'entrée. Le nœud crée ensuite une configuration d'échantillonnage de modèle spécialisée et l'applique au modèle d'entrée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'entrée auquel appliquer les paramètres d'échantillonnage | MODEL | Oui | - |
| `décalage_max` | La valeur de décalage maximale utilisée dans le calcul d'interpolation linéaire (par défaut : 2.05) | FLOAT | Oui | 0.0 à 100.0 (pas : 0.01) |
| `décalage_base` | La valeur de décalage de base utilisée dans le calcul d'interpolation linéaire (par défaut : 0.95) | FLOAT | Oui | 0.0 à 100.0 (pas : 0.01) |
| `latent` | Entrée latente optionnelle utilisée pour déterminer le nombre de jetons pour le calcul du décalage. Si elle n'est pas fournie, un nombre de jetons par défaut de 4096 est utilisé | LATENT | Non | - |

La valeur de décalage est calculée en interpolant entre `base_shift` et `max_shift` sur une plage de jetons de 1024 à 4096. Lorsqu'un `latent` est fourni, le nombre de jetons est calculé à partir du produit de ses dimensions spatiales (telles que la hauteur et la largeur). Si aucun `latent` n'est fourni, le nombre de jetons par défaut est de 4096.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec les paramètres d'échantillonnage appliqués | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/fr.md)

---
**Source fingerprint (SHA-256):** `aba596c5478e9d6ee821eec1eca15506935bcc765a368087ccc442fc2ed6671b`
