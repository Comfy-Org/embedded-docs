# ComboOptionTestNode

Le nœud ComboOptionTestNode est un nœud logique conçu pour tester et transmettre les sélections des listes déroulantes. Il prend deux entrées de type liste déroulante, chacune avec un ensemble prédéfini d'options, et renvoie les valeurs sélectionnées directement sans modification.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `combo` | La première sélection parmi un ensemble de trois options de test. | COMBO | Oui | `"option1"`<br>`"option2"`<br>`"option3"` |
| `combo2` | La deuxième sélection parmi un ensemble différent de trois options de test. | COMBO | Oui | `"option4"`<br>`"option5"`<br>`"option6"` |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output_1` | Renvoie la valeur sélectionnée dans la première liste déroulante (`combo`). | COMBO |
| `output_2` | Renvoie la valeur sélectionnée dans la deuxième liste déroulante (`combo2`). | COMBO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/fr.md)

---
**Source fingerprint (SHA-256):** `fe0b6a35680de55767af2c0d8a293010ddb4c4282cfdde7f9dff7a3a11ff1e5c`
