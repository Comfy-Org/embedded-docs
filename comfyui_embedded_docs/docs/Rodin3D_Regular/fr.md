# Rodin 3D Générer - Génération Régulière

Le nœud **Rodin 3D Regular** génère des actifs 3D en utilisant l'API Rodin. Il prend des images en entrée et les traite via le service Rodin pour créer des modèles 3D. Le nœud gère l'ensemble du flux de travail, de la création de la tâche au téléchargement des fichiers de modèle 3D finaux.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `Images` | Images d'entrée utilisées pour la génération du modèle 3D. Plusieurs images peuvent être fournies. | IMAGE | Oui | - |
| `Graine` | Valeur de graine aléatoire pour des résultats reproductibles. | INT | Oui | - |
| `Type_Matériau` | Type de matériau à appliquer au modèle 3D. | STRING | Oui | - |
| `Nombre_Polygones` | Nombre de polygones cible pour le modèle 3D généré. Ce paramètre détermine le mode de qualité et la complexité du maillage. | STRING | Oui | - |


| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `3D Model Path` | Chemin d'accès au fichier du modèle 3D généré (conservé pour la rétrocompatibilité). | STRING |
| `GLB` | Le modèle 3D généré au format GLB. | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Regular/fr.md)

---
**Source fingerprint (SHA-256):** `f937be3aa579baf4407434839e741141d6bd63c09b7e0bdc49a9e92a10d7a130`
