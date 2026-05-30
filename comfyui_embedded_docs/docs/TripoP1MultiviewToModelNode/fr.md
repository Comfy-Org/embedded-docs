> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI :

## Aperçu

Ce nœud génère un modèle 3D à partir de 2 à 4 images de référence d'un objet ou d'un personnage. Vous fournissez des images sous différents angles (avant, gauche, arrière, droite), et le nœud crée un maillage 3D au format GLB. La vue de face est obligatoire, et vous pouvez éventuellement ajouter toute combinaison des trois autres vues pour de meilleurs résultats.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Oui | - | Vue de face (0°). Requise. |
| `image_left` | IMAGE | Non | - | Vue de gauche (90°), c'est-à-dire le côté gauche du sujet. |
| `image_back` | IMAGE | Non | - | Vue arrière (180°). |
| `image_right` | IMAGE | Non | - | Vue de droite (270°), c'est-à-dire le côté droit du sujet. |
| `output_mode` | COMBO | Oui | `"geometry"`<br>`"textured"`<br>`"detailed"` | Le mode de sortie pour le modèle généré. `"geometry"` produit un maillage brut, `"textured"` ajoute une texture standard, et `"detailed"` crée un modèle texturé haute définition (par défaut : `"textured"`). |
| `face_limit` | INT | Non | -1 à 100000 | Nombre maximum de faces pour le maillage de sortie. Réglez sur -1 pour aucune limite (par défaut : -1). |
| `model_seed` | INT | Non | 0 à 2147483647 | Graine pour une génération de modèle reproductible. Réglez sur 0 pour aléatoire (par défaut : 0). |
| `auto_size` | BOOLEAN | Non | Vrai / Faux | Redimensionner automatiquement le modèle pour qu'il s'adapte à une boîte englobante standard (par défaut : Faux). |
| `export_uv` | BOOLEAN | Non | Vrai / Faux | Exporter les coordonnées UV avec le modèle (par défaut : Vrai). |
| `compress_geometry` | BOOLEAN | Non | Vrai / Faux | Compresser les données géométriques pour réduire la taille du fichier (par défaut : Faux). |

**Remarque :** Vous devez fournir au moins 2 images : la vue de face (`image`) plus au moins une des autres vues (`image_left`, `image_back` ou `image_right`). Si moins de 2 images sont fournies, le nœud générera une erreur.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `model_file` | STRING | Le nom du fichier du modèle GLB généré (uniquement pour la rétrocompatibilité). |
| `model_task_id` | MODEL_TASK_ID | L'identifiant unique de la tâche pour cette demande de génération de modèle. |
| `GLB` | FILE3DGLB | Le modèle 3D généré au format GLB. |

---
**Source fingerprint (SHA-256):** `29bb87cdc5d3eef891a653c622e8876a37d6e6dc1a43e5c248b184060ead9029`
