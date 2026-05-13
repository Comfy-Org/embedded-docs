> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI, en respectant vos règles :

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/en.md)

Le nœud Enregistrer les images et textes dans un dossier enregistre une liste d'images et leurs légendes textuelles correspondantes dans un dossier spécifié à l'intérieur du répertoire de sortie de ComfyUI. Pour chaque image enregistrée au format PNG, un fichier texte portant le même nom de base est créé pour stocker sa légende. Cela est utile pour créer des ensembles de données organisés d'images générées et de leurs descriptions.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `images` | IMAGE | Oui | - | Liste des images à enregistrer. |
| `texts` | STRING | Oui | - | Liste des légendes textuelles à enregistrer. |
| `folder_name` | STRING | Non | - | Nom du dossier dans lequel enregistrer les images (à l'intérieur du répertoire de sortie). (par défaut : "dataset") |
| `filename_prefix` | STRING | Non | - | Préfixe pour les noms de fichiers d'images enregistrés. (par défaut : "image") |

**Remarque :** Les entrées `images` et `texts` sont des listes. Le nœud s'attend à ce que le nombre de légendes textuelles corresponde au nombre d'images fournies. Chaque légende sera enregistrée dans un fichier `.txt` correspondant à son image associée.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| - | - | Ce nœud n'a aucune sortie. Il enregistre les fichiers directement dans le système de fichiers. |

---
**Source fingerprint (SHA-256):** `0c76f623e97b1502c850e0a59dc9edd7c241bcd823f5e32a8dcdd8b8160d2e44`
