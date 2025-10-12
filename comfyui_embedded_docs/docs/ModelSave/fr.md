> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/fr.md)

Le nœud ModelSave permet de sauvegarder des modèles entraînés ou modifiés dans le stockage de votre ordinateur. Il prend un modèle en entrée et l'écrit dans un fichier portant le nom que vous avez spécifié. Cela vous permet de préserver votre travail et de réutiliser les modèles dans de futurs projets.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle à sauvegarder sur le disque |
| `préfixe_fichier` | STRING | Oui | - | Le préfixe du nom de fichier et du chemin pour le fichier de modèle sauvegardé (par défaut : "diffusion_models/ComfyUI") |
| `prompt` | PROMPT | Non | - | Informations du prompt du workflow (fournies automatiquement) |
| `extra_pnginfo` | EXTRA_PNGINFO | Non | - | Métadonnées supplémentaires du workflow (fournies automatiquement) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| *Aucune* | - | Ce nœud ne retourne aucune valeur de sortie |
