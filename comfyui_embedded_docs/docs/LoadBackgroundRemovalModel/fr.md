# Charger le modèle de suppression d’arrière-plan

Charge un modèle de suppression d'arrière-plan depuis un fichier. Ce nœud prépare le modèle afin qu'il puisse être utilisé par d'autres nœuds pour supprimer les arrière-plans des images.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `bg_removal_name` | Le modèle utilisé pour supprimer les arrière-plans des images. Sélectionnez-le dans la liste des fichiers de modèle de suppression d'arrière-plan disponibles. | COMBO | Oui | Liste des fichiers de modèle disponibles (triés par ordre alphabétique) |

Remarque : Si le fichier sélectionné ne contient pas un modèle de suppression d'arrière-plan valide, le nœud déclenche une RuntimeError.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `bg_model` | Le modèle de suppression d'arrière-plan chargé, prêt à être utilisé par d'autres nœuds pour traiter des images. | BACKGROUND_REMOVAL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/fr.md)

---
**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`
