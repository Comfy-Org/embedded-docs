> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedCheckpointLoader/fr.md)

Le nœud CheckpointLoader est conçu pour des opérations de chargement avancées, permettant spécifiquement de charger des points de contrôle de modèle avec leurs configurations. Il facilite la récupération des composants du modèle nécessaires à l'initialisation et à l'exécution de modèles génératifs, y compris les configurations et les points de contrôle provenant de répertoires spécifiés.

## Entrées

| Paramètre | Type de données | Description |
|--------------|--------------|-------------|
| `config_name` | COMBO[STRING] | Spécifie le nom du fichier de configuration à utiliser. Ce paramètre est crucial pour déterminer les paramètres et réglages du modèle, influençant son comportement et ses performances. |
| `ckpt_name` | COMBO[STRING] | Indique le nom du fichier de point de contrôle à charger. Cela influence directement l'état du modèle en cours d'initialisation, impactant ses poids et biais initiaux. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-------------|-------------|
| `model` | MODEL | Représente le modèle principal chargé à partir du point de contrôle, prêt pour d'autres opérations ou inférences. |
| `clip` | CLIP | Fournit le composant du modèle CLIP, s'il est disponible et demandé, chargé à partir du point de contrôle. |
| `vae` | VAE | Délivre le composant du modèle VAE, s'il est disponible et demandé, chargé à partir du point de contrôle. |