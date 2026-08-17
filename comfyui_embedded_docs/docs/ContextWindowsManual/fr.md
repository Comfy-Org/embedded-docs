# Fenêtres de contexte (Manuel)

Le nœud Context Windows (Manuel) vous permet de configurer manuellement les fenêtres de contexte pour les modèles pendant l'échantillonnage. Il crée des segments de contexte se chevauchant, avec une longueur, un chevauchement et des motifs de planification spécifiés, afin de traiter les données en blocs gérables tout en maintenant une continuité entre les segments. Ce nœud fournit des options avancées pour contrôler la manière dont les fenêtres de contexte sont appliquées, notamment le mélange de bruit (noise shuffling), la rétention des conditionnements, la rétention du bruit latent et les corrections de fenêtre causale.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle auquel appliquer les fenêtres de contexte pendant l'échantillonnage. | MODEL | Oui | - |
| `context_length` | La longueur de la fenêtre de contexte (par défaut : 16). | INT | Non | 1+ |
| `context_overlap` | Le chevauchement de la fenêtre de contexte (par défaut : 4). | INT | Non | 0+ |
| `context_schedule` | Algorithme de planification dépendant de l'étape pour les fenêtres de contexte (par défaut : STATIC_STANDARD). | COMBO | Non | `"STATIC_STANDARD"`<br>`"UNIFORM_STANDARD"`<br>`"UNIFORM_LOOPED"`<br>`"BATCHED"` |
| `context_stride` | Le pas de la fenêtre de contexte ; applicable uniquement aux planifications uniformes (par défaut : 1). | INT | Non | 1+ |
| `closed_loop` | Indique s'il faut fermer la boucle de la fenêtre de contexte ; applicable uniquement aux planifications en boucle (par défaut : False). | BOOLEAN | Non | - |
| `fuse_method` | La méthode à utiliser pour fusionner les fenêtres de contexte (par défaut : PYRAMID). | COMBO | Non | `"PYRAMID"`<br>`"LIST_STATIC"` |
| `dim` | La dimension à laquelle appliquer les fenêtres de contexte (par défaut : 0). | INT | Non | 0-5 |
| `freenoise` | Indique s'il faut appliquer le mélange de bruit FreeNoise ; améliore le fondu des fenêtres (par défaut : False). | BOOLEAN | Non | - |
| `cond_retain_index_list` | Liste des indices latents à conserver dans les tenseurs de conditionnement pour chaque fenêtre. Pour les modèles I2V de type concat (par exemple Wan I2V, HunyuanVideo I2V, Cosmos I2V, SVD), l'image de départ encodée se trouve dans les canaux de conditionnement `c_concat` ; définir cette valeur sur « 0 » conservera le contenu de cette image de départ à la sous-position 0 de chaque fenêtre (par défaut : « »). | STRING | Non | - |
| `split_conds_to_windows` | Indique s'il faut répartir les multiples conditionnements (créés par ConditionCombine) dans chaque fenêtre en fonction de l'index de région (par défaut : False). | BOOLEAN | Non | - |
| `latent_retain_index_list` | Liste des indices latents à conserver dans le bruit latent lui-même pour chaque fenêtre. À utiliser pour les flux de travail où le contenu de référence (par exemple une image de départ) réside directement dans le bruit latent plutôt que dans des canaux de conditionnement séparés (par exemple I2V de type inplace comme LTXV, AnimateDiff). Indépendant de `cond_retain_index_list` (par défaut : « »). | STRING | Non | - |
| `causal_window_fix` | Indique s'il faut ajouter une trame de correction causale aux fenêtres de contexte non indexées à 0 (par défaut : True). | BOOLEAN | Non | - |

**Contraintes des paramètres :**

- `context_stride` n'est utilisé que lorsque des planifications uniformes sont sélectionnées
- `closed_loop` n'est applicable qu'aux planifications en boucle
- `dim` doit être compris entre 0 et 5 inclus
- `cond_retain_index_list` attend une liste d'indices entiers séparés par des virgules sous forme de chaîne (par exemple « 0,1,2 »)
- `latent_retain_index_list` attend une liste d'indices entiers séparés par des virgules sous forme de chaîne (par exemple « 0,1,2 ») et est indépendant de `cond_retain_index_list`

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle avec les fenêtres de contexte appliquées pendant l'échantillonnage. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/fr.md)

---
**Source fingerprint (SHA-256):** `39dc39ece3d3c10c13ca8c4b85af4fbbebbcaba8a019145a6d4727c3df7b302b`
