Le nœud `GLIGENTextBoxApply` est conçu pour intégrer un conditionnement basé sur du texte dans l’entrée d’un modèle génératif, en appliquant spécifiquement des paramètres de zone de texte et en les encodant à l’aide d’un modèle CLIP. Ce processus enrichit le conditionnement avec des informations spatiales et textuelles, facilitant ainsi une génération plus précise et contextuelle.

## Entrées

| Paramètre | Description | Type Comfy |
| --- | --- | --- |
| `conditionnement_à` | Spécifie l’entrée de conditionnement initiale à laquelle les paramètres de la zone de texte et les informations textuelles encodées seront ajoutés. Il joue un rôle crucial dans la détermination de la sortie finale en intégrant de nouvelles données de conditionnement. | `CONDITIONING` |
| `clip` | Le modèle CLIP utilisé pour encoder le texte fourni dans un format exploitable par le modèle génératif. Il est essentiel pour convertir les informations textuelles en un format de conditionnement compatible. | `CLIP` |
| `modèle_boîte_texte_gligen` | Représente la configuration spécifique du modèle GLIGEN à utiliser pour générer la zone de texte. Il est crucial pour garantir que la zone de texte soit générée selon les spécifications souhaitées. | `GLIGEN` |
| `texte` | Le contenu textuel à encoder et à intégrer dans le conditionnement. Il fournit les informations sémantiques qui guident le modèle génératif. | `STRING` |
| `largeur` | La largeur de la zone de texte en pixels. Elle définit la dimension spatiale de la zone de texte dans l’image générée. | `INT` |
| `hauteur` | La hauteur de la zone de texte en pixels. Comme la largeur, elle définit la dimension spatiale de la zone de texte dans l’image générée. | `INT` |
| `x` | La coordonnée x du coin supérieur gauche de la zone de texte dans l’image générée. Elle spécifie la position horizontale de la zone de texte. | `INT` |
| `y` | La coordonnée y du coin supérieur gauche de la zone de texte dans l’image générée. Elle spécifie la position verticale de la zone de texte. | `INT` |

## Sorties

| Paramètre | Description | Type Comfy |
| --- | --- | --- |
| `conditioning` | La sortie de conditionnement enrichie, qui inclut les données de conditionnement d’origine ainsi que les nouveaux paramètres de zone de texte et les informations textuelles encodées. Elle est utilisée pour guider le modèle génératif afin de produire des résultats contextuels. | `CONDITIONING` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLIGENTextBoxApply/fr.md)
