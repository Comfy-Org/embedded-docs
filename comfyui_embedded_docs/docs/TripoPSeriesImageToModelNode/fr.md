# Tripo P2 : Image vers modèle

Génère un modèle 3D low-poly avec une topologie propre à partir d'une seule image en utilisant le modèle P2 de Tripo. Le résultat est renvoyé sous forme de maillage triangulaire (GLB) ou, lorsque `model.quad` est activé, sous forme de maillage à dominante quadrangulaire (FBX).

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle de la série P de Tripo à utiliser. La sélection d'un modèle révèle ses propres entrées ci-dessous. | DYNAMIC_COMBO | Oui | `"P2"` |

### Entrées P2

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `model.image` | L'image à partir de laquelle le modèle est généré. | IMAGE | Oui | - |
| `quad` | Renvoie un maillage à dominante quadrangulaire sur la sortie FBX au lieu d'un maillage triangulaire sur la sortie GLB (par défaut : False). | BOOLEAN | Oui | True/False |
| `face_limit` | Nombre de faces cible. `-1` laisse Tripo choisir. Lorsque `model.quad` est activé, la limite est de 48 à 25 000, sinon de 48 à 50 000 (par défaut : -1). | INT | Oui | -1, ou 48 à 50000 |
| `texture` | Résolution de la texture de couleur de base : standard correspond à 2K, detailed à 4K et extreme à 8K. `"none"` renvoie un maillage non texturé (par défaut : `"standard"`). | COMBO | Oui | `"standard"`<br>`"detailed"`<br>`"extreme"`<br>`"none"` |
| `pbr` | Ajoute des cartes de métallicité, de rugosité et de normales à la couleur de base. Ignoré lorsque `model.texture` est `"none"` (par défaut : True). | BOOLEAN | Oui | True/False |
| `model_seed` | Graine pour la géométrie (par défaut : 42). | INT | Oui | 0 à 2147483647 |
| `texture_alignment` | Fait correspondre les couleurs de l'image d'entrée ou adapte les textures à la géométrie générée. Ignoré lorsque `model.texture` est `"none"` (par défaut : `"original_image"`). Paramètre avancé. | COMBO | Oui | `"original_image"`<br>`"geometry"` |
| `orientation` | `"align_image"` fait pivoter le modèle selon le point de vue de l'image d'entrée. Ignoré lorsque `model.texture` est `"none"` (par défaut : `"default"`). Paramètre avancé. | COMBO | Oui | `"default"`<br>`"align_image"` |
| `enable_image_autofix` | Laisse Tripo améliorer une image de faible résolution ou de faible qualité avant la modélisation (par défaut : False). Paramètre avancé. | BOOLEAN | Oui | True/False |
| `texture_seed` | Graine pour les textures (par défaut : 42). Paramètre avancé. | INT | Oui | 0 à 2147483647 |
| `auto_size` | Redimensionne le modèle à sa taille réelle en mètres via sa transformation de scène (par défaut : False). Paramètre avancé. | BOOLEAN | Oui | True/False |
| `export_uv` | Déplie les UV du maillage lorsqu'il n'est pas texturé. Les maillages texturés sont toujours dépliés (par défaut : True). Paramètre avancé. | BOOLEAN | Oui | True/False |
| `compress_geometry` | Applique la compression de géométrie meshopt : des fichiers beaucoup plus petits, mais l'aperçu 3D de ComfyUI ne peut pas les afficher. Ignoré pour les maillages quadrangulaires (par défaut : False). Paramètre avancé. | BOOLEAN | Oui | True/False |

**Remarques :**

- `model.image` est obligatoire et seule la première image du lot est utilisée.
- `model.face_limit` est une cible plutôt qu'un plafond strict, le résultat peut donc contenir plus de faces que demandé. `-1` laisse le choix à Tripo.
- `model.quad` détermine quelle sortie porte le maillage. Lorsqu'il est activé, le modèle arrive sur la sortie FBX et la sortie GLB reste vide ; lorsqu'il est désactivé, le modèle arrive sur GLB et FBX reste vide. Le nœud renvoie une erreur si la sortie vide est celle que vous avez connectée.
- `model.texture`, `model.pbr`, `model.texture_seed`, `model.auto_size`, `model.texture_alignment` et `model.orientation` ne s'appliquent qu'aux modèles texturés : avec `"none"`, le nœud n'envoie aucun paramètre de texture et renvoie une géométrie brute.
- `model.compress_geometry` n'a aucun effet sur les maillages quadrangulaires.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model task_id` | L'identifiant de tâche unique pour la requête de génération du modèle. | MODEL_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB. Vide lorsque `model.quad` est activé. | FILE3DGLB |
| `FBX` | Le modèle 3D généré au format FBX. Rempli uniquement lorsque `model.quad` est activé. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesImageToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `9bfad31ee00546d0603ce3273502cfc93c79e3b125941fed255866aa83f770a5`
