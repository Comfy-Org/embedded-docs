
Ce nœud se spécialise dans la combinaison de deux entrées de masque à travers une variété d'opérations telles que l'addition, la soustraction et les opérations logiques, pour produire un nouveau masque modifié. Il gère de manière abstraite la manipulation des données de masque pour réaliser des effets de masquage complexes, servant de composant crucial dans les flux de travail d'édition et de traitement d'images basés sur les masques.

## Entrées

| Paramètre    | Data Type | Description                                                                                                                                      |
| ------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `destination`| MASK        | Le masque principal qui sera modifié en fonction de l'opération avec le masque source. Il joue un rôle central dans l'opération composite, servant de base pour les modifications. |
| `source`     | MASK        | Le masque secondaire qui sera utilisé en conjonction avec le masque de destination pour effectuer l'opération spécifiée, influençant le masque de sortie final. |
| `x`          | INT         | Le décalage horizontal auquel le masque source sera appliqué au masque de destination, affectant le positionnement du résultat composite.       |
| `y`          | INT         | Le décalage vertical auquel le masque source sera appliqué au masque de destination, affectant le positionnement du résultat composite.         |
| `operation`  | COMBO[STRING]| Spécifie le type d'opération à appliquer entre les masques de destination et source, tels que 'add', 'subtract', ou des opérations logiques, déterminant la nature de l'effet composite. |

## Sorties

| Paramètre | Data Type | Description                                                                 |
| --------- | ------------ | ---------------------------------------------------------------------------- |
| `mask`    | MASK        | Le masque résultant après l'application de l'opération spécifiée entre les masques de destination et source, représentant le résultat composite. |
