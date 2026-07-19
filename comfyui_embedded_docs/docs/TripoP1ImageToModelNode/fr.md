# Tripo P1 : Image vers Modèle

Voici la traduction de la documentation technique du nœud ComfyUI **TripoP1ImageToModelNode** :

## Aperçu

Ce nœud convertit une image 2D unique en un modèle 3D via l'API Tripo P1. Il est optimisé pour générer des maillages prêts pour le jeu, à faible nombre de polygones.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à convertir en modèle 3D. | IMAGE | Oui | - |
| `output_mode` | Un dictionnaire spécifiant le mode de sortie et les paramètres de qualité. Ce paramètre contrôle le type de modèle généré et sa qualité de texture. Les options disponibles sont définies par la fonction d'assistance `_build_p1_output_mode` et incluent des réglages pour `texture_quality` (par exemple, "standard", "high", "ultra") et `image_alignment`. | DICT | Oui | Voir description |
| `enable_image_autofix` | Prétraite l'image d'entrée pour améliorer la qualité de génération. (par défaut : False) | BOOLEAN | Non | True<br>False |
| `face_limit` | Limite le nombre de faces dans le maillage généré. Une valeur de -1 signifie aucune limite. (par défaut : -1) | INT | Non | - |
| `model_seed` | Une valeur de graine pour une génération de modèle reproductible. Si non fournie, une graine aléatoire est utilisée. (par défaut : None) | INT | Non | - |
| `auto_size` | Détermine automatiquement la taille optimale du modèle généré. (par défaut : False) | BOOLEAN | Non | True<br>False |
| `export_uv` | Exporte les coordonnées UV avec le modèle. (par défaut : True) | BOOLEAN | Non | True<br>False |
| `compress_geometry` | Compresse les données de géométrie pour réduire la taille du fichier. (par défaut : False) | BOOLEAN | Non | True<br>False |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model_file` | Le chemin d'accès au fichier du modèle 3D généré. Cette sortie est fournie uniquement pour la rétrocompatibilité. | STRING |
| `model task_id` | L'identifiant unique de la tâche pour la demande de génération de modèle. | MODEL_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB. | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `2ac611603dd6eb88700a8105c19f97a8c4eefe5f4efb23d8854ccc27af590626`
