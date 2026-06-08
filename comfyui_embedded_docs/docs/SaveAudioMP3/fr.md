Le nœud SaveAudioMP3 enregistre des données audio sous forme de fichier MP3. Il prend une entrée audio et l'exporte vers le répertoire de sortie spécifié avec des paramètres personnalisables de nom de fichier et de qualité. Le nœud gère automatiquement la dénomination des fichiers et la conversion de format pour créer un fichier MP3 lisible.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio` | Les données audio à enregistrer sous forme de fichier MP3 | AUDIO | Oui | - |
| `préfixe_nom_fichier` | Le préfixe pour le nom du fichier de sortie (par défaut : "audio/ComfyUI") | STRING | Non | - |
| `qualité` | Le réglage de qualité audio pour le fichier MP3 (par défaut : "V0") | STRING | Non | "V0"<br>"128k"<br>"320k" |
| `prompt` | Données internes de l'invite (fournies automatiquement par le système) | PROMPT | Non | - |
| `extra_pnginfo` | Informations PNG supplémentaires (fournies automatiquement par le système) | EXTRA_PNGINFO | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| *Aucun* | Ce nœud ne renvoie aucune donnée de sortie, mais enregistre le fichier audio dans le répertoire de sortie | - |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/fr.md)

---
**Source fingerprint (SHA-256):** `70b960cc9c86ad9a4c98e643f40e6caaafdeb9840ac72a5f8e59533fd6120e3e`
