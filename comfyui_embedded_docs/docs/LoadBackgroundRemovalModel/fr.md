> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/fr.md)

Voici la traduction de la documentation du nœud ComfyUI :

## Aperçu

Charge un modèle de suppression d'arrière-plan à partir d'un fichier. Ce nœud prépare le modèle pour une utilisation dans la suppression des arrière-plans d'images.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `bg_removal_name` | STRING | Oui | Liste des fichiers de modèle disponibles | Le modèle utilisé pour supprimer les arrière-plans des images. Sélectionnez dans la liste des fichiers de modèle de suppression d'arrière-plan disponibles. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `bg_model` | BACKGROUND_REMOVAL | Le modèle de suppression d'arrière-plan chargé, prêt à être utilisé par d'autres nœuds pour le traitement des images. |