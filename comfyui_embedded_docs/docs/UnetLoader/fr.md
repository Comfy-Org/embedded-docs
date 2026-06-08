Le nœud UNETLoader est conçu pour charger des modèles U-Net par nom, facilitant ainsi l'utilisation d'architectures U-Net pré-entraînées au sein du système.

Ce nœud détectera les modèles situés dans le dossier `ComfyUI/models/diffusion_models`.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `nom_unet` | Spécifie le nom du modèle U-Net à charger. Ce nom est utilisé pour localiser le modèle dans une structure de répertoires prédéfinie, permettant le chargement dynamique de différents modèles U-Net. | COMBO[STRING] |
| `dtype_poids` | 🚧  fp8_e4m3fn fp9_e5m2 | ... |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `model` | Renvoie le modèle U-Net chargé, permettant son utilisation pour un traitement ultérieur ou une inférence au sein du système. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNETLoader/fr.md)
