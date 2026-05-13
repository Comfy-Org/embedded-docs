> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen2/fr.md)

Voici la traduction en français de la documentation du nœud Rodin3D_Gen2, en respectant vos règles :

Le nœud Rodin3D_Gen2 génère des actifs 3D à l'aide de l'API Rodin. Il prend des images en entrée et les convertit en modèles 3D avec différents types de matériaux et nombres de polygones. Le nœud gère automatiquement l'ensemble du processus de génération, y compris la création de tâches, l'interrogation de l'état et le téléchargement des fichiers.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `Images` | IMAGE | Oui | - | Images d'entrée à utiliser pour la génération du modèle 3D |
| `Graine` | INT | Non | 0-65535 | Valeur de graine aléatoire pour la génération (par défaut : 0) |
| `Type_Matériau` | COMBO | Non | "PBR"<br>"Shaded" | Type de matériau à appliquer au modèle 3D (par défaut : "PBR") |
| `Nombre_Polygones` | COMBO | Non | "4K-Quad"<br>"8K-Quad"<br>"18K-Quad"<br>"50K-Quad"<br>"2K-Triangle"<br>"20K-Triangle"<br>"150K-Triangle"<br>"500K-Triangle" | Nombre de polygones cible pour le modèle 3D généré (par défaut : "500K-Triangle") |
| `PoseTAP` | BOOLEAN | Non | - | Indique s'il faut appliquer le traitement TAPose (par défaut : False) |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `GLB` | STRING | Chemin d'accès au fichier du modèle 3D généré (pour la rétrocompatibilité) |
| `GLB` | FILE3DGLB | Le modèle 3D généré au format GLB |

---
**Source fingerprint (SHA-256):** `940712a9a40f4cb07050f3ed7ac502469b30bd364f86bb42b9dd8bf63eb912a2`
