# Charger le modèle ControlNet (diff)

Ce nœud détecte les modèles situés dans le dossier `ComfyUI/models/controlnet`, et lit également les modèles depuis les chemins supplémentaires configurés dans le fichier extra_model_paths.yaml. Il peut parfois être nécessaire de **rafraîchir l'interface ComfyUI** pour lui permettre de lire les fichiers de modèles depuis le dossier correspondant.

Le nœud DiffControlNetLoader est conçu pour charger des réseaux de contrôle différentiels, qui sont des modèles spécialisés capables de modifier le comportement d'un autre modèle en fonction de spécifications de réseau de contrôle. Ce nœud permet l'ajustement dynamique des comportements du modèle en appliquant des réseaux de contrôle différentiels, facilitant ainsi la création de sorties de modèle personnalisées.

## Entrées

| Champ | Description | Type Comfy |
| --- | --- | --- |
| `modèle` | Le modèle de base auquel le réseau de contrôle différentiel sera appliqué, permettant la personnalisation du comportement du modèle. | `MODEL` |
| `nom_control_net` | Identifie le réseau de contrôle différentiel spécifique à charger et à appliquer au modèle de base pour modifier son comportement. | `COMBO[STRING]` |

## Sorties

| Champ | Description | Type Comfy |
| --- | --- | --- |
| `control_net` | Un réseau de contrôle différentiel qui a été chargé et est prêt à être appliqué à un modèle de base pour une modification de comportement. | `CONTROL_NET` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffControlNetLoader/fr.md)
