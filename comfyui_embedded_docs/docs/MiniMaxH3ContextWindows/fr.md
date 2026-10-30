# MiniMax H3 Context Windows

Divise l'échantillonnage en fenêtres de contexte chevauchantes afin qu'une vidéo MiniMax H3 puisse être plus longue que la fenêtre de passage unique du modèle. Les fenêtres sont placées sur les blocs de 17 images du modèle, ce qui maintient l'alignement de la vidéo et de l'audio générés aux limites des fenêtres. Connectez le modèle renvoyé à l'échantillonneur à la place du modèle d'origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle auquel appliquer des fenêtres de contexte pendant l'échantillonnage. | MODEL | Oui | - |
| `context_length` | La longueur de la fenêtre de contexte en images réelles. Doit être 17*n + 5 (par défaut : 124). | INT | Oui | 22 à 16384 (MAX_RESOLUTION), pas de 17 |
| `context_overlap` | Le chevauchement de la fenêtre de contexte en images réelles. Doit être 17*n + 5 (par défaut : 39). | INT | Oui | 5 ou plus, pas de 17 |
| `fuse_method` | La méthode utilisée pour fusionner les fenêtres de contexte (par défaut : `"pyramid"`). | COMBO | Oui | `"pyramid"`<br>`"relative"`<br>`"flat"`<br>`"overlap-linear"` |
| `freenoise` | Indique s'il faut appliquer la permutation du bruit FreeNoise, qui améliore le mélange des fenêtres (par défaut : True, paramètre avancé). | BOOLEAN | Oui | true<br>false |
| `split_conds_to_windows` | Indique s'il faut répartir plusieurs conditionnements (créés par ConditionCombine) vers chaque fenêtre en fonction de l'indice de région (par défaut : False, paramètre avancé). | BOOLEAN | Oui | true<br>false |

Les deux longueurs sont indiquées en images réelles et converties en latents avant l'échantillonnage : `context_length` devient 2 latents pour 5 images ou moins, sinon `((frames - 5) / 17) * 5 + 2`. `context_overlap` est converti de la même manière, puis plafonné à `context_length` moins 5, de sorte que le chevauchement laisse toujours un bloc complet à avancer. Le nœud utilise toujours la planification statique avec un pas de 1, applique les fenêtres sur la dimension temporelle latente et n'ajoute pas l'image de correction causale, car chaque fenêtre commence sur une limite de bloc. `split_conds_to_windows` attend plusieurs conditionnements créés par le nœud ConditionCombine.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle avec la configuration de fenêtres de contexte appliquée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ContextWindows/fr.md)

---
**Source fingerprint (SHA-256):** `e9e019d0bc870abfe226ef1aafb2607f55c0cc1b297884db35fe98c465cc0d91`
