Ce nœud détecte les modèles situés dans le dossier `ComfyUI/models/loras`, et lit également les modèles depuis les chemins supplémentaires configurés dans le fichier extra_model_paths.yaml. Il peut être nécessaire d'**actualiser l'interface ComfyUI** pour lui permettre de lire les fichiers de modèles depuis le dossier correspondant.

Ce nœud est spécialisé dans le chargement d'un modèle LoRA sans nécessiter de modèle CLIP, en se concentrant sur l'amélioration ou la modification d'un modèle donné en fonction des paramètres LoRA. Il permet un ajustement dynamique de la puissance du modèle via les paramètres LoRA, facilitant un contrôle fin du comportement du modèle.

## Entrées

| Champ | Description | Type Comfy |
| --- | --- | --- |
| `model` | Le modèle de base à modifier, auquel les ajustements LoRA seront appliqués. | `MODEL` |
| `lora_name` | Le nom du fichier LoRA à charger, spécifiant les ajustements à appliquer au modèle. | `COMBO[STRING]` |
| `strength_model` | Détermine l'intensité des ajustements LoRA, les valeurs plus élevées indiquant des modifications plus fortes. | `FLOAT` |

## Sorties

| Champ | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec les ajustements LoRA appliqués, reflétant les changements de comportement ou de capacités du modèle. | `MODEL` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderModelOnly/fr.md)
