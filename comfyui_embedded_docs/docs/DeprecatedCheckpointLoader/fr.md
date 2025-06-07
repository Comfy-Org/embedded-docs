Le nœud CheckpointLoader est conçu pour des opérations de chargement avancées, spécifiquement pour charger les checkpoints de modèle avec leurs configurations. Il facilite la récupération des composants du modèle nécessaires pour initialiser et exécuter des modèles génératifs, y compris les configurations et checkpoints à partir de répertoires spécifiés.

## Entrées

| Paramètre    | Data Type | Description |
|--------------|--------------|-------------|
| `config_name` | COMBO[STRING] | Spécifie le nom du fichier de configuration à utiliser. Cela est crucial pour déterminer les paramètres et réglages du modèle, affectant le comportement et la performance du modèle. |
| `ckpt_name`  | COMBO[STRING] | Indique le nom du fichier de checkpoint à charger. Cela influence directement l'état du modèle en cours d'initialisation, impactant ses poids et biais initiaux. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `model`   | MODEL     | Représente le modèle principal chargé à partir du checkpoint, prêt pour des opérations ultérieures ou une inférence. |
| `clip`    | CLIP      | Fournit le composant modèle CLIP, si disponible et demandé, chargé à partir du checkpoint. |
| `vae`     | VAE       | Livre le composant modèle VAE, si disponible et demandé, chargé à partir du checkpoint. |
