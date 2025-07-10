Le nœud `Moyenne de Conditionnement` est utilisé pour mélanger deux ensembles différents de conditionnements (comme des invites textuelles) selon un poids spécifié, générant un nouveau conditionnement situé entre les deux. En ajustant le paramètre de poids, vous pouvez contrôler de manière flexible l'influence de chaque conditionnement sur le résultat final. Il est particulièrement utile pour l'interpolation d'invites, la fusion de styles et d'autres cas avancés.

Comme illustré ci-dessous, en ajustant la force de `conditionnement_à`, vous pouvez obtenir un résultat intermédiaire entre les deux conditionnements.

![example](./asset/example.webp)

**Explication de l'exemple**
`conditioning_to` — `conditionnement_à`
`conditioning_from` — `conditionnement_de`
`conditioning_to_strength` — `force_conditionnement_à`

## Entrées

| Nom du paramètre         | Type de donnée      | Description |
|-------------------------|---------------------|-------------|
| `conditionnement_à`     | CONDITIONNEMENT     | Vecteur de conditionnement cible, servant de base principale pour la moyenne pondérée. |
| `conditionnement_de`    | CONDITIONNEMENT     | Vecteur de conditionnement source, qui sera mélangé au vecteur cible selon le poids spécifié. |
| `force_conditionnement_à` | FLOAT              | Poids du conditionnement cible, plage 0.0-1.0, par défaut 1.0, pas 0.01. |

## Sorties

| Nom du paramètre         | Type de donnée      | Description |
|-------------------------|---------------------|-------------|
| `conditionnement`       | CONDITIONNEMENT     | Retourne le vecteur de conditionnement mélangé, reflétant le résultat de la moyenne pondérée. |

## Cas d'utilisation typiques

- **Interpolation d'invites** : Transition fluide entre deux invites textuelles différentes, générant un contenu de style ou de sens intermédiaire.
- **Fusion de styles** : Combine différents styles artistiques ou conditions sémantiques pour créer de nouveaux effets.
- **Ajustement de la force** : Contrôle précis de l'influence d'un conditionnement sur le résultat en ajustant le poids.
- **Exploration créative** : Explorez divers effets génératifs en mélangeant différentes invites.
