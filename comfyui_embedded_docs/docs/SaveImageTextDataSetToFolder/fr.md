> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Oui | - | Liste des images à enregistrer. |
| `texts` | STRING | Oui | - | Liste des légendes textuelles à enregistrer. |
| `folder_name` | STRING | Non | - | Nom du dossier dans lequel enregistrer les images (à l'intérieur du répertoire de sortie). (par défaut : "dataset") |
| `filename_prefix` | STRING | Non | - | Préfixe pour les noms de fichiers des images enregistrées. (par défaut : "image") |

**Remarque :** Les entrées `images` et `texts` sont des listes. Le nœud s'attend à ce que le nombre de légendes textuelles corresponde au nombre d'images fournies. Chaque légende sera enregistrée dans un fichier `.txt` correspondant à son image associée.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| - | - | Ce nœud ne possède aucune sortie. Il enregistre les fichiers directement sur le système de fichiers. |
