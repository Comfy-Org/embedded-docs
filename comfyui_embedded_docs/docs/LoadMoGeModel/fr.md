> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMoGeModel/fr.md)

Voici la traduction en français de la documentation, en respectant toutes vos règles :

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMoGeModel/en.md)

## Aperçu

Charge un modèle MoGe (géométrie monoculaire) à partir d'un fichier et le prépare pour une utilisation dans des tâches d'estimation géométrique. Ce nœud lit un fichier de modèle depuis le dossier `geometry_estimation` et initialise le modèle MoGe avec ses poids entraînés.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model_name` | STRING | Oui | Liste des fichiers de modèle disponibles dans le dossier `geometry_estimation` | Le nom du fichier de modèle MoGe à charger. Sélectionnez parmi les fichiers de modèle disponibles dans votre installation ComfyUI. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `MOGE_MODEL` | MOGE_MODEL | L'instance du modèle MoGe chargée, prête à être utilisée dans des workflows d'estimation géométrique. |

---
**Source fingerprint (SHA-256):** `4707002565181ca17936ecf87ea8059630c97c44c17facfecd04053d9581b7d1`
