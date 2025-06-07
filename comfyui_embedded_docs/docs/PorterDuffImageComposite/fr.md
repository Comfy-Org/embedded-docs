
Le nœud PorterDuffImageComposite est conçu pour effectuer la composition d'images en utilisant les opérateurs de composition Porter-Duff. Il permet la combinaison d'images source et destination selon divers modes de fusion, permettant la création d'effets visuels complexes en manipulant la transparence des images et en superposant les images de manière créative.

## Entrées

| Paramètre | Type Comfy | Description |
| --------- | ----------- | ----------- |
| `source`  | `IMAGE`     | Le tenseur d'image source à composer sur l'image de destination. Il joue un rôle crucial dans la détermination du résultat visuel final en fonction du mode de composition sélectionné. |
| `source_alpha` | `MASK` | Le canal alpha de l'image source, qui spécifie la transparence de chaque pixel de l'image source. Il affecte la manière dont l'image source se fond avec l'image de destination. |
| `destination` | `IMAGE` | Le tenseur d'image de destination qui sert de toile de fond sur laquelle l'image source est composée. Il contribue à l'image composée finale en fonction du mode de fusion. |
| `destination_alpha` | `MASK` | Le canal alpha de l'image de destination, définissant la transparence des pixels de l'image de destination. Il influence la fusion des images source et destination. |
| `mode` | COMBO[STRING] | Le mode de composition Porter-Duff à appliquer, qui détermine comment les images source et destination sont fusionnées. Chaque mode crée des effets visuels différents. |

## Sorties

| Paramètre | Type Comfy | Description |
| --------- | ----------- | ----------- |
| `image`   | `IMAGE`     | L'image composée résultant de l'application du mode Porter-Duff spécifié. |
| `mask`    | `MASK`      | Le canal alpha de l'image composée, indiquant la transparence de chaque pixel. |
