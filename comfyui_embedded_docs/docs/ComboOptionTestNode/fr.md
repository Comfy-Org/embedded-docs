> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/fr.md)

Le ComboOptionTestNode est un nœud logique conçu pour tester et transmettre des sélections de listes déroulantes. Il prend deux entrées de type liste déroulante, chacune avec un ensemble prédéfini d'options, et sort les valeurs sélectionnées directement sans modification.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `combo` | COMBO | Oui | `"option1"`<br>`"option2"`<br>`"option3"` | La première sélection parmi un ensemble de trois options de test. |
| `combo2` | COMBO | Oui | `"option4"`<br>`"option5"`<br>`"option6"` | La seconde sélection parmi un ensemble différent de trois options de test. |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output_1` | COMBO | Sort la valeur sélectionnée dans la première liste déroulante (`combo`). |
| `output_2` | COMBO | Sort la valeur sélectionnée dans la seconde liste déroulante (`combo2`). |
