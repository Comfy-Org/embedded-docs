> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/fr.md)

Voici la traduction en français de la documentation du nœud OpticalFlowLoader :

## Aperçu

Charge un modèle de flux optique depuis le dossier `models/optical_flow/`. Actuellement, seul le format RAFT-large de torchvision est pris en charge, qui est le modèle utilisé par le nœud VOIDWarpedNoise. ComfyUI ne télécharge pas automatiquement les poids du flux optique ; vous devez placer manuellement le fichier de point de contrôle dans le répertoire `models/optical_flow/`.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model_name` | STRING | Oui | Liste des fichiers dans le dossier `models/optical_flow/` | Modèle de flux optique à charger. Les fichiers doivent être placés dans le dossier `optical_flow`. Actuellement, seul le fichier `raft_large.pth` de torchvision est pris en charge. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `OPTICAL_FLOW` | MODEL | Le modèle de flux optique chargé, encapsulé dans un ModelPatcher pour une utilisation avec d'autres nœuds. |