# Charger le modèle de flux optique

Charge un modèle de flux optique depuis le dossier `models/optical_flow/`. Actuellement, seul le format RAFT-large de torchvision est pris en charge, qui est le modèle utilisé par le nœud VOIDWarpedNoise. ComfyUI ne télécharge pas automatiquement les poids du flux optique ; vous devez placer manuellement le fichier checkpoint dans le répertoire `models/optical_flow/`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model_name` | Modèle de flux optique à charger. Les fichiers doivent être placés dans le dossier `optical_flow`. Aujourd'hui, seul le `raft_large.pth` de torchvision est pris en charge. | COMBO | Oui | Liste des fichiers dans le dossier `models/optical_flow/` |

Remarque : Le checkpoint sélectionné doit être un state dict RAFT-large de torchvision contenant des clés préfixées par `feature_encoder.`, `context_encoder.` et `update_block.`. Si le fichier ne correspond pas à ce format, le nœud lève une ValueError.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `OPTICAL_FLOW` | Le modèle de flux optique chargé, réglé sur le mode évaluation et la précision float32, enveloppé dans un ModelPatcher pour utilisation avec d'autres nœuds. | OPTICAL_FLOW |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/fr.md)

---
**Source fingerprint (SHA-256):** `5e79551545ad7ee2fd4856a47da29808a404342d1d5e57da0980058db6b11c3b`
