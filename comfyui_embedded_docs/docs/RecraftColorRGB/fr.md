> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftColorRGB/fr.md)

Créez une couleur Recraft en choisissant des valeurs RVB spécifiques. Ce nœud vous permet de définir une couleur en spécifiant des valeurs individuelles pour le rouge, le vert et le bleu, qui sont ensuite converties dans un format de couleur Recraft utilisable dans d'autres opérations Recraft.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `r` | INT | Oui | 0-255 | Valeur du rouge de la couleur (par défaut : 0) |
| `g` | INT | Oui | 0-255 | Valeur du vert de la couleur (par défaut : 0) |
| `b` | INT | Oui | 0-255 | Valeur du bleu de la couleur (par défaut : 0) |
| `recraft_color` | COLOR | Non | - | Couleur Recraft existante optionnelle à étendre |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `recraft_color` | COLOR | L'objet couleur Recraft créé contenant les valeurs RVB spécifiées |
