# Tripo P1 : Image vers Modèle

Tripo P1: Image to Model convertit une seule image 2D en un modèle 3D à l'aide de l'API Tripo P1. Il est optimisé pour générer des maillages low-poly, prêts pour le jeu, et vous permet de choisir entre un maillage uniquement géométrique ou un modèle texturé avec des cartes PBR. Le modèle final est renvoyé sous forme de fichier GLB.

## Entrées

### Entrées communes

Ces paramètres sont toujours disponibles.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `output_mode` | Choisit le type de résultat. « Geometry only » renvoie un maillage non texturé ; « Textured » ajoute des cartes de couleur/PBR et révèle des paramètres de texture supplémentaires. | DYNAMIC_COMBO | Oui | `"Geometry only"`<br>`"Textured"` |
| `image` | L'image 2D source utilisée pour générer le modèle 3D. Une seule image est requise ; le nœud lève une erreur si aucune n'est fournie. | IMAGE | Oui | - |
| `enable_image_autofix` | Pré-traite l'image d'entrée pour une meilleure qualité de génération. (par défaut : False) | BOOLEAN | Non | True<br>False |
| `face_limit` | Nombre cible de faces, 48 à 20000. -1 laisse Tripo choisir de manière adaptative. (par défaut : -1) | INT | Non | -1 à 20000 |
| `model_seed` | Graine utilisée pour la génération de la géométrie afin que les résultats puissent être reproduits. (par défaut : 42) | INT | Non | 0 à 2147483647 |
| `auto_size` | Met à l'échelle la sortie pour approximer des dimensions réelles en mètres. (par défaut : False) | BOOLEAN | Non | True<br>False |
| `export_uv` | Dépliage UV pendant la génération. Désactivez cette option pour des exécutions uniquement géométriques plus rapides. (par défaut : True) | BOOLEAN | Non | True<br>False |
| `compress_geometry` | Applique la compression géométrique meshopt (EXT_meshopt_compression). Fichiers plus petits, mais l'aperçu 3D de ComfyUI ne peut pas les afficher ; décompressez-les avant l'édition. (par défaut : False) | BOOLEAN | Non | True<br>False |

### Entrées Geometry only

Aucun paramètre supplémentaire. La sortie est un maillage non texturé.

### Entrées Textured

Ces paramètres apparaissent lorsque `output_mode` est défini sur « Textured ».

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `pbr` | Inclut les cartes PBR. Lorsque cette option est activée, la texture de base est également activée de force. (par défaut : True) | BOOLEAN | Oui | True<br>False |
| `texture_quality` | detailed = textures HD, extreme = textures Ultra 8K. (par défaut : "standard") | COMBO | Oui | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | Priorise la fidélité visuelle à l'image source, ou l'alignement sur la géométrie du maillage. (par défaut : "original_image") | COMBO | Oui | `"original_image"`<br>`"geometry"` |
| `orientation` | Fait pivoter la sortie pour correspondre à l'image source. S'applique uniquement en mode texturé. (par défaut : "default") | COMBO | Oui | `"default"`<br>`"align_image"` |
| `texture_seed` | Graine utilisée pour la génération de texture afin que les résultats texturés puissent être reproduits. (par défaut : 42) | INT | Oui | 0 à 2147483647 |

Remarque : lorsque `output_mode` est « Geometry only », la texturation est désactivée pour la requête. En mode « Textured », une texture de couleur est toujours demandée ; désactiver `pbr` supprime les cartes PBR mais conserve la texture de couleur de base, tandis qu'activer `pbr` force aussi l'activation de la texture de base. `texture_alignment` et `orientation` ne sont disponibles qu'en mode « Textured ».

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Une chaîne contenant le nom du fichier de modèle généré (`<task_id>.glb`). Conservé uniquement pour la compatibilité ascendante. | STRING |
| `model task_id` | L'ID unique de tâche renvoyé par l'API Tripo pour la tâche de génération terminée. | MODEL_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB. | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `1369da2ef732556896bce3415e7b99023f310544b8077ea4c6b1730bec59ee99`
