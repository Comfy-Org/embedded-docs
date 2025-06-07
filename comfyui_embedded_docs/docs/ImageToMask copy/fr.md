
Le nœud ImageToMask est conçu pour convertir une image en un masque basé sur un canal de couleur spécifié. Il permet l'extraction de couches de masque correspondant aux canaux rouge, vert, bleu ou alpha d'une image, facilitant les opérations nécessitant un masquage ou un traitement spécifique à un canal.

## Entrées

| Paramètre   | Data Type | Description                                                                                                          |
|-------------|-------------|----------------------------------------------------------------------------------------------------------------------|
| `image`     | `IMAGE`     | Le paramètre 'image' représente l'image d'entrée à partir de laquelle un masque sera généré en fonction du canal de couleur spécifié. Il joue un rôle crucial dans la détermination du contenu et des caractéristiques du masque résultant. |
| `channel`   | COMBO[STRING] | Le paramètre 'channel' spécifie quel canal de couleur (rouge, vert, bleu ou alpha) de l'image d'entrée doit être utilisé pour générer le masque. Ce choix influence directement l'apparence du masque et les parties de l'image qui sont mises en évidence ou masquées. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `mask`    | `MASK`      | La sortie 'mask' est une représentation binaire ou en niveaux de gris du canal de couleur spécifié de l'image d'entrée, utile pour un traitement d'image ou des opérations de masquage ultérieurs. |
