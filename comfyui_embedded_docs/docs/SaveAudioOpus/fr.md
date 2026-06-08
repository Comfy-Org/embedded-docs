Le nœud SaveAudioOpus enregistre des données audio dans un fichier au format Opus. Il prend une entrée audio et l'exporte sous forme de fichier Opus compressé avec des paramètres de qualité configurables. Le nœud gère automatiquement le nommage des fichiers et enregistre la sortie dans le répertoire de sortie désigné.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio` | Les données audio à enregistrer sous forme de fichier Opus | AUDIO | Oui | - |
| `préfixe_nom_fichier` | Le préfixe pour le nom du fichier de sortie (par défaut : "audio/ComfyUI") | STRING | Non | - |
| `qualité` | Le paramètre de qualité audio pour le fichier Opus (par défaut : "128k") | COMBO | Non | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| - | Ce nœud ne renvoie aucune valeur de sortie. Sa fonction principale est d'enregistrer le fichier audio sur le disque. | - |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/fr.md)

---
**Source fingerprint (SHA-256):** `87c3b1b85ca51b79d43c8486eeb2de7b074faa11c4da2bff7b8931a3049560e2`
