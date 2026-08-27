# Fenêtres de contexte WAN (Manuel)

Le nœud **WAN Context Windows (Manual)** vous permet de configurer manuellement les fenêtres de contexte pour les modèles vidéo de style Wan. Il applique ces paramètres pendant l'échantillonnage, vous donnant le contrôle sur la longueur des fenêtres, le chevauchement, la programmation et la méthode de fusion utilisés pendant que le modèle traite la vidéo. La longueur et le chevauchement du contexte sont spécifiés en images réelles et sont convertis en interne pour le traitement 2D du modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel appliquer les fenêtres de contexte pendant l'échantillonnage. | MODEL | Oui | - |
| `longueur de contexte` | La longueur de la fenêtre de contexte en images réelles. Doit être 4*n + 1 (défaut : 81). | INT | Oui | 1 à 16384 (MAX_RESOLUTION), pas de 4 |
| `chevauchement de contexte` | Le chevauchement de la fenêtre de contexte en images réelles (défaut : 30). | INT | Oui | 0 ou plus |
| `planification de contexte` | Algorithme de programmation dépendant de l'étape pour les fenêtres de contexte (défaut : "uniform_standard"). | COMBO | Oui | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `pas de contexte` | Le pas de la fenêtre de contexte ; applicable uniquement aux programmations uniformes (défaut : 1). | INT | Oui | 1 ou plus |
| `boucle_fermée` | Indique s'il faut fermer la boucle de la fenêtre de contexte ; applicable uniquement aux programmations en boucle (défaut : False). | BOOLEAN | Oui | - |
| `méthode_de_fusion` | La méthode à utiliser pour fusionner les fenêtres de contexte (défaut : "pyramid"). | COMBO | Oui | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` |
| `freenoise` | Indique s'il faut appliquer le mélange de bruit FreeNoise, améliore le fondu des fenêtres (défaut : True). | BOOLEAN | Oui | - |
| `conserver_première_image` | Conserver la première image I2V dans chaque fenêtre de contexte (peut aider à préserver la référence initiale) (défaut : False). | BOOLEAN | Oui | - |
| `diviser_conditions_fenêtres` | Indique s'il faut diviser plusieurs conditionnements (créés par ConditionCombine) pour chaque fenêtre en fonction de l'index de région (défaut : False). | BOOLEAN | Oui | - |

**Remarque :** `context_stride` n'affecte que les programmations uniformes, et `closed_loop` ne s'applique qu'aux programmations en boucle. La longueur et le chevauchement du contexte sont spécifiés en images réelles et sont automatiquement convertis et limités aux valeurs minimales valides pendant le traitement (`context_length` devient ((length - 1) / 4) + 1, `context_overlap` devient overlap / 4). `context_length` doit suivre la forme 4*n + 1. `retain_first_frame` est destiné à une utilisation image-vers-vidéo. `split_conds_to_windows` attend plusieurs conditionnements créés par le nœud ConditionCombine. Le paramètre `fuse_method` inclut plusieurs options au-delà de « pyramid ».

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle avec la configuration de fenêtres de contexte appliquée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/fr.md)

---
**Source fingerprint (SHA-256):** `cf4927371e9d4b509f2e6e5319cd6109e3ef36da6b3faee278bcf8c906672857`
