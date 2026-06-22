# Charger le modèle de suppression d’arrière-plan

Voici la traduction en français de la documentation, conformément à vos règles :

## Aperçu

Charge un modèle de suppression d'arrière-plan à partir d'un fichier. Ce nœud prépare le modèle pour une utilisation dans la suppression des arrière-plans des images.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `nom_du_modèle_de_suppression_arrière-plan` | Le modèle utilisé pour supprimer les arrière-plans des images. Sélectionnez dans la liste des fichiers de modèle de suppression d'arrière-plan disponibles. | STRING | Oui | Liste des fichiers de modèle disponibles |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `bg_model` | Le modèle de suppression d'arrière-plan chargé, prêt à être utilisé par d'autres nœuds pour le traitement des images. | BACKGROUND_REMOVAL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/fr.md)

---
**Source fingerprint (SHA-256):** `63a1ffb37ea8581e3ba29f7dc4f871612d7ec458e6d36f5e2244201941d48f9d`
