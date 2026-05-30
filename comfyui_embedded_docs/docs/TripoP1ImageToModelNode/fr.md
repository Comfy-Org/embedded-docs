> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/fr.md)

Voici la traduction de la documentation technique du nœud ComfyUI **TripoP1ImageToModelNode** :

## Aperçu

Ce nœud convertit une image 2D unique en un modèle 3D via l'API Tripo P1. Il est optimisé pour générer des maillages prêts pour le jeu, à faible nombre de polygones.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à convertir en modèle 3D. |
| `output_mode` | DICT | Oui | Voir description | Un dictionnaire spécifiant le mode de sortie et les paramètres de qualité. Ce paramètre contrôle le type de modèle généré et sa qualité de texture. Les options disponibles sont définies par la fonction d'assistance `_build_p1_output_mode` et incluent des réglages pour `texture_quality` (par exemple, "standard", "high", "ultra") et `image_alignment`. |
| `enable_image_autofix` | BOOLEAN | Non | True<br>False | Prétraite l'image d'entrée pour améliorer la qualité de génération. (par défaut : False) |
| `face_limit` | INT | Non | - | Limite le nombre de faces dans le maillage généré. Une valeur de -1 signifie aucune limite. (par défaut : -1) |
| `model_seed` | INT | Non | - | Une valeur de graine pour une génération de modèle reproductible. Si non fournie, une graine aléatoire est utilisée. (par défaut : None) |
| `auto_size` | BOOLEAN | Non | True<br>False | Détermine automatiquement la taille optimale du modèle généré. (par défaut : False) |
| `export_uv` | BOOLEAN | Non | True<br>False | Exporte les coordonnées UV avec le modèle. (par défaut : True) |
| `compress_geometry` | BOOLEAN | Non | True<br>False | Compresse les données de géométrie pour réduire la taille du fichier. (par défaut : False) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `model_file` | STRING | Le chemin d'accès au fichier du modèle 3D généré. Cette sortie est fournie uniquement pour la rétrocompatibilité. |
| `model task_id` | MODEL_TASK_ID | L'identifiant unique de la tâche pour la demande de génération de modèle. |
| `GLB` | FILE3DGLB | Le modèle 3D généré au format GLB. |

---
**Source fingerprint (SHA-256):** `2ac611603dd6eb88700a8105c19f97a8c4eefe5f4efb23d8854ccc27af590626`
