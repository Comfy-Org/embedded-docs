# ModelPatchLoader

Le nœud ModelPatchLoader charge des patches de modèle spécialisés depuis le dossier `model_patches`. Il détecte automatiquement le type de fichier de patch et charge l'architecture de modèle appropriée, puis l'enveloppe dans un `ModelPatcher` pour utilisation dans le flux de travail. Ce nœud prend en charge différents types de patches, notamment les blocs ControlNet, les modèles d'intégration de caractéristiques (feature embedder) et d'autres architectures spécialisées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `name` | Le nom du fichier du patch de modèle à charger depuis le répertoire `model_patches`. | STRING | Oui | Tous les fichiers de patch de modèle disponibles dans le dossier `model_patches`. |

Remarque : Ce nœud est marqué comme expérimental dans ComfyUI. Le type de patch est détecté automatiquement à partir du contenu du fichier, un seul nœud peut donc gérer plusieurs types de patches.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL_PATCH` | Le patch de modèle chargé, enveloppé dans un `ModelPatcher` pour utilisation dans le flux de travail. | MODEL_PATCH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/fr.md)

---
**Source fingerprint (SHA-256):** `7f5225521b82b39b85183ccc7957fc4172e64aed9289f66d53969ea4a2e81b7f`
