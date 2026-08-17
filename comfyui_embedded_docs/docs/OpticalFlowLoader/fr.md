# Charger le modèle de flux optique

## Aperçu

Charge un modèle de flux optique depuis le dossier `models/optical_flow/`. Actuellement, seul le format RAFT-large de torchvision est pris en charge, c'est-à-dire le modèle utilisé par le nœud VOIDWarpedNoise. ComfyUI ne télécharge pas automatiquement les poids du flux optique ; vous devez placer manuellement le fichier de checkpoint dans le répertoire `models/optical_flow/`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model_name` | Modèle de flux optique à charger. Les fichiers doivent être placés dans le dossier `optical_flow`. Aujourd'hui, seul `raft_large.pth` de torchvision est pris en charge. | COMBO | Oui | Liste des fichiers dans le dossier `models/optical_flow/` |

Le fichier sélectionné doit être un checkpoint RAFT-large de torchvision. Le nœud vérifie que le fichier contient les clés RAFT attendues (`feature_encoder.*`, `context_encoder.*`, et `update_block.*`) et lève une ValueError si le format n'est pas reconnu.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `OPTICAL_FLOW` | Le modèle de flux optique chargé, enveloppé dans un ModelPatcher pour être utilisé avec d'autres nœuds. | OPTICAL_FLOW |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/fr.md)

---
**Source fingerprint (SHA-256):** `5e79551545ad7ee2fd4856a47da29808a404342d1d5e57da0980058db6b11c3b`
