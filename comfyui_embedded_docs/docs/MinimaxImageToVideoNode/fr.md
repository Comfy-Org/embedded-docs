# MiniMax Image vers Vidéo

Voici la traduction en français de la documentation du nœud MinimaxImageToVideoNode :

Génère des vidéos de manière synchrone à partir d'une image et d'une description textuelle, ainsi que de paramètres optionnels, en utilisant l'API de MiniMax. Ce nœud prend une image d'entrée et une description textuelle pour créer une séquence vidéo, avec différentes options de modèle et paramètres de configuration disponibles.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | Image à utiliser comme première image de la génération vidéo | IMAGE | Oui | - |
| `texte d'invite` | Description textuelle pour guider la génération vidéo (par défaut : chaîne vide) | STRING | Oui | - |
| `modèle` | Modèle à utiliser pour la génération vidéo (par défaut : "I2V-01") | COMBO | Oui | "I2V-01-Director"<br>"I2V-01"<br>"I2V-01-live" |
| `graine` | La graine aléatoire utilisée pour créer le bruit (par défaut : 0) | INT | Non | 0 à 18446744073709551615 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La sortie vidéo générée | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `9ad1659352e363361f09d6a7a0e24835056b20cc84532247251f516b0ac284e8`
