# ModelPatchLoader

Le nœud ModelPatchLoader charge un fichier de patch de modèle depuis le dossier `model_patches` et le prépare pour une utilisation dans un flux de travail. Il détecte automatiquement le type de patch contenu dans le fichier, construit l'architecture correspondante, charge les poids enregistrés et encapsule le tout dans un patcheur de modèle afin de pouvoir l'appliquer à d'autres modèles. Il prend en charge de nombreux formats de patch spécialisés, notamment des branches ControlNet supplémentaires, des modèles d'intégration de caractéristiques, des adaptateurs, des modules de guidage d'animation/LLLite et des modules similaires.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `name` | Le nom de fichier du patch de modèle à charger depuis le dossier `model_patches`. Sélectionnez l'un des fichiers de patch disponibles dans la liste. | COMBO | Oui | Liste générée dynamiquement de tous les fichiers de patch de modèle trouvés dans le dossier `model_patches` |

Remarque : Ce nœud est marqué comme expérimental. Le type de patch est détecté automatiquement à partir du contenu du fichier, aucune sélection manuelle du type n'est donc requise. Le nœud lit les métadonnées du checkpoint et inspecte les clés de poids pour déterminer l'architecture à construire (par exemple Qwen Image block-wise ControlNet, Z-Image ControlNet, Wan Uni3C ControlNet, MiniMax H3 Fun ControlNet, projection de caractéristiques SigLIP, tête de durée Lightricks, Anima LLLite, MultiTalk ou SUPIR). Les poids sont chargés avec le chargement sécurisé activé, et le modèle est placé sur le périphérique de déchargement à l'intérieur d'un `CoreModelPatcher`, afin de pouvoir être appliqué ultérieurement à un autre modèle.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL_PATCH` | Le patch de modèle chargé, encapsulé dans un patcheur de modèle, prêt à être appliqué à un modèle dans le flux de travail | MODEL_PATCH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/fr.md)

---
**Source fingerprint (SHA-256):** `069f40b1f108ecd74fc58c12aa2f74edff07f743aa1ed6352ff7bcf0c39341d4`
