# Moyenne de Conditionnement

Le nœud `ConditioningAverage` est utilisé pour fusionner deux ensembles différents de conditionnements (tels que des invites textuelles) selon un poids spécifié, générant ainsi un nouveau vecteur de conditionnement situé entre les deux. En ajustant le paramètre de poids, vous pouvez contrôler de manière flexible l'influence de chaque conditionnement sur le résultat final. Cela est particulièrement adapté à l'interpolation d'invites, à la fusion de styles et à d'autres cas d'utilisation avancés.

Comme illustré ci-dessous, en ajustant la force de `conditioning_to`, vous pouvez obtenir un résultat situé entre les deux conditionnements.

![exemple](./asset/example.webp)

## Entrées

| Paramètre | Description | Type Comfy |
| --- | --- | --- |
| `conditionnement_à` | Le vecteur de conditionnement cible, servant de base principale pour la moyenne pondérée. | `CONDITIONING` |
| `conditionnement_de` | Le vecteur de conditionnement source, qui sera fusionné dans la cible selon un certain poids. | `CONDITIONING` |
| `force_conditionnement_à` | La force du conditionnement cible, plage 0,0-1,0, valeur par défaut 1,0, pas de 0,01. | `FLOAT` |

## Sorties

| Paramètre | Description | Type Comfy |
| --- | --- | --- |
| `conditioning` | Le vecteur de conditionnement résultant après la fusion, reflétant la moyenne pondérée. | `CONDITIONING` |

## Cas d'utilisation typiques

- **Interpolation d'invites :** Transition en douceur entre deux invites textuelles différentes, générant un contenu au style ou à la sémantique intermédiaire.
- **Fusion de styles :** Combiner différents styles artistiques ou conditions sémantiques pour créer des effets novateurs.
- **Ajustement de la force :** Contrôler précisément l'influence d'un conditionnement particulier sur le résultat en ajustant le poids.
- **Exploration créative :** Explorer divers effets génératifs en mélangeant différentes invites.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningAverage/fr.md)
