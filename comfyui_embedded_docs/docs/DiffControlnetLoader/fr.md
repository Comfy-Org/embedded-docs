Ce nœud détecte les modèles situés dans le dossier `ComfyUI/models/controlnet` et lit également les modèles des chemins supplémentaires que vous avez configurés dans le fichier extra_model_paths.yaml. Parfois, vous devrez **rafraîchir l'interface ComfyUI** pour qu'elle puisse lire les fichiers de modèle dans le dossier correspondant.

Le nœud DiffControlNetLoader est conçu pour charger des réseaux de contrôle différentiel, qui sont des modèles spécialisés pouvant modifier le comportement d'un autre modèle en fonction des spécifications du réseau de contrôle. Ce nœud permet l'ajustement dynamique des comportements du modèle en appliquant des réseaux de contrôle différentiel, facilitant la création de sorties de modèle personnalisées.

## Entrées

| Champ               | Comfy dtype       | Description                                                                                 |
|---------------------|-------------------|---------------------------------------------------------------------------------------------|
| `model`             | `MODEL`           | Le modèle de base auquel le réseau de contrôle différentiel sera appliqué, permettant la personnalisation du comportement du modèle. |
| `control_net_name`  | `COMBO[STRING]`    | Identifie le réseau de contrôle différentiel spécifique à charger et à appliquer au modèle de base pour modifier son comportement. |

## Sorties

| Champ          | Comfy dtype   | Description                                                                   |
|----------------|---------------|-------------------------------------------------------------------------------|
| `control_net`  | `CONTROL_NET` | Un réseau de contrôle différentiel qui a été chargé et est prêt à être appliqué à un modèle de base pour la modification du comportement. |
