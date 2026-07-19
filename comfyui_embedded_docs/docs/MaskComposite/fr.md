# MaskComposite

Ce nœud est spécialisé dans la combinaison de deux entrées de masque via diverses opérations telles que l'addition, la soustraction et les opérations logiques, afin de produire un nouveau masque modifié. Il gère de manière abstraite la manipulation des données de masque pour obtenir des effets de masquage complexes, constituant un composant essentiel dans les workflows d'édition et de traitement d'images basés sur des masques.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `destination` | Le masque principal qui sera modifié en fonction de l'opération avec le masque source. Il joue un rôle central dans l'opération composite, servant de base aux modifications. | MASK |
| `source` | Le masque secondaire qui sera utilisé conjointement avec le masque de destination pour effectuer l'opération spécifiée, influençant le masque de sortie final. | MASK |
| `x` | Le décalage horizontal auquel le masque source sera appliqué au masque de destination, affectant le positionnement du résultat composite. | INT |
| `y` | Le décalage vertical auquel le masque source sera appliqué au masque de destination, affectant le positionnement du résultat composite. | INT |
| `opération` | Spécifie le type d'opération à appliquer entre les masques de destination et source, comme 'add' (addition), 'subtract' (soustraction) ou des opérations logiques, déterminant la nature de l'effet composite. | COMBO[STRING] |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `mask` | Le masque résultant après application de l'opération spécifiée entre les masques de destination et source, représentant le résultat composite. | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskComposite/fr.md)
