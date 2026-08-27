# Fenêtres de contexte (Manuel)

Le nœud **Context Windows (Manual)** vous permet de configurer manuellement les fenêtres de contexte d'un modèle pendant l'échantillonnage, en créant des segments de contexte se chevauchant avec une longueur, un chevauchement et un modèle de planification spécifiés, afin que les données soient traitées par blocs gérables tout en maintenant la continuité entre les segments. Il fournit des options avancées pour contrôler la manière dont les fenêtres de contexte sont appliquées, notamment le remaniement du bruit, la rétention du conditionnement et les corrections de fenêtre causale. Ce nœud est expérimental.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel appliquer les fenêtres de contexte pendant l'échantillonnage. | MODEL | Oui | - |
| `longueur_contexte` | La longueur de la fenêtre de contexte (défaut : 16). | INT | Oui | 1+ |
| `chevauchement_contexte` | Le chevauchement de la fenêtre de contexte (défaut : 4). | INT | Oui | 0+ |
| `planification_contexte` | Algorithme de planification dépendant de l'étape pour les fenêtres de contexte (défaut : STATIC_STANDARD). | COMBO | Oui | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` |
| `pas_contexte` | Le pas (stride) de la fenêtre de contexte ; applicable uniquement aux planifications uniformes (défaut : 1). | INT | Oui | 1+ |
| `boucle_fermée` | Indique s'il faut boucler la fenêtre de contexte ; applicable uniquement aux planifications en boucle (défaut : False). | BOOLEAN | Oui | - |
| `méthode_fusion` | La méthode à utiliser pour fusionner les fenêtres de contexte (défaut : PYRAMID). | COMBO | Oui | Méthodes de fusion statiques (voir `ContextFuseMethods.LIST_STATIC`) |
| `dimension` | La dimension à laquelle appliquer les fenêtres de contexte (défaut : 0). | INT | Oui | 0-5 |
| `bruit_libre` | Indique s'il faut appliquer le remaniement de bruit FreeNoise, améliore le mélange des fenêtres (défaut : False). | BOOLEAN | Oui | - |
| `cond_retain_index_list` | Liste des indices latents à conserver dans les tenseurs de conditionnement pour chaque fenêtre. Pour les modèles I2V de type concat (par ex. Wan I2V, HunyuanVideo I2V, Cosmos I2V, SVD), l'image de départ encodée se trouve dans les canaux de conditionnement `c_concat` ; définir cette valeur sur « 0 » conservera ce contenu d'image de départ à la sous-position 0 de chaque fenêtre (défaut : ""). | STRING | Non | - |
| `split_conds_to_windows` | Indique s'il faut diviser les conditionnements multiples (créés par ConditionCombine) pour chaque fenêtre en fonction de l'index de région (défaut : False). | BOOLEAN | Non | - |
| `latent_retain_index_list` | Liste des indices latents à conserver dans le latent de bruit lui-même pour chaque fenêtre. À utiliser pour les flux de travail où le contenu de référence (par ex. une image de départ) se trouve directement dans le latent de bruit plutôt que dans des canaux de conditionnement séparés (par ex. I2V de style inplace comme LTXV, AnimateDiff). Indépendant de `cond_retain_index_list` (défaut : ""). | STRING | Non | - |
| `causal_window_fix` | Indique s'il faut ajouter une frame de correction causale aux fenêtres de contexte non indexées à 0 (défaut : True). | BOOLEAN | Non | - |

**Contraintes des paramètres :**

- `context_stride` n'est utilisé que lorsqu'une planification uniforme est sélectionnée (`UNIFORM_STANDARD` ou `UNIFORM_LOOPED`).
- `closed_loop` n'est applicable qu'aux planifications en boucle (`UNIFORM_LOOPED`).
- `dim` doit être compris entre 0 et 5 inclus.
- `cond_retain_index_list` et `latent_retain_index_list` attendent une liste d'indices entiers séparés par des virgules sous forme de chaîne (par ex. « 0,1,2 »).
- `latent_retain_index_list` est indépendant de `cond_retain_index_list`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle avec les fenêtres de contexte appliquées pendant l'échantillonnage. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/fr.md)

---
**Source fingerprint (SHA-256):** `39dc39ece3d3c10c13ca8c4b85af4fbbebbcaba8a019145a6d4727c3df7b302b`
