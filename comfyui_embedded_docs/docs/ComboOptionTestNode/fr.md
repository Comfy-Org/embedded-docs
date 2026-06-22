# ComboOptionTestNode

Voici la traduction en français de la documentation du nœud ComfyUI :

Le **ComboOptionTestNode** est un nœud logique conçu pour tester et transmettre les sélections de listes déroulantes. Il accepte deux entrées de type liste déroulante, chacune avec un ensemble prédéfini d'options, et renvoie directement les valeurs sélectionnées sans modification.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `combo` | La première sélection parmi un ensemble de trois options de test. | COMBO | Oui | `"option1"`<br>`"option2"`<br>`"option3"` |
| `combo2` | La deuxième sélection parmi un ensemble différent de trois options de test. | COMBO | Oui | `"option4"`<br>`"option5"`<br>`"option6"` |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output_1` | Renvoie la valeur sélectionnée dans la première liste déroulante (`combo`). | COMBO |
| `output_2` | Renvoie la valeur sélectionnée dans la deuxième liste déroulante (`combo2`). | COMBO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/fr.md)

---
**Source fingerprint (SHA-256):** `2f5a73eb7c2962a983b12688159e52d4d05f569d67909f536956ab18a6cc87d7`
