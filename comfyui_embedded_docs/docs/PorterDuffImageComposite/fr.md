> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PorterDuffImageComposite/fr.md)

Le nœud **PorterDuffImageComposite** est conçu pour effectuer la composition d'images à l'aide des opérateurs de composition Porter-Duff. Il permet de combiner des images source et de destination selon différents modes de fusion, offrant ainsi la possibilité de créer des effets visuels complexes en manipulant la transparence des images et en les superposant de manière créative.

## Entrées

| Paramètre | Type de données | Description |
| --------- | ------------ | ----------- |
| `source`  | `IMAGE`     | Le tenseur de l'image source à composer sur l'image de destination. Il joue un rôle crucial dans la détermination du résultat visuel final en fonction du mode de composition sélectionné. |
| `source_alpha` | `MASK` | Le canal alpha de l'image source, qui spécifie la transparence de chaque pixel de l'image source. Il affecte la manière dont l'image source se fond avec l'image de destination. |
| `destination` | `IMAGE` | Le tenseur de l'image de destination servant d'arrière-plan sur lequel l'image source est composée. Il contribue à l'image finale composée en fonction du mode de fusion. |
| `destination_alpha` | `MASK` | Le canal alpha de l'image de destination, définissant la transparence des pixels de l'image de destination. Il influence la fusion des images source et de destination. |
| `mode` | COMBO[STRING] | Le mode de composition Porter-Duff à appliquer, qui détermine la manière dont les images source et de destination sont fusionnées. Chaque mode produit des effets visuels différents. |

## Sorties

| Paramètre | Type de données | Description |
| --------- | ------------ | ----------- |
| `image`   | `IMAGE`     | L'image composée résultant de l'application du mode Porter-Duff spécifié. |
| `mask`    | `MASK`      | Le canal alpha de l'image composée, indiquant la transparence de chaque pixel. |