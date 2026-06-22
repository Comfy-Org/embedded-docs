# Tripo P1 : Multivues vers Modèle

Voici la traduction en français de la documentation du nœud ComfyUI :

## Aperçu

Ce nœud génère un modèle 3D à partir de 2 à 4 images de référence d'un objet ou d'un personnage. Vous fournissez des images sous différents angles (avant, gauche, arrière, droite), et le nœud crée un maillage 3D au format GLB. La vue de face est obligatoire, et vous pouvez éventuellement ajouter toute combinaison des trois autres vues pour de meilleurs résultats.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | Vue de face (0°). Requise. | IMAGE | Oui | - |
| `image_left` | Vue de gauche (90°), c'est-à-dire le côté gauche du sujet. | IMAGE | Non | - |
| `image_back` | Vue arrière (180°). | IMAGE | Non | - |
| `image_right` | Vue de droite (270°), c'est-à-dire le côté droit du sujet. | IMAGE | Non | - |
| `output_mode` | Le mode de sortie pour le modèle généré. `"geometry"` produit un maillage brut, `"textured"` ajoute une texture standard, et `"detailed"` crée un modèle texturé haute définition (par défaut : `"textured"`). | COMBO | Oui | `"geometry"`<br>`"textured"`<br>`"detailed"` |
| `face_limit` | Nombre maximum de faces pour le maillage de sortie. Réglez sur -1 pour aucune limite (par défaut : -1). | INT | Non | -1 à 100000 |
| `model_seed` | Graine pour une génération de modèle reproductible. Réglez sur 0 pour aléatoire (par défaut : 0). | INT | Non | 0 à 2147483647 |
| `auto_size` | Redimensionner automatiquement le modèle pour qu'il s'adapte à une boîte englobante standard (par défaut : Faux). | BOOLEAN | Non | Vrai / Faux |
| `export_uv` | Exporter les coordonnées UV avec le modèle (par défaut : Vrai). | BOOLEAN | Non | Vrai / Faux |
| `compress_geometry` | Compresser les données géométriques pour réduire la taille du fichier (par défaut : Faux). | BOOLEAN | Non | Vrai / Faux |

**Remarque :** Vous devez fournir au moins 2 images : la vue de face (`image`) plus au moins une des autres vues (`image_left`, `image_back` ou `image_right`). Si moins de 2 images sont fournies, le nœud générera une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model task_id` | Le nom du fichier du modèle GLB généré (uniquement pour la rétrocompatibilité). | STRING |
| `GLB` | L'identifiant unique de la tâche pour cette demande de génération de modèle. | MODEL_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB. | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `29bb87cdc5d3eef891a653c622e8876a37d6e6dc1a43e5c248b184060ead9029`
