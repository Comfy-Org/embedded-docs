# Charger le modèle de suppression d’arrière-plan

Charge un modèle de suppression d'arrière-plan à partir d'un fichier et le rend prêt à être utilisé par d'autres nœuds lors de la suppression d'arrière-plans d'images. Le fichier de modèle est sélectionné parmi les fichiers disponibles dans le dossier de suppression d'arrière-plan.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `bg_removal_name` | Le modèle utilisé pour supprimer les arrière-plans des images. | COMBO | Oui | Liste des fichiers de modèle disponibles (liste triée des fichiers dans le dossier background_removal) |

**Remarque :** Le nœud génère une erreur si le fichier sélectionné ne contient pas un modèle de suppression d'arrière-plan valide.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `bg_model` | Le modèle de suppression d'arrière-plan chargé, prêt à être utilisé par d'autres nœuds pour traiter des images. | BACKGROUND_REMOVAL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/fr.md)

---
**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`
