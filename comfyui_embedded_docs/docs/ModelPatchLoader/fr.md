> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/fr.md)

Le nœud ModelPatchLoader charge des correctifs de modèle spécialisés depuis le dossier model_patches. Il détecte automatiquement le type de fichier de correctif et charge l'architecture de modèle appropriée, puis l'encapsule dans un ModelPatcher pour une utilisation dans le workflow. Ce nœud prend en charge différents types de correctifs, notamment les blocs controlnet, les modèles d'intégration de caractéristiques et d'autres architectures spécialisées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `nom` | STRING | Oui | Tous les fichiers de correctifs de modèle disponibles dans le dossier model_patches | Le nom du fichier de correctif de modèle à charger depuis le répertoire model_patches |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `MODEL_PATCH` | MODEL_PATCH | Le correctif de modèle chargé, encapsulé dans un ModelPatcher pour une utilisation dans le workflow |

---
**Source fingerprint (SHA-256):** `e394e165cf416019ed53d9fde42d97c3c9b9f9afd843b12371a624467a4841bf`
