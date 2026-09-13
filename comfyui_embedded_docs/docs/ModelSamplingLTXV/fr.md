# ModèleÉchantillonnageLTXV

Le nœud ModelSamplingLTXV applique des paramètres d'échantillonnage avancés à un modèle en fonction du nombre de tokens. Il calcule une valeur de décalage en interpolant linéairement entre `base_shift` et `max_shift` sur une plage de tokens, puis modifie le modèle d'entrée avec une configuration d'échantillonnage spécialisée. Si un latent est fourni, ses dimensions déterminent le nombre de tokens ; sinon, 4096 tokens sont utilisés.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle d'entrée auquel appliquer les paramètres d'échantillonnage. | MODEL | Oui | - |
| `max_shift` | La valeur de décalage maximale utilisée dans le calcul d'interpolation linéaire (par défaut : 2.05). | FLOAT | Oui | 0.0 à 100.0 (pas : 0.01) |
| `base_shift` | La valeur de décalage de base utilisée dans le calcul d'interpolation linéaire (par défaut : 0.95). | FLOAT | Oui | 0.0 à 100.0 (pas : 0.01) |
| `latent` | Entrée `latent` facultative utilisée pour déterminer le nombre de tokens pour le calcul du décalage. Si elle n'est pas fournie, un nombre de tokens par défaut de 4096 est utilisé. | LATENT | Non | - |

La valeur de décalage est calculée en interpolant entre `base_shift` à 1024 tokens et `max_shift` à 4096 tokens. Lorsque `latent` est fourni, le nombre de tokens est le produit de toutes les dimensions après les deux premières dans les échantillons latents (les dimensions spatiales/temporelles). Si aucun `latent` n'est fourni, le nombre de tokens est par défaut de 4096.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec les paramètres d'échantillonnage appliqués. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/fr.md)

---
**Source fingerprint (SHA-256):** `aba596c5478e9d6ee821eec1eca15506935bcc765a368087ccc442fc2ed6671b`
