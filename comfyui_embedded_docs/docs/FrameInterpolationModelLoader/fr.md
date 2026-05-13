> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/fr.md)

Voici la traduction en français de la documentation du nœud FrameInterpolationModelLoader :

---

## Aperçu

Ce nœud charge un modèle d'interpolation d'images à partir d'un fichier et le prépare pour une utilisation dans le workflow. Il détecte automatiquement le type de modèle (FILM ou RIFE) et le configure pour des performances optimales sur votre matériel.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model_name` | STRING | Oui | Liste des fichiers de modèles dans le dossier `frame_interpolation` | Sélectionnez un modèle d'interpolation d'images à charger. Les modèles doivent être placés dans le dossier 'frame_interpolation'. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `FRAME_INTERPOLATION_MODEL` | MODEL | Le modèle d'interpolation d'images chargé et configuré, prêt à être utilisé dans d'autres nœuds. |

---
**Source fingerprint (SHA-256):** `497c20d5123bcbfd321dc4a659250ce3e0903e55c3a0274d3ed45710d75573d9`
