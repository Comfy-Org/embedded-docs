> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageMergeTileList/fr.md)

Ce nœud prend une liste de tuiles d'image et les fusionne pour reconstituer une seule image plus grande. Il est conçu pour reconstruire une image qui avait été précédemment découpée en une grille de tuiles se chevauchant, en utilisant une technique de fusion pondérée pour obtenir un résultat final sans couture.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image_list` | IMAGE | Oui | N/A | Une liste de tuiles d'image à fusionner. La première tuile de la liste est utilisée pour déterminer les dimensions et le type de données des tuiles pour l'ensemble du processus. |
| `final_width` | INT | Non | 64 - 32768 | La largeur de l'image fusionnée finale en pixels (par défaut : 1024). |
| `final_height` | INT | Non | 64 - 32768 | La hauteur de l'image fusionnée finale en pixels (par défaut : 1024). |
| `overlap` | INT | Non | 0 - 4096 | La quantité de chevauchement entre les tuiles adjacentes en pixels. Une valeur supérieure à 0 permet un effet de fusion doux au niveau des jointures des tuiles (par défaut : 128). |

**Note :** `image_list` est une liste d'entrées dynamique. Le nœud traitera les tuiles dans l'ordre où elles sont fournies, jusqu'au nombre nécessaire pour remplir la grille définie par `final_width`, `final_height` et les dimensions de la première tuile. Si la liste contient plus de tuiles que nécessaire, les tuiles supplémentaires sont ignorées.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image fusionnée finale, reconstituée à partir des tuiles d'entrée. |