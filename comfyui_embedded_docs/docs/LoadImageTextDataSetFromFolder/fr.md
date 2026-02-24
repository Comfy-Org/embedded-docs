> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/fr.md)

Ce nœud charge un jeu de données d'images et de leurs légendes textuelles correspondantes à partir d'un dossier spécifié. Il recherche les fichiers image et cherche automatiquement les fichiers `.txt` correspondants portant le même nom de base pour les utiliser comme légendes. Le nœud prend également en charge une structure de dossiers spécifique où les sous-dossiers peuvent être nommés avec un préfixe numérique (comme `10_nom_dossier`) pour indiquer que les images qu'ils contiennent doivent être répétées plusieurs fois en sortie.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `folder` | COMBO | Oui | *Chargé dynamiquement depuis `folder_paths.get_input_subfolders()`* | Le dossier depuis lequel charger les images. Les options disponibles sont les sous-répertoires du répertoire d'entrée de ComfyUI. |

**Remarque :** Le nœud s'attend à une structure de fichiers spécifique. Pour chaque fichier image (`.png`, `.jpg`, `.jpeg`, `.webp`), il cherchera un fichier `.txt` portant le même nom pour l'utiliser comme légende. Si un fichier de légende n'est pas trouvé, une chaîne vide est utilisée. Le nœud prend également en charge une structure spéciale où le nom d'un sous-dossier commence par un nombre et un tiret bas (par exemple, `5_chats`), ce qui entraînera la répétition de toutes les images contenues dans ce sous-dossier autant de fois dans la liste de sortie finale.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `images` | IMAGE | Une liste de tenseurs d'images chargées. |
| `texts` | STRING | Une liste de légendes textuelles correspondant à chaque image chargée. |
