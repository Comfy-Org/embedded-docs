# Tripo : Modèle de texture

Le nœud TripoTextureNode génère des modèles 3D texturés à l'aide de l'API Tripo. Il prend un ID de tâche de modèle et applique la génération de textures avec diverses options, notamment les matériaux PBR, les paramètres de qualité de texture, les méthodes d'alignement et un guide textuel facultatif. Le nœud communique avec l'API Tripo pour traiter la demande de génération de textures et renvoie le fichier de modèle résultant ainsi que l'ID de tâche.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_task_id` | L'ID de tâche du modèle auquel appliquer les textures | MODEL_TASK_ID | Oui | - |
| `texture` | Indique s'il faut générer des textures (défaut : True) | BOOLEAN | Non | - |
| `pbr` | Indique s'il faut générer des matériaux PBR (Rendu physiquement réaliste) (défaut : True) | BOOLEAN | Non | - |
| `texture_seed` | Graine aléatoire pour la génération de textures (défaut : 42) | INT | Non | - |
| `texture_quality` | Niveau de qualité pour la génération de textures (défaut : "standard"). L'option "detailed" coûte 0,20 $ US, tandis que "standard" coûte 0,10 $ US. | COMBO | Non | "standard"<br>"detailed" |
| `texture_alignment` | Méthode d'alignement des textures (défaut : "original_image"). "original_image" aligne les textures sur l'image d'entrée d'origine, tandis que "geometry" les aligne sur la géométrie 3D. | COMBO | Non | "original_image"<br>"geometry" |
| `texture_prompt` | Guide textuel facultatif pour la texturation. Requis en pratique pour les modèles importés (Tripo : Import Model), qui ne comportent aucune image source pour en déduire les couleurs. (zone de texte multiligne, défaut : chaîne vide) | STRING | Non | - |

*Remarque : Ce nœud nécessite des jetons d'authentification et des clés API, qui sont gérés automatiquement par le système.*

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Le fichier modèle généré avec les textures appliquées (uniquement pour la rétrocompatibilité) | STRING |
| `model task_id` | L'ID de tâche pour suivre le processus de génération de textures | MODEL_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB avec les textures appliquées | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/fr.md)

---
**Source fingerprint (SHA-256):** `a0157b7fa2bb94d174ea5893d7389885180876794032a510642586e310ba30d4`
