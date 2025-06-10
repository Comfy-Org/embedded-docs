`CLIP Text Encode (Prompt)` agit comme un traducteur, convertissant vos descriptions textuelles créatives en un "langage" spécial que l'IA peut comprendre, aidant ainsi l'IA à interpréter précisément le type d'image que vous souhaitez créer.

## Principe de Fonctionnement

Imaginez que vous communiquez avec un artiste étranger - vous avez besoin d'un traducteur pour transmettre précisément l'œuvre que vous désirez. Ce nœud agit comme ce traducteur, utilisant le modèle CLIP (un modèle d'IA entraîné sur de vastes quantités de paires image-texte) pour comprendre vos descriptions textuelles et les convertir en "instructions" que le modèle d'art IA peut comprendre.

## Entrées

| Paramètre | Type de Donnée | Méthode d'Entrée | Valeur par Défaut | Plage | Description |
|-----------|----------------|------------------|-------------------|--------|-------------|
| text | STRING | Saisie de texte | Vide | Tout texte | Comme des instructions détaillées à un artiste, entrez ici votre description d'image. Supporte le texte multiligne pour des descriptions détaillées. |
| clip | CLIP | Sélection de modèle | Aucun | Modèles CLIP chargés | Comme choisir un traducteur spécifique, différents modèles CLIP sont comme différents traducteurs avec des compréhensions légèrement différentes des styles artistiques. |

## Sorties

| Nom de Sortie | Type de Donnée | Description |
|---------------|----------------|-------------|
| CONDITIONNEMENT | CONDITIONING | Ce sont les "instructions de peinture" traduites contenant des directives créatives détaillées que le modèle d'IA peut comprendre. Ces instructions indiquent au modèle d'IA comment créer une image correspondant à votre description. |

## Conseils d'Utilisation

1. **Utilisation Basique des Prompts Textuels**
   - Écrivez des descriptions détaillées comme si vous rédigiez un court essai
   - Des descriptions plus spécifiques mènent à des résultats plus précis
   - Utilisez des virgules anglaises pour séparer différents éléments descriptifs

2. **Fonction Spéciale : Utilisation des Modèles d'Embedding**
   - Les modèles d'embedding sont comme des packages de styles artistiques préréglés qui peuvent rapidement appliquer des effets artistiques spécifiques
   - Supporte actuellement les formats de fichiers .safetensors, .pt et .bin, et vous n'avez pas nécessairement besoin d'utiliser le nom complet du modèle
   - Comment utiliser :
     1. Placez le fichier du modèle d'embedding (au format .pt) dans le dossier `ComfyUI/models/embeddings`
     2. Utilisez `embedding:nom_du_modèle` dans votre texte
     Exemple : Si vous avez un modèle nommé `EasyNegative.pt`, vous pouvez l'utiliser ainsi :

     ```
     a beautiful landscape, embedding:EasyNegative, high quality
     ```

3. **Ajustement des Poids des Prompts**
   - Utilisez des parenthèses pour ajuster l'importance de certaines descriptions
   - Par exemple : `(beautiful:1.2)` rendra la caractéristique "beautiful" plus prononcée
   - Les parenthèses simples `()` ont un poids par défaut de 1.1
   - Utilisez les raccourcis clavier `ctrl + flèches haut/bas` pour ajuster rapidement les poids
   - La taille des pas d'ajustement des poids peut être modifiée dans les paramètres

4. **Notes Importantes**
   - Assurez-vous que le modèle CLIP est correctement chargé
   - Utilisez des descriptions textuelles positives et claires
   - Lors de l'utilisation de modèles d'embedding, assurez-vous que le nom du fichier est correct et compatible avec l'architecture de votre modèle principal actuel
