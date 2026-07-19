# LTXVContextWindows

Ce nœud définit des fenêtres de contexte pour les modèles de type LTXV lors de l'échantillonnage. Il divise le processus de génération vidéo en fenêtres qui se chevauchent afin de gérer l'utilisation de la mémoire et d'améliorer la cohérence temporelle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle auquel appliquer les fenêtres de contexte lors de l'échantillonnage. | MODEL | Oui | - |
| `context_length` | La longueur de la fenêtre de contexte en images réelles. Doit être 8*n + 1. (par défaut : 145) | INT | Oui | Minimum : 1<br>Maximum : nodes.MAX_RESOLUTION<br>Pas : 8 |
| `context_overlap` | Le chevauchement de la fenêtre de contexte en images réelles. (par défaut : 40) | INT | Oui | Minimum : 0<br>Pas : 8 |
| `context_schedule` | Algorithme de planification dépendant de l'étape pour les fenêtres de contexte. (par défaut : UNIFORM_STANDARD) | COMBO | Oui | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` |
| `context_stride` | Le pas de la fenêtre de contexte ; applicable uniquement aux planifications uniformes. (par défaut : 1) | INT | Non | Minimum : 1 |
| `closed_loop` | Indique s'il faut fermer la boucle de la fenêtre de contexte ; applicable uniquement aux planifications en boucle. (par défaut : False) | BOOLEAN | Non | True<br>False |
| `fuse_method` | La méthode à utiliser pour fusionner les fenêtres de contexte. (par défaut : PYRAMID) | COMBO | Oui | Options issues de comfy.context_windows.ContextFuseMethods.LIST_STATIC |
| `freenoise` | Indique s'il faut appliquer le mélange de bruit FreeNoise, améliore le mélange des fenêtres. (par défaut : True) | BOOLEAN | Non | True<br>False |
| `retain_first_frame` | Conserver la première image latente dans chaque fenêtre de contexte (peut aider à conserver la référence initiale). (par défaut : False) | BOOLEAN | Non | True<br>False |
| `split_conds_to_windows` | Indique s'il faut diviser les conditionnements multiples (créés par ConditionCombine) en chaque fenêtre en fonction de l'index de région. (par défaut : False) | BOOLEAN | Non | True<br>False |

**Remarque :** Le paramètre `context_length` doit respecter la formule 8*n + 1, où n est un entier positif. Le nœud ajuste automatiquement la valeur pour répondre à cette exigence en convertissant les images réelles en images latentes. Le paramètre `context_overlap` est également converti d'images réelles en images latentes (divisé par 8).

## Sorties

| Nom de la sortie | Description | Type de données |
|------------------|-------------|-----------------|
| `MODEL` | Le modèle avec les fenêtres de contexte appliquées pour l'échantillonnage. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVContextWindows/fr.md)

---
**Source fingerprint (SHA-256):** `ad0b8c54acaab1853f6fe98dbad675478f033caf867df954b40b7db5208f5ae4`
