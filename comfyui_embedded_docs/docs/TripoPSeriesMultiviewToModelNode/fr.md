# Tripo P2 : Vues multiples vers modèle

Génère un modèle 3D low-poly avec une topologie propre à partir de plusieurs vues du même sujet à l'aide du modèle P2 de Tripo. La vue de face est obligatoire et une à trois des vues gauche, arrière et droite peuvent être ajoutées pour améliorer le résultat. Le modèle est renvoyé sous forme de maillage triangulaire (GLB) ou, lorsque `model.quad` est activé, sous forme de maillage à dominante quadrilatérale (FBX).

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle Tripo de la série P à utiliser. La sélection d'un modèle affiche ses propres entrées ci-dessous. | DYNAMIC_COMBO | Oui | `"P2"` |

### Entrées P2

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model.image` | Vue de face (0°) du sujet. | IMAGE | Oui | - |
| `model.image_left` | Vue de gauche (90°), le côté gauche du sujet lui-même. | IMAGE | Non | - |
| `model.image_back` | Vue arrière (180°). | IMAGE | Non | - |
| `model.image_right` | Vue de droite (270°), le côté droit du sujet lui-même. | IMAGE | Non | - |
| `quad` | Renvoyer un maillage à dominante quadrilatérale sur la sortie FBX au lieu d'un maillage triangulaire sur la sortie GLB (par défaut : False). | BOOLEAN | Oui | True/False |
| `face_limit` | Nombre de faces cible. `-1` laisse Tripo choisir. Lorsque `model.quad` est activé, la limite est de 48 à 25 000, sinon de 48 à 50 000 (par défaut : -1). | INT | Oui | -1, ou 48 à 50 000 |
| `texture` | Résolution de la texture de couleur de base : standard correspond à 2K, detailed à 4K et extreme à 8K. `"none"` renvoie un maillage non texturé (par défaut : `"standard"`). | COMBO | Oui | `"standard"`<br>`"detailed"`<br>`"extreme"`<br>`"none"` |
| `pbr` | Ajouter des cartes de métallicité, de rugosité et de normales à la couleur de base. Ignoré lorsque `model.texture` vaut `"none"` (par défaut : True). | BOOLEAN | Oui | True/False |
| `model_seed` | Graine pour la géométrie (par défaut : 42). | INT | Oui | 0 à 2147483647 |
| `texture_alignment` | Faire correspondre les couleurs des images d'entrée, ou adapter les textures à la géométrie générée. Ignoré lorsque `model.texture` vaut `"none"` (par défaut : `"original_image"`). Paramètre avancé. | COMBO | Oui | `"original_image"`<br>`"geometry"` |
| `orientation` | `"align_image"` fait pivoter le modèle vers le point de vue des images d'entrée. Ignoré lorsque `model.texture` vaut `"none"` (par défaut : `"default"`). Paramètre avancé. | COMBO | Oui | `"default"`<br>`"align_image"` |
| `texture_seed` | Graine pour les textures (par défaut : 42). Paramètre avancé. | INT | Oui | 0 à 2147483647 |
| `auto_size` | Mettre le modèle à l'échelle de sa taille réelle en mètres via la transformation de sa scène. Ignoré lorsque `model.texture` vaut `"none"` (par défaut : False). Paramètre avancé. | BOOLEAN | Oui | True/False |
| `export_uv` | Effectuer un dépliage UV du maillage lorsqu'il n'est pas texturé. Les maillages texturés sont toujours dépliés (par défaut : True). Paramètre avancé. | BOOLEAN | Oui | True/False |
| `compress_geometry` | Appliquer la compression de géométrie meshopt : fichiers beaucoup plus petits, mais l'aperçu 3D de ComfyUI ne peut pas les afficher. Ignoré pour les maillages quadrilatéraux (par défaut : False). Paramètre avancé. | BOOLEAN | Oui | True/False |

**Remarques :**

- `model.image` est obligatoire, et au moins une des entrées `model.image_left`, `model.image_back` ou `model.image_right` doit également être connectée ; le nœud renvoie une erreur si la vue de face est la seule image.
- Seule la première image de chaque lot est utilisée.
- `model.face_limit` est une cible plutôt qu'un plafond strict, le résultat peut donc contenir plus de faces que demandé. `-1` laisse le choix à Tripo.
- `model.quad` détermine quelle sortie transporte le maillage. Lorsqu'il est activé, le modèle arrive sur la sortie FBX et la sortie GLB reste vide ; lorsqu'il est désactivé, le modèle arrive sur GLB et FBX reste vide. Le nœud renvoie une erreur si la sortie vide est celle que vous avez connectée.
- `model.texture`, `model.pbr`, `model.texture_seed`, `model.auto_size`, `model.texture_alignment` et `model.orientation` ne s'appliquent qu'aux modèles texturés : avec `"none"`, le nœud n'envoie aucun paramètre de texture et renvoie une géométrie brute.
- `model.compress_geometry` n'a aucun effet sur les maillages quadrilatéraux.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model task_id` | L'identifiant unique de tâche pour la requête de génération du modèle. | MODEL_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB. Vide lorsque `model.quad` est activé. | FILE3DGLB |
| `FBX` | Le modèle 3D généré au format FBX. Rempli uniquement lorsque `model.quad` est activé. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesMultiviewToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `cea0a65ca001bc8298af9fbe2a83f592abf497987e634b0126482f3d2a18571c`
