# Fenêtres de contexte LTXV

Ce nœud définit des fenêtres de contexte pour les modèles de type LTXV pendant l'échantillonnage. Il divise la génération en fenêtres qui se chevauchent afin d'aider à gérer l'utilisation de la mémoire et d'améliorer la cohérence temporelle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle auquel appliquer les fenêtres de contexte pendant l'échantillonnage. | MODEL | Oui | - |
| `context_length` | La longueur de la fenêtre de contexte en images réelles. Doit être 8*n + 1. (par défaut : 145) | INT | Oui | Minimum : 1<br>Maximum : nodes.MAX_RESOLUTION<br>Pas : 8 |
| `context_overlap` | Le chevauchement de la fenêtre de contexte en images réelles. (par défaut : 40) | INT | Oui | Minimum : 0<br>Pas : 8 |
| `context_schedule` | Algorithme de planification dépendant des étapes pour les fenêtres de contexte. (par défaut : "UNIFORM_STANDARD") | COMBO | Oui | `"STATIC_STANDARD"`<br>`"UNIFORM_STANDARD"`<br>`"UNIFORM_LOOPED"`<br>`"BATCHED"` |
| `context_stride` | Le pas de la fenêtre de contexte ; applicable uniquement aux planifications uniformes. (par défaut : 1) | INT | Oui | Minimum : 1 |
| `closed_loop` | Indique s'il faut fermer la boucle de la fenêtre de contexte ; applicable uniquement aux planifications en boucle. (par défaut : False) | BOOLEAN | Oui | True<br>False |
| `fuse_method` | La méthode à utiliser pour fusionner les fenêtres de contexte. Les options disponibles sont définies par `ContextFuseMethods.LIST_STATIC`. (par défaut : "PYRAMID") | COMBO | Oui | Défini par `ContextFuseMethods.LIST_STATIC` |
| `freenoise` | Indique s'il faut appliquer le brassage de bruit FreeNoise, ce qui améliore le mélange des fenêtres. (par défaut : True) | BOOLEAN | Oui | True<br>False |
| `retain_first_frame` | Conserver la première image latente dans chaque fenêtre de contexte (peut aider à conserver la référence initiale). (par défaut : False) | BOOLEAN | Oui | True<br>False |
| `split_conds_to_windows` | Indique s'il faut répartir plusieurs conditionnements (créés par ConditionCombine) vers chaque fenêtre en fonction de l'index de région. (par défaut : False) | BOOLEAN | Oui | True<br>False |

**Remarque :** La valeur `context_length` est fournie en images réelles et est convertie en interne en images latentes à l'aide de la formule `((context_length - 1) // 8) + 1`, avec un minimum de 1. La valeur `context_overlap` est également fournie en images réelles et est convertie en images latentes par division entière par 8, avec un minimum de 0. L'infobulle de `context_length` indique qu'elle doit suivre le modèle 8*n + 1.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `MODEL` | Le modèle avec les fenêtres de contexte appliquées pour l'échantillonnage. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVContextWindows/fr.md)

---
**Source fingerprint (SHA-256):** `148649d0a938e08c932a163f5d7614332626fba37b8f79db7f92bbcf422e692f`
