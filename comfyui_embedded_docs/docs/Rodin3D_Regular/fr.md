> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Regular/fr.md)

Le nœud **Rodin 3D Regular** génère des actifs 3D en utilisant l'API Rodin. Il prend des images en entrée et les traite via le service Rodin pour créer des modèles 3D. Le nœud gère l'ensemble du flux de travail, de la création de la tâche au téléchargement des fichiers de modèle 3D finaux.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `Images` | IMAGE | Oui | - | Images d'entrée utilisées pour la génération du modèle 3D. Plusieurs images peuvent être fournies. |
| `Seed` | INT | Oui | - | Valeur de graine aléatoire pour des résultats reproductibles. |
| `Material_Type` | STRING | Oui | - | Type de matériau à appliquer au modèle 3D. |
| `Polygon_count` | STRING | Oui | - | Nombre de polygones cible pour le modèle 3D généré. Ce paramètre détermine le mode de qualité et la complexité du maillage. |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `3D Model Path` | STRING | Chemin d'accès au fichier du modèle 3D généré (conservé pour la rétrocompatibilité). |
| `GLB` | FILE3DGLB | Le modèle 3D généré au format GLB. |

---
**Source fingerprint (SHA-256):** `f937be3aa579baf4407434839e741141d6bd63c09b7e0bdc49a9e92a10d7a130`
