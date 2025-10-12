> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Smooth/fr.md)

Le nœud Rodin 3D Smooth génère des actifs 3D en utilisant l'API Rodin en traitant des images d'entrée et en les convertissant en modèles 3D lissés. Il prend plusieurs images en entrée et produit un fichier de modèle 3D téléchargeable. Le nœud gère l'intégralité du processus de génération, incluant la création de tâches, la vérification du statut et le téléchargement des fichiers automatiquement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | Oui | - | Images d'entrée à utiliser pour la génération du modèle 3D |
| `Seed` | INT | Oui | - | Valeur de seed aléatoire pour la cohérence de la génération |
| `Material_Type` | STRING | Oui | - | Type de matériau à appliquer au modèle 3D |
| `Polygon_count` | STRING | Oui | - | Nombre de polygones cible pour le modèle 3D généré |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | Chemin d'accès au fichier du modèle 3D téléchargé |
