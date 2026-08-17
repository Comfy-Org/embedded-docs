# ModèleÉchantillonnageLTXV

Le nœud ModelSamplingLTXV applique des paramètres d'échantillonnage avancés à un modèle en fonction du nombre de jetons. Il calcule une valeur de décalage en utilisant une interpolation linéaire entre les valeurs de décalage de base et maximale, le calcul dépendant du nombre de jetons dans le latent d'entrée. Le nœud crée ensuite une configuration d'échantillonnage de modèle spécialisée et l'applique au modèle d'entrée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle d'entrée auquel appliquer les paramètres d'échantillonnage | MODEL | Oui | - |
| `max_shift` | La valeur de décalage maximale utilisée dans le calcul d'interpolation linéaire. La valeur de décalage est égale à ce maximum à 4096 jetons (défaut : 2.05) | FLOAT | Oui | 0.0 à 100.0 |
| `base_shift` | La valeur de décalage de base utilisée dans le calcul d'interpolation linéaire. La valeur de décalage est égale à cette base à 1024 jetons (défaut : 0.95) | FLOAT | Oui | 0.0 à 100.0 |
| `latent` | Entrée latente facultative utilisée pour déterminer le nombre de jetons pour le calcul du décalage. Le nombre de jetons est le produit des dimensions spatiales des échantillons latents. S'il n'est pas fourni, un nombre de jetons par défaut de 4096 est utilisé | LATENT | Non | - |

Remarque : La valeur de décalage est calculée par interpolation linéaire entre `base_shift` à 1024 jetons et `max_shift` à 4096 jetons. Lorsqu'aucun `latent` n'est fourni, le nombre de jetons par défaut de 4096 rend le décalage égal à `max_shift`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec les paramètres d'échantillonnage appliqués | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/fr.md)

---
**Source fingerprint (SHA-256):** `aba596c5478e9d6ee821eec1eca15506935bcc765a368087ccc442fc2ed6671b`
