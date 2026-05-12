> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/fr.md)

Voici la traduction en français de la documentation, en respectant vos règles :

## Aperçu

Le nœud Supprimer l'arrière-plan utilise un modèle de suppression d'arrière-plan pour générer un masque qui sépare le sujet principal de l'arrière-plan d'une image d'entrée. Il prend une image et un modèle de suppression d'arrière-plan, puis produit un masque mettant en évidence le sujet principal.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Oui | N/A | Image d'entrée dont il faut supprimer l'arrière-plan |
| `bg_removal_model` | BACKGROUND_REMOVAL_MODEL | Oui | N/A | Modèle de suppression d'arrière-plan utilisé pour générer le masque |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `mask` | MASK | Masque de premier plan généré qui met en évidence le sujet principal de l'image d'entrée |