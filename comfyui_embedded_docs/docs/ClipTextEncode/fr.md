Le nœud CLIPTextEncode est conçu pour encoder les entrées textuelles à l'aide d'un modèle CLIP, transformant le texte en une forme utilisable pour le conditionnement dans les tâches génératives. Il simplifie la complexité de la tokenisation et de l'encodage du texte, offrant une interface simplifiée pour générer des vecteurs de conditionnement basés sur le texte.

En plus des invites textuelles normales, vous pouvez également utiliser des modèles d'incorporation. Par exemple, si vous ajoutez un modèle d'incorporation dans le répertoire `ComfyUI/models/embeddings`, vous pouvez utiliser ce modèle d'incorporation dans l'invite.

Par exemple, si le nom du modèle correspondant est `EasyNegative`, vous pouvez utiliser `embedding:EasyNegative,` dans l'invite pour utiliser ce modèle correspondant.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `text`    | `STRING`    | Le paramètre 'text' est l'entrée textuelle qui sera encodée. Il joue un rôle crucial dans la détermination du vecteur de conditionnement de sortie, car il est la source principale d'information pour le processus d'encodage. |
| `clip`    | CLIP      | Le paramètre 'clip' représente le modèle CLIP utilisé pour la tokenisation et l'encodage du texte. Il est essentiel pour convertir l'entrée textuelle en un vecteur de conditionnement, influençant la qualité et la pertinence de la sortie générée. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | La sortie 'conditioning' est une représentation vectorielle du texte d'entrée, encodée par le modèle CLIP. Elle sert de composant crucial pour guider les modèles génératifs dans la production de sorties pertinentes et cohérentes. |
