> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/fr.md)

Le nœud ModelPatchLoader charge des correctifs de modèles spécialisés depuis le dossier model_patches. Il détecte automatiquement le type de fichier de correctif et charge l'architecture de modèle appropriée, puis l'encapsule dans un ModelPatcher pour utilisation dans le flux de travail. Ce nœud prend en charge différents types de correctifs, y compris les blocs controlnet et les modèles d'incorporation de caractéristiques.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `name` | STRING | Oui | Tous les fichiers de correctifs de modèles disponibles dans le dossier model_patches | Le nom du fichier du correctif de modèle à charger depuis le répertoire model_patches |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `MODEL_PATCH` | MODEL_PATCH | Le correctif de modèle chargé, encapsulé dans un ModelPatcher pour utilisation dans le flux de travail |
