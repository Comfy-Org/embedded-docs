Le nœud `GLIGENTextBoxApply` est conçu pour intégrer le conditionnement basé sur le texte dans l'entrée d'un modèle génératif, en appliquant spécifiquement les paramètres de la boîte de texte et en les encodant à l'aide d'un modèle CLIP. Ce processus enrichit le conditionnement avec des informations spatiales et textuelles, facilitant une génération plus précise et contextuellement consciente.

## Entrées

| Paramètre            | Comfy dtype        | Description |
|----------------------|--------------------|-------------|
| `conditioning_to`     | `CONDITIONING`     | Spécifie l'entrée de conditionnement initiale à laquelle les paramètres de la boîte de texte et les informations textuelles encodées seront ajoutés. Il joue un rôle crucial dans la détermination du résultat final en intégrant de nouvelles données de conditionnement. |
| `clip`               | `CLIP`             | Le modèle CLIP utilisé pour encoder le texte fourni dans un format qui peut être utilisé par le modèle génératif. Il est essentiel pour convertir les informations textuelles en un format de conditionnement compatible. |
| `gligen_textbox_model` | `GLIGEN`         | Représente la configuration spécifique du modèle GLIGEN à utiliser pour générer la boîte de texte. Il est crucial pour s'assurer que la boîte de texte est générée selon les spécifications souhaitées. |
| `text`               | `STRING`           | Le contenu textuel à encoder et intégrer dans le conditionnement. Il fournit l'information sémantique qui guide le modèle génératif. |
| `width`              | `INT`              | La largeur de la boîte de texte en pixels. Elle définit la dimension spatiale de la boîte de texte dans l'image générée. |
| `height`             | `INT`              | La hauteur de la boîte de texte en pixels. Comme la largeur, elle définit la dimension spatiale de la boîte de texte dans l'image générée. |
| `x`                  | `INT`              | La coordonnée x du coin supérieur gauche de la boîte de texte dans l'image générée. Elle spécifie la position horizontale de la boîte de texte. |
| `y`                  | `INT`              | La coordonnée y du coin supérieur gauche de la boîte de texte dans l'image générée. Elle spécifie la position verticale de la boîte de texte. |

## Sorties

| Paramètre            | Comfy dtype        | Description |
|----------------------|--------------------|-------------|
| `conditioning`        | `CONDITIONING`     | La sortie de conditionnement enrichie, qui inclut les données de conditionnement originales ainsi que les nouveaux paramètres de la boîte de texte et les informations textuelles encodées. Elle est utilisée pour guider le modèle génératif dans la production de sorties contextuellement conscientes. |
