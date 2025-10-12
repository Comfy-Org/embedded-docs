> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGLB/fr.md)

Le nœud SaveGLB sauvegarde les données de maillage 3D au format GLB, un format courant pour les modèles 3D. Il prend des données de maillage en entrée et les exporte vers le répertoire de sortie avec le préfixe de nom de fichier spécifié. Le nœud peut sauvegarder plusieurs maillages si l'entrée contient plusieurs objets de maillage, et il ajoute automatiquement des métadonnées aux fichiers lorsque cette fonctionnalité est activée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `mesh` | MESH | Oui | - | Les données de maillage 3D à sauvegarder en tant que fichier GLB |
| `filename_prefix` | STRING | Non | - | Le préfixe pour le nom de fichier de sortie (par défaut : "mesh/ComfyUI") |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `ui` | UI | Affiche les fichiers GLB sauvegardés dans l'interface utilisateur avec les informations de nom de fichier et de sous-dossier |