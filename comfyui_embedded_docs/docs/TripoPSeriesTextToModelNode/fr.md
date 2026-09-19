# Tripo P2 : Texte vers modèle

Génère un modèle 3D low-poly avec une topologie propre à partir d'une invite textuelle en utilisant le modèle P2 de Tripo. Le résultat est renvoyé sous forme de maillage triangulaire (GLB) ou, lorsque `model.quad` est activé, sous forme de maillage à dominante quadrilatérale (FBX).

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Modèle Tripo série P à utiliser. La sélection d'un modèle révèle ses propres entrées ci-dessous. | DYNAMIC_COMBO | Oui | `"P2"` |

### Entrées P2

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `invite` | Description textuelle du modèle 3D à générer. Ne doit pas être vide, jusqu'à 1024 caractères (par défaut : vide). | STRING | Oui | Jusqu'à 1024 caractères |
| `negative_prompt` | Description textuelle de ce qu'il faut éviter dans le modèle généré (par défaut : vide). | STRING | Non | Jusqu'à 255 caractères |
| `quad` | Renvoyer un maillage à dominante quadrilatérale sur la sortie FBX au lieu d'un maillage triangulaire sur la sortie GLB (par défaut : False). | BOOLEAN | Oui | True/False |
| `face_limit` | Nombre de faces cible. `-1` laisse Tripo choisir. Lorsque `model.quad` est activé, la limite est de 48 à 25 000, sinon de 48 à 50 000 (par défaut : -1). | INT | Oui | -1, ou 48 à 50000 |
| `texture` | Résolution de la texture de couleur de base : standard correspond à 2K, detailed à 4K et extreme à 8K. `"none"` renvoie un maillage non texturé (par défaut : `"standard"`). | COMBO | Oui | `"standard"`<br>`"detailed"`<br>`"extreme"`<br>`"none"` |
| `pbr` | Ajouter les cartes métallique, de rugosité et de normales à la couleur de base. Ignoré lorsque `model.texture` vaut `"none"` (par défaut : True). | BOOLEAN | Oui | True/False |
| `model_seed` | Graine pour la géométrie (par défaut : 42). | INT | Oui | 0 à 2147483647 |
| `image_seed` | Graine pour l'image que Tripo dessine à partir de l'invite avant la modélisation (par défaut : 42). Paramètre avancé. | INT | Oui | 0 à 2147483647 |
| `texture_seed` | Graine pour les textures (par défaut : 42). Paramètre avancé. | INT | Oui | 0 à 2147483647 |
| `auto_size` | Mettre le modèle à l'échelle de sa taille réelle en mètres via la transformation de sa scène. Ignoré lorsque `model.texture` vaut `"none"` (par défaut : False). Paramètre avancé. | BOOLEAN | Oui | True/False |
| `export_uv` | Déplier les UV du maillage lorsqu'il n'est pas texturé. Les maillages texturés sont toujours dépliés (par défaut : True). Paramètre avancé. | BOOLEAN | Oui | True/False |
| `compress_geometry` | Appliquer la compression de géométrie meshopt : fichiers beaucoup plus petits, mais l'aperçu 3D de ComfyUI ne peut pas les afficher. Ignoré pour les maillages quadrilatéraux (par défaut : False). Paramètre avancé. | BOOLEAN | Oui | True/False |

**Remarques :**

- `model.prompt` est requis ; `model.negative_prompt` est facultatif et limité à 255 caractères.
- `model.face_limit` est une cible plutôt qu'un plafond strict, le résultat peut donc contenir plus de faces que demandé. `-1` laisse le choix à Tripo.
- `model.quad` détermine quelle sortie porte le maillage. Lorsqu'il est activé, le modèle arrive sur la sortie FBX et la sortie GLB reste vide ; lorsqu'il est désactivé, le modèle arrive sur GLB et FBX reste vide. Le nœud génère une erreur si la sortie vide est celle que vous avez connectée.
- `model.texture`, `model.pbr`, `model.texture_seed` et `model.auto_size` ne s'appliquent qu'aux modèles texturés : avec `"none"`, le nœud n'envoie aucun paramètre de texture et renvoie une géométrie brute.
- `model.compress_geometry` n'a aucun effet sur les maillages quadrilatéraux.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model task_id` | L'identifiant unique de tâche pour la requête de génération du modèle. | MODEL_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB. Vide lorsque `model.quad` est activé. | FILE3DGLB |
| `FBX` | Le modèle 3D généré au format FBX. Rempli uniquement lorsque `model.quad` est activé. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesTextToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `e55596c1a237cf6b92e3bdead4359f380c6cba60992dcc61b5ee4e6b1bdd843b`
