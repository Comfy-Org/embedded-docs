> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen2/fr.md)

Le nœud Rodin3D_Gen2 génère des ressources 3D en utilisant l'API Rodin. Il prend des images en entrée et les convertit en modèles 3D avec différents types de matériaux et nombres de polygones. Le nœud gère automatiquement l'intégralité du processus de génération, incluant la création de tâches, la vérification du statut et le téléchargement des fichiers.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | Oui | - | Images d'entrée à utiliser pour la génération du modèle 3D |
| `Seed` | INT | Non | 0-65535 | Valeur de graine aléatoire pour la génération (par défaut : 0) |
| `Material_Type` | COMBO | Non | "PBR"<br>"Shaded" | Type de matériau à appliquer au modèle 3D (par défaut : "PBR") |
| `Polygon_count` | COMBO | Non | "4K-Quad"<br>"8K-Quad"<br>"18K-Quad"<br>"50K-Quad"<br>"2K-Triangle"<br>"20K-Triangle"<br>"150K-Triangle"<br>"500K-Triangle" | Nombre de polygones cible pour le modèle 3D généré (par défaut : "500K-Triangle") |
| `TAPose` | BOOLEAN | Non | - | Indique s'il faut appliquer le traitement TAPose (par défaut : False) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | Chemin d'accès au fichier du modèle 3D généré |
