Le nœud CheckpointSave est conçu pour sauvegarder l'état de divers composants de modèle, y compris les modèles, CLIP, et VAE, dans un fichier de point de contrôle. Cette fonctionnalité est cruciale pour préserver la progression de l'entraînement ou la configuration des modèles pour une utilisation ou un partage ultérieur.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|----------------|-------------|
| `model`   | MODEL          | Le paramètre modèle représente le modèle principal dont l'état doit être sauvegardé. Il est essentiel pour capturer l'état actuel du modèle pour une restauration ou une analyse future. |
| `clip`    | CLIP           | Le paramètre clip est destiné au modèle CLIP associé au modèle principal, permettant de sauvegarder son état aux côtés du modèle principal. |
| `vae`     | VAE            | Le paramètre vae est pour le modèle Autoencodeur Variationnel (VAE), permettant de sauvegarder son état pour une utilisation ou une analyse future aux côtés du modèle principal et du CLIP. |
| `filename_prefix` | STRING | Ce paramètre spécifie le préfixe pour le nom de fichier sous lequel le point de contrôle sera sauvegardé, fournissant un moyen d'organiser et d'identifier les points de contrôle sauvegardés. |

## Sorties

Ce nœud produira un fichier de point de contrôle, et le chemin de sortie correspondant est le répertoire `output/checkpoints/`
