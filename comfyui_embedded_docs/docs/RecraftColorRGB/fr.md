> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftColorRGB/fr.md)

Créez une couleur Recraft en spécifiant des valeurs individuelles de rouge, vert et bleu. Ce nœud prend des valeurs entières RVB (0-255) et les convertit dans un format de couleur Recraft pouvant être utilisé dans d'autres opérations Recraft. Vous pouvez également fournir optionnellement une chaîne de couleurs Recraft existante pour l'étendre avec la nouvelle couleur.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `r` | INT | Oui | 0-255 | Valeur rouge de la couleur (par défaut : 0) |
| `g` | INT | Oui | 0-255 | Valeur verte de la couleur (par défaut : 0) |
| `b` | INT | Oui | 0-255 | Valeur bleue de la couleur (par défaut : 0) |
| `recraft_color` | COLOR | Non | - | Chaîne de couleurs Recraft existante optionnelle à étendre avec la nouvelle couleur RVB |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `recraft_color` | COLOR | L'objet couleur Recraft créé contenant les valeurs RVB spécifiées, ou la chaîne de couleurs étendue si une chaîne existante a été fournie |

---
**Source fingerprint (SHA-256):** `8c3503632d085fa4c1771f92f17008b7b051e9604d9e7d1e7d352cbbbd22dddc`
