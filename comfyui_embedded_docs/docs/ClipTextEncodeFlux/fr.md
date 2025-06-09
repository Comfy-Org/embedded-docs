Encodage de Texte : Utilise le modèle CLIP pour encoder l'entrée texte dans `clip_l`, capturant les caractéristiques clés et les informations sémantiques du texte.
Compréhension Améliorée du Texte : Utilise le modèle de langage large T5XXL pour traiter l'entrée `t5xxl`, potentiellement en élargissant ou en affinant les descriptions textuelles pour fournir des informations sémantiques plus riches.
Fusion Multimodale : Combine les résultats de traitement de CLIP et T5XXL pour créer une représentation textuelle plus complète.
Contrôle de la Génération : Ajuste l'influence des invites textuelles sur la génération d'images via le paramètre de guidage, permettant aux utilisateurs de trouver un équilibre entre la liberté créative et le respect strict des invites.
Génération de Données Conditionnelles : Produit des données conditionnelles traitées, qui seront utilisées dans les processus de génération d'images ultérieurs pour s'assurer que les images générées correspondent aux descriptions textuelles.

## Entrées

| Nom du Paramètre | Type de Donnée | Fonction |
|------------------|----------------|----------|
| clip             | CLIP           | Entrée d'objet modèle CLIP, utilisée pour l'encodage et le traitement du texte, généralement utilisée avec DualCLIPLoader |
| clip_l           | STRING         | Entrée texte multi-lignes, entrez un texte similaire aux informations de balise pour l'encodage du modèle CLIP |
| t5xxl            | STRING         | Entrée texte multi-lignes, entrez des descriptions d'invites en langage naturel pour l'encodage du modèle T5XXL |
| guidance         | FLOAT          | Valeur flottante, utilisée pour guider le processus de génération ; des valeurs plus élevées augmentent la correspondance image-invite mais peuvent réduire la créativité |

## Sorties

| Nom du Paramètre | Type de Donnée | Fonction |
|------------------|----------------|----------|
| CONDITIONING     | Condition      | Contient des données conditionnelles (cond) pour les tâches de génération conditionnelle ultérieures |
