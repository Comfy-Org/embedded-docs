# PourcentageÉchantillonnageVersSigma

Le nœud `SamplingPercentToSigma` convertit une valeur de pourcentage d'échantillonnage en une valeur sigma correspondante à l'aide des paramètres d'échantillonnage du modèle. Il prend une valeur de pourcentage comprise entre 0.0 et 1.0 et la fait correspondre à la valeur sigma appropriée dans le plan de bruit du modèle, avec des options pour renvoyer soit le sigma calculé, soit les valeurs sigma maximales/minimales réelles aux limites.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle contenant les paramètres d'échantillonnage utilisés pour la conversion | MODEL | Oui | - |
| `pourcent_échantillonnage` | Le pourcentage d'échantillonnage à convertir en sigma (par défaut : 0.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.0001) |
| `retourner_sigma_réel` | Renvoie la valeur sigma réelle au lieu de la valeur utilisée pour les vérifications d'intervalle. Cela n'affecte que les résultats à 0.0 et 1.0. (par défaut : False) | BOOLEAN | Oui | - |

Lorsque `return_actual_sigma` est activé, un `sampling_percent` de 0.0 renvoie la valeur sigma maximale du modèle (sigma_max), et un `sampling_percent` de 1.0 renvoie la valeur sigma minimale (sigma_min). Pour tous les autres pourcentages, le résultat est identique, que l'option soit activée ou non.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `valeur_sigma` | La valeur sigma convertie correspondant au pourcentage d'échantillonnage d'entrée | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/fr.md)

---
**Source fingerprint (SHA-256):** `30decf1d4804accbdf2a70eba1a773b41ef0e09cfb74f2a9388044dadf0a1ac1`
