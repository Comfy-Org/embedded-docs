> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/fr.md)

Le nœud CheckpointLoader charge un point de contrôle de modèle pré-entraîné ainsi que son fichier de configuration. Il prend en entrée un fichier de configuration et un fichier de point de contrôle, puis retourne les composants du modèle chargé, notamment le modèle principal, le modèle CLIP et le modèle VAE, pour une utilisation dans le workflow.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `nom_config` | STRING | Oui | Fichiers de configuration disponibles | Le fichier de configuration qui définit l'architecture et les paramètres du modèle |
| `nom_ckpt` | STRING | Oui | Fichiers de point de contrôle disponibles | Le fichier de point de contrôle contenant les poids et paramètres du modèle entraîné |

**Remarque :** Ce nœud nécessite la sélection d'un fichier de configuration et d'un fichier de point de contrôle. Le fichier de configuration doit correspondre à l'architecture du fichier de point de contrôle chargé.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `MODEL` | MODEL | Le composant du modèle principal chargé, prêt pour l'inférence |
| `CLIP` | CLIP | Le composant du modèle CLIP chargé pour l'encodage de texte |
| `VAE` | VAE | Le composant du modèle VAE chargé pour l'encodage et le décodage d'images |

**Remarque importante :** Ce nœud a été marqué comme obsolète et pourrait être supprimé dans les versions futures. Pour les nouveaux workflows, envisagez d'utiliser des nœuds de chargement alternatifs.

---
**Source fingerprint (SHA-256):** `9977bda5e124a9d10566839cbee868c74fab120c454141f27ce145efa60105e9`
