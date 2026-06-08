Le nœud Rodin 3D Detail génère des actifs 3D détaillés à l'aide de l'API Rodin. Il prend des images en entrée et les traite via le service Rodin pour créer des modèles 3D de haute qualité avec une géométrie et des matériaux détaillés. Le nœud gère l'ensemble du flux de travail, de la création de la tâche au téléchargement du fichier de modèle 3D final.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `Images` | Images d'entrée utilisées pour la génération du modèle 3D. Plusieurs images peuvent être fournies. | IMAGE | Oui | - |
| `Graine` | Valeur de graine aléatoire pour des résultats reproductibles | INT | Oui | - |
| `Type_Matériau` | Type de matériau à appliquer au modèle 3D | STRING | Oui | - |
| `Nombre_Polygones` | Nombre de polygones cible pour le modèle 3D généré. Détermine le niveau de qualité du maillage. | STRING | Oui | - |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `GLB` | Chemin d'accès au fichier du modèle 3D généré (uniquement pour la rétrocompatibilité) | STRING |
| `GLB` | Le modèle 3D généré au format GLB | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Detail/fr.md)

---
**Source fingerprint (SHA-256):** `ed9ed2c8a55ca80d18da88ee2703c66057a09beeac7163fc270d81a492417b0a`
