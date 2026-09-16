# StartLoop

Le nœud Start Loop démarre une structure de boucle à l'intérieur d'un workflow. Il exécute le corps de boucle connecté une fois par itération et peut compter les itérations de trois manières : un nombre fixe de répétitions (simple), une plage d'indices numériques (For), ou un passage par élément d'une liste (List). Chaque passage expose l'indice courant, des indicateurs premier/dernier, et une valeur transportée facultative qui peut être transmise d'une itération à la suivante.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mode` | Le mode d'itération de la boucle (par défaut : "simple"). Le mode sélectionné détermine quels paramètres supplémentaires sont affichés. | DYNAMIC_COMBO | Oui | `"simple"`<br>`"For"`<br>`"List"` |
| `cache_iterations` | Réutilise les résultats d'itération inchangés des exécutions précédentes. Désactivez pour exécuter à nouveau chaque itération. Par défaut : false. | BOOLEAN | Oui | true<br>false |
| `parent_iteration` | Connectez iteration_index depuis un Start Loop externe pour imbriquer cette boucle. Cette entrée est obligatoirement connectée (un lien est requis). | INT | Non | Tout entier |
| `initial_iteration_value` | Valeur exposée en tant que current_iteration_value lors de la première itération. | ANY (type correspondant) | Non | Toute valeur |

### Entrées du mode Simple

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `num_iterations` | Nombre de fois où exécuter le corps de la boucle. Par défaut : 4. | INT | Oui | Minimum 0 |

### Entrées du mode For

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `start_iteration_index` | Indice de la première itération lors de l'utilisation du mode de boucle For. Par défaut : 0. | INT | Oui | Tout entier |
| `max_iteration` | Valeur d'arrêt exclusive pour iteration_index en mode For. Par défaut : 4. | INT | Oui | Maximum 0xffffffffffffffff |
| `step` | Taille du pas d'indice entre chaque itération lors de l'utilisation du mode de boucle For. Par défaut : 1. | INT | Oui | Minimum 1 |

### Entrées du mode List

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `list` | Liste d'éléments sur laquelle la boucle itère. Le corps de la boucle s'exécute une fois par élément. | ANY (élément de liste à type correspondant) | Oui | Toute liste |

Remarques :

- Seuls les paramètres appartenant au `mode` actuellement sélectionné sont affichés et utilisés.
- En mode Simple, les indices d'itération vont de 0 jusqu'à `num_iterations` moins 1. En mode For, les indices vont de `start_iteration_index` jusqu'à (mais sans inclure) `max_iteration`, en augmentant de `step`. En mode List, une itération s'exécute par élément dans `list`.
- `step` ne doit pas être 0 ; une valeur de 0 déclenche une erreur. Les valeurs inférieures à 1 ne sont pas autorisées.
- Si le nombre calculé d'itérations est zéro, la sortie `is_last` est signalée comme true et le corps de la boucle ne s'exécute pas.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `iteration_index` | Indice de l'itération de boucle actuelle. | INT |
| `is_first` | Vrai pendant la première itération de la boucle. | BOOLEAN |
| `is_last` | Vrai pendant la dernière itération de la boucle. | BOOLEAN |
| `list_item` | Élément courant de la liste lors de l'utilisation du mode List. Aucun en modes Simple et For. | ANY (type correspondant) |
| `current_iteration_value` | Valeur transportée par la boucle pour l'itération courante : initial_iteration_value lors de la première itération, puis next_iteration_value depuis End Loop à chaque itération suivante. | ANY (type correspondant) |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StartLoop/fr.md)

---
**Source fingerprint (SHA-256):** `be34fedd4db9d4f4cc795855c87f6489f294e029da316b5dc66e5af7dff004a9`
