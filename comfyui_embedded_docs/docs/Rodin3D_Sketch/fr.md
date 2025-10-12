> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Sketch/fr.md)

Ce nœud génère des ressources 3D en utilisant l'API Rodin. Il prend des images en entrée et les convertit en modèles 3D via un service externe. Le nœud gère l'intégralité du processus, de la création de la tâche au téléchargement des fichiers finaux du modèle 3D.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | Oui | - | Images d'entrée à convertir en modèles 3D |
| `Seed` | INT | Non | 0-65535 | Valeur de seed aléatoire pour la génération (par défaut : 0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | Chemin d'accès au fichier du modèle 3D généré |
