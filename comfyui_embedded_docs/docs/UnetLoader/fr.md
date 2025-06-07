
Le nœud UNETLoader est conçu pour charger des modèles U-Net par nom, facilitant l'utilisation des architectures U-Net pré-entraînées au sein du système.

## Entrées - Guide du Chargeur UNET | Charger le Modèle de Diffusion

| Paramètre   | Data Type | Description |
|-------------|--------------|-------------|
| `unet_name` | COMBO[STRING] | Spécifie le nom du modèle U-Net à charger. Ce nom est utilisé pour localiser le modèle dans une structure de répertoire prédéfinie, permettant le chargement dynamique de différents modèles U-Net. |
| `weight_dtype` | ... | 🚧  fp8_e4m3fn fp9_e5m2  |

## Sorties  - Guide du Chargeur UNET | Charger le Modèle de Diffusion

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `model`   | MODEL     | Retourne le modèle U-Net chargé, permettant son utilisation pour un traitement ou une inférence ultérieure au sein du système. |

## Exemple de Flux de Travail du Modèle de Diffusion | Guide du Chargeur UNET

1. Installez les modèles UNET
2. Téléchargez le fichier de flux de travail
3. Importez le flux de travail dans ComfyUI
4. Choisissez le modèle UNET et exécutez le flux de travail
