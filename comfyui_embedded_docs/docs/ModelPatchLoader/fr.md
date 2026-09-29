# ModelPatchLoader

Le nœud ModelPatchLoader charge un fichier de patch de modèle depuis le dossier `model_patches` et le prépare pour utilisation dans un workflow. Il détecte automatiquement le type de patch contenu dans le fichier, construit l'architecture correspondante, charge les poids enregistrés et encapsule le tout dans un patcher de modèle afin qu'il puisse être appliqué à d'autres modèles. Il prend en charge de nombreux formats de patch spécialisés, notamment des branches ControlNet supplémentaires, des modèles d'embedding de caractéristiques, des adaptateurs, des modules de guidage animation/LLLite et des modules similaires.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `nom` | Le nom de fichier du patch de modèle à charger depuis le dossier `model_patches`. Sélectionnez l'un des fichiers de patch disponibles dans la liste. | COMBO | Oui | Liste générée dynamiquement de tous les fichiers de patch de modèle trouvés dans le dossier `model_patches` |

Remarque : Ce nœud est marqué comme expérimental. Le type de patch est détecté automatiquement à partir du contenu du fichier, aucune sélection manuelle du type n'est donc nécessaire. Le nœud lit les métadonnées du checkpoint et inspecte les clés de poids pour décider quelle architecture construire (par exemple Qwen Image block-wise ControlNet, Qwen Image 2.1 Fun ControlNet, Z-Image ControlNet, Wan Uni3C ControlNet, MiniMax H3 Fun ControlNet, SigLIP feature projection, Lightricks duration head, Anima LLLite, MultiTalk ou SUPIR). Les poids sont chargés avec le chargement sécurisé activé, et le modèle est placé sur le périphérique de déchargement à l'intérieur d'un `CoreModelPatcher` afin de pouvoir être appliqué ultérieurement à un autre modèle.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL_PATCH` | Le patch de modèle chargé, encapsulé dans un patcher de modèle, prêt à être appliqué à un modèle dans le workflow | MODEL_PATCH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/fr.md)

---
**Source fingerprint (SHA-256):** `83b607f3c2b4b210e6ca3d310ef974757a6caf3c83f1d2d5165f3b8248928e9c`
