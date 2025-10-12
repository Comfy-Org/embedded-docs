> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/fr.md)

Le nœud CheckpointLoader charge un point de contrôle de modèle pré-entraîné ainsi que son fichier de configuration. Il prend en entrée un fichier de configuration et un fichier de point de contrôle, et renvoie les composants du modèle chargé, incluant le modèle principal, le modèle CLIP et le modèle VAE, pour une utilisation dans le flux de travail.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `nom_config` | STRING | COMBO | - | Fichiers de configuration disponibles | Le fichier de configuration qui définit l'architecture et les paramètres du modèle |
| `nom_ckpt` | STRING | COMBO | - | Fichiers de point de contrôle disponibles | Le fichier de point de contrôle contenant les poids et paramètres entraînés du modèle |

**Note :** Ce nœud nécessite la sélection à la fois d'un fichier de configuration et d'un fichier de point de contrôle. Le fichier de configuration doit correspondre à l'architecture du fichier de point de contrôle chargé.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `MODEL` | MODEL | Le composant de modèle principal chargé, prêt pour l'inférence |
| `CLIP` | CLIP | Le composant de modèle CLIP chargé pour l'encodage de texte |
| `VAE` | VAE | Le composant de modèle VAE chargé pour l'encodage et le décodage d'image |

**Note importante :** Ce nœud a été marqué comme obsolète et pourrait être supprimé dans les versions futures. Envisagez d'utiliser des nœuds de chargement alternatifs pour les nouveaux flux de travail.
