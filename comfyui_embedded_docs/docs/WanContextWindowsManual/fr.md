Le nœud WAN Context Windows (Manuel) vous permet de configurer manuellement les fenêtres de contexte pour les modèles de type WAN avec un traitement bidimensionnel. Il applique des paramètres personnalisés de fenêtre de contexte lors de l'échantillonnage en spécifiant la longueur de la fenêtre, le chevauchement, la méthode de planification et la technique de fusion. Cela vous offre un contrôle précis sur la manière dont le modèle traite les informations dans différentes régions de contexte.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel appliquer les fenêtres de contexte lors de l'échantillonnage. | MODEL | Oui | - |
| `longueur de contexte` | La longueur de la fenêtre de contexte (par défaut : 81). | INT | Oui | 1 à 1048576 |
| `chevauchement de contexte` | Le chevauchement de la fenêtre de contexte (par défaut : 30). | INT | Oui | 0 à 1048576 |
| `planification de contexte` | Le pas de la fenêtre de contexte. | COMBO | Oui | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `pas de contexte` | Le pas de la fenêtre de contexte ; applicable uniquement aux planifications uniformes (par défaut : 1). | INT | Oui | 1 à 1048576 |
| `boucle_fermée` | Indique s'il faut fermer la boucle de la fenêtre de contexte ; applicable uniquement aux planifications en boucle (par défaut : False). | BOOLEAN | Oui | - |
| `méthode_de_fusion` | La méthode à utiliser pour fusionner les fenêtres de contexte (par défaut : "pyramid"). | COMBO | Oui | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` |
| `freenoise` | Indique s'il faut appliquer le brassage de bruit FreeNoise, améliore le mélange des fenêtres (par défaut : False). | BOOLEAN | Oui | - |

**Remarque :** Le paramètre `context_stride` n'affecte que les planifications uniformes, et `closed_loop` ne s'applique qu'aux planifications en boucle. Les valeurs de longueur de contexte et de chevauchement sont automatiquement ajustées pour garantir des valeurs minimales valides lors du traitement. Le paramètre `fuse_method` inclut désormais des options supplémentaires au-delà de "pyramid".

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle avec la configuration de fenêtre de contexte appliquée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/fr.md)

---
**Source fingerprint (SHA-256):** `33e539f1e6647a6a2bc98fadc357a25279b0900746f5b3d568e2782cdb770258`
