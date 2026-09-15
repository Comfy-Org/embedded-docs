# StartLoop

Le nœud Start Loop démarre une structure de boucle à l’intérieur d’un workflow. Il exécute le corps de boucle connecté une fois par itération et peut compter les itérations de trois manières : un nombre fixe de répétitions (simple), une plage d’index numériques (For), ou une passe par élément d’une liste (List). Chaque passe expose l’index courant, des indicateurs premier/dernier et une valeur transportée optionnelle qui peut être transmise d’une itération à la suivante.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mode` | Le mode d’itération de la boucle (par défaut : "simple"). Le mode sélectionné détermine quels paramètres supplémentaires sont affichés. | DYNAMIC_COMBO | Oui | `"simple"`<br>`"For"`<br>`"List"` |
| `cache_iterations` | Réutiliser les résultats d’itération inchangés des exécutions précédentes. Désactivez pour exécuter à nouveau chaque itération. Par défaut : false. | BOOLEAN | Non | true<br>false |
| `parent_iteration` | Connectez iteration_index d’une boucle Start Loop externe pour imbriquer cette boucle. Cette entrée est uniquement une entrée forcée (un lien est requis). | INT | Non | Tout entier |
| `initial_iteration_value` | Valeur exposée comme current_iteration_value lors de la première itération. | ANY (type-matched) | Non | Toute valeur |

### Entrées du mode Simple

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `num_iterations` | Nombre de fois où exécuter le corps de la boucle. Par défaut : 4. | INT | Oui | Minimum 0 |

### Entrées du mode For

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `start_iteration_index` | Index de la première itération lors de l’utilisation du mode de boucle For. Par défaut : 0. | INT | Oui | Tout entier |
| `max_iteration` | Valeur d’arrêt exclusive pour iteration_index en mode For. Par défaut : 4. | INT | Oui | Maximum 0xffffffffffffffff |
| `step` | Taille du pas d’index entre chaque itération lors de l’utilisation du mode de boucle For. Par défaut : 1. | INT | Oui | Minimum 1 |

### Entrées du mode List

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `list` | Liste d’éléments sur laquelle la boucle itère. Le corps de la boucle s’exécute une fois par élément. | ANY (type-matched list item) | Oui | Toute liste |

Remarques :

- Seuls les paramètres appartenant au `mode` actuellement sélectionné sont affichés et utilisés.
- En mode Simple, les indices d’itération vont de 0 à `num_iterations` moins 1. En mode For, les indices vont de `start_iteration_index` jusqu’à (mais sans inclure) `max_iteration`, en augmentant de `step`. En mode List, une itération s’exécute par élément dans `list`.
- `step` ne doit pas être 0 ; une valeur de 0 génère une erreur. Les valeurs inférieures à 1 ne sont pas autorisées.
- Si le nombre d’itérations calculé est zéro, la sortie `is_last` est signalée comme vraie et le corps de la boucle ne s’exécute pas.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `iteration_index` | Index de l’itération actuelle de la boucle. | INT |
| `is_first` | Vrai pendant la première itération de la boucle. | BOOLEAN |
| `is_last` | Vrai pendant la dernière itération de la boucle. | BOOLEAN |
| `list_item` | Élément actuel de la liste lors de l’utilisation du mode List. Aucun en modes Simple et For. | ANY (type-matched) |
| `current_iteration_value` | Valeur transportée par la boucle pour l’itération actuelle : initial_iteration_value lors de la première itération, puis next_iteration_value depuis End Loop à chaque itération suivante. | ANY (type-matched) |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StartLoop/fr.md)

---
**Source fingerprint (SHA-256):** `2584af9fd623f4762f440a043679e47aeef25ad0d571cfac11506cb513dd1b98`
