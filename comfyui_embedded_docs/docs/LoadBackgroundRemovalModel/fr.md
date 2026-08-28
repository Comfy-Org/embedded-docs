# Charger le modèle de suppression d’arrière-plan

Charge un modèle de suppression d'arrière-plan à partir d'un fichier. Ce nœud prépare le modèle pour son utilisation dans la suppression des arrière-plans d'images.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `nom_du_modèle_de_suppression_arrière-plan` | Le modèle utilisé pour supprimer les arrière-plans des images. Sélectionnez parmi la liste des fichiers de modèles de suppression d'arrière-plan disponibles. | COMBO | Oui | Liste des fichiers de modèles disponibles (triés par ordre alphabétique) |

Remarque : Si le fichier sélectionné ne contient pas un modèle valide de suppression d'arrière-plan, le nœud génère une erreur d'exécution (RuntimeError).

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `modèle_bg` | Le modèle de suppression d'arrière-plan chargé, prêt à être utilisé par d'autres nœuds pour le traitement d'images. | BACKGROUND_REMOVAL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/fr.md)

---
**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`
