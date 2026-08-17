# Fenêtres de contexte WAN (Manuel)

Le nœud Wan Context Windows (Manual) vous permet de configurer manuellement des fenêtres de contexte pour les modèles de type Wan avec un traitement bidimensionnel. Il applique les paramètres de fenêtre de contexte pendant l'échantillonnage en spécifiant la longueur de la fenêtre, le chevauchement, la méthode de planification et la technique de fusion, vous donnant ainsi le contrôle sur la façon dont le modèle traite les différentes régions de contexte.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle auquel appliquer les fenêtres de contexte pendant l'échantillonnage. | MODEL | Oui | - |
| `context_length` | La longueur de la fenêtre de contexte en images réelles. Doit être 4*n + 1. (défaut : 81) | INT | Oui | 1 à 16384 (pas de 4) |
| `context_overlap` | Le chevauchement de la fenêtre de contexte en images réelles. (défaut : 30) | INT | Oui | 0 ou plus |
| `context_schedule` | Algorithme de planification dépendant de l'étape pour les fenêtres de contexte. (défaut : "uniform_standard") | COMBO | Oui | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `context_stride` | Le pas de la fenêtre de contexte ; applicable uniquement aux planifications uniformes. (défaut : 1) | INT | Oui | 1 ou plus |
| `closed_loop` | Indique si la boucle de la fenêtre de contexte doit être fermée ; applicable uniquement aux planifications en boucle. (défaut : False) | BOOLEAN | Oui | True ou False |
| `fuse_method` | La méthode à utiliser pour fusionner les fenêtres de contexte. (défaut : "pyramid") | COMBO | Oui | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` |
| `freenoise` | Indique si le brassage de bruit FreeNoise est appliqué ; améliore la fusion des fenêtres. (défaut : True) | BOOLEAN | Oui | True ou False |
| `retain_first_frame` | Conserver la première image I2V dans chaque fenêtre de contexte (peut aider à conserver la référence initiale). (défaut : False) | BOOLEAN | Oui | True ou False |
| `split_conds_to_windows` | Indique si les multiples conditionnements (créés par ConditionCombine) doivent être répartis dans chaque fenêtre en fonction de l'index de région. (défaut : False) | BOOLEAN | Oui | True ou False |

**Remarque :** `context_stride` affecte uniquement les planifications uniformes, et `closed_loop` ne s'applique qu'aux planifications en boucle. `context_length` doit suivre le modèle 4n + 1. Le nœud convertit `context_length` et `context_overlap` d'images réelles en unités de modèle avant de les appliquer, en imposant un minimum de 1 pour `context_length` et de 0 pour `context_overlap`. Les entrées `context_stride`, `closed_loop`, `freenoise` et `split_conds_to_windows` sont des options avancées.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle avec la configuration de fenêtre de contexte appliquée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/fr.md)

---
**Source fingerprint (SHA-256):** `cf4927371e9d4b509f2e6e5319cd6109e3ef36da6b3faee278bcf8c906672857`
