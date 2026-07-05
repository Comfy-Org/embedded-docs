# FreeU_V2

Le nœud FreeU_V2 améliore la qualité de génération d'images en appliquant des modifications basées sur les fréquences à l'architecture U-Net d'un modèle de diffusion. Il utilise des facteurs d'échelle configurables pour ajuster les canaux de caractéristiques dans différents blocs, améliorant ainsi la sortie sans nécessiter d'entraînement supplémentaire.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de diffusion auquel appliquer l'amélioration FreeU | MODEL | Oui | - |
| `b1` | Facteur d'échelle des caractéristiques du backbone pour le premier bloc (par défaut : 1,3) | FLOAT | Oui | 0,0 - 10,0 |
| `b2` | Facteur d'échelle des caractéristiques du backbone pour le deuxième bloc (par défaut : 1,4) | FLOAT | Oui | 0,0 - 10,0 |
| `s1` | Facteur d'échelle des caractéristiques de saut pour le premier bloc (par défaut : 0,9) | FLOAT | Oui | 0,0 - 10,0 |
| `s2` | Facteur d'échelle des caractéristiques de saut pour le deuxième bloc (par défaut : 0,2) | FLOAT | Oui | 0,0 - 10,0 |


| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle de diffusion amélioré avec les modifications FreeU appliquées | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU_V2/fr.md)

---
**Source fingerprint (SHA-256):** `40ded64177e8e00cc5d8d5dde35c20958a77c500dada725572b64484c5ce1045`
