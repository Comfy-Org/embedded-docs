# Tripo P1 : Texte vers Modèle

Tripo P1 text-to-3D. Ce nœud génère un modèle 3D à partir d'une description textuelle à l'aide de l'API Tripo P1. Il est optimisé pour créer des maillages low-poly, prêts pour le jeu, avec une topologie stable, ce qui le rend adapté aux applications temps réel.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `output_mode` | Détermine si le modèle généré contient uniquement la géométrie ou également des textures de couleur/PBR. « Geometry only » renvoie un maillage non texturé. « Textured » ajoute des cartes de couleur/PBR et fait apparaître les options de texture ci-dessous. | DYNAMIC_COMBO | Oui | `"Geometry only"`<br>`"Textured"` |
| `prompt` | Description textuelle du modèle 3D que vous souhaitez générer. Jusqu'à 1024 caractères. Requis et ne peut pas être vide. | STRING | Oui | Jusqu'à 1024 caractères |
| `negative_prompt` | Description textuelle de ce que vous ne voulez pas dans le modèle généré. Jusqu'à 255 caractères. Par défaut : non défini. | STRING | Non | Jusqu'à 255 caractères |
| `image_seed` | Une valeur de graine utilisée pour contrôler l'aléatoire. Par défaut : 42. | INT | Non | 0 à 2147483647 |
| `face_limit` | Nombre cible de faces, 48-20000. -1 laisse Tripo choisir de manière adaptative. Par défaut : -1. | INT | Non | -1 à 20000 |
| `model_seed` | Une valeur de graine utilisée pour contrôler l'aléatoire. Par défaut : 42. | INT | Non | 0 à 2147483647 |
| `auto_size` | Met à l'échelle la sortie pour approximer des mètres réels. Par défaut : False. | BOOLEAN | Non | True / False |
| `export_uv` | Dépliage UV pendant la génération. Désactivez pour des exécutions plus rapides en géométrie seule. Par défaut : True. | BOOLEAN | Non | True / False |
| `compress_geometry` | Applique la compression géométrique meshopt (EXT_meshopt_compression). Fichiers plus petits, mais l'aperçu 3D de ComfyUI ne peut pas les afficher ; décompressez avant l'édition. Par défaut : False. | BOOLEAN | Non | True / False |

### Entrées Geometry only

Aucune entrée supplémentaire n'est disponible lorsque `output_mode` est défini sur `"Geometry only"`. Les paramètres liés aux textures ne sont pas envoyés à Tripo dans ce mode.

### Entrées Textured

Ces entrées n'apparaissent que lorsque `output_mode` est défini sur `"Textured"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `pbr` | Inclut les cartes PBR. Lorsque cette option est activée, la texture de base est également forcée. Par défaut : True. | BOOLEAN | Oui | True / False |
| `texture_quality` | Préréglage de qualité de texture. detailed = textures HD, extreme = textures 8K Ultra. Par défaut : "standard". | COMBO | Oui | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_seed` | Une valeur de graine pour la génération de texture, utilisée pour contrôler l'aléatoire. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Nom du fichier de modèle généré, conservé uniquement pour la compatibilité ascendante. | STRING |
| `model task_id` | ID de tâche unique pour la demande de génération du modèle. | MODEL_TASK_ID |
| `GLB` | Modèle 3D généré au format GLB. | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `53a5573384294612b912558436e82f3481717d2ba3d50b73f1e40c3065aff2a0`
