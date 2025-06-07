
**Fonction du nœud :** Le nœud `Save Image-Sauvegarder l'Image` est principalement utilisé pour enregistrer des images dans le dossier **output** de ComfyUI. Si vous souhaitez uniquement prévisualiser l'image pendant le processus intermédiaire au lieu de l'enregistrer, vous pouvez utiliser le nœud `Preview Image-Prévisualiser l'Image`.
Emplacement d'enregistrement par défaut : `ComfyUI/output/`

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `images` | `IMAGE` | Les images à sauvegarder. Ce paramètre est crucial car il contient directement les données d'image qui seront traitées et sauvegardées sur le disque. |
| `filename_prefix` | STRING   | Le préfixe du nom de fichier pour les images enregistrées dans le dossier `ComfyUI/output/`. La valeur par défaut est `ComfyUI`, mais elle peut être personnalisée. |

## Options du Menu Contextuel

Après la génération de l'image, un clic droit sur le menu correspondant fournit les options et fonctions spécifiques au nœud suivantes :

| Nom de l'Option | Fonction |
|-----------------|-----------|
| `Save Image-Sauvegarder l'Image` | Enregistrer l'image localement |
| `Copy Image-Copier l'Image` | Copier l'image dans le presse-papiers |
| `Open Image-Ouvrir l'Image` | Ouvrir l'image dans un nouvel onglet du navigateur |

Les images sauvegardées sont généralement au format PNG et incluent toutes les données de génération d'images. Si vous souhaitez utiliser le flux de travail correspondant pour la régénération, il suffit de charger l'image correspondante dans ComfyUI pour charger le flux de travail.
