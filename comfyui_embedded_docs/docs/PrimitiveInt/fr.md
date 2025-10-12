> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveInt/fr.md)

Le nœud PrimitiveInt offre un moyen simple de travailler avec des valeurs entières dans votre flux de travail. Il prend une valeur entière en entrée et renvoie la même valeur en sortie, ce qui le rend utile pour transmettre des paramètres entiers entre les nœuds ou pour définir des valeurs numériques spécifiques pour d'autres opérations.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `value` | INT | Oui | -9223372036854775807 à 9223372036854775807 | La valeur entière à sortir |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | INT | La valeur entière d'entrée transmise sans modification |