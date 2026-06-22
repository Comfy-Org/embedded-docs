# Recraft Couleur RGB

Créez une couleur Recraft en spécifiant des valeurs individuelles de rouge, vert et bleu. Ce nœud prend des valeurs entières RVB (0-255) et les convertit dans un format de couleur Recraft pouvant être utilisé dans d'autres opérations Recraft. Vous pouvez également fournir optionnellement une chaîne de couleurs Recraft existante pour l'étendre avec la nouvelle couleur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `r` | Valeur rouge de la couleur (par défaut : 0) | INT | Oui | 0-255 |
| `g` | Valeur verte de la couleur (par défaut : 0) | INT | Oui | 0-255 |
| `b` | Valeur bleue de la couleur (par défaut : 0) | INT | Oui | 0-255 |
| `recraft_color` | Chaîne de couleurs Recraft existante optionnelle à étendre avec la nouvelle couleur RVB | COLOR | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `recraft_color` | L'objet couleur Recraft créé contenant les valeurs RVB spécifiées, ou la chaîne de couleurs étendue si une chaîne existante a été fournie | COLOR |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftColorRGB/fr.md)

---
**Source fingerprint (SHA-256):** `8c3503632d085fa4c1771f92f17008b7b051e9604d9e7d1e7d352cbbbd22dddc`
