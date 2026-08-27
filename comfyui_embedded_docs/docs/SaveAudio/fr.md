# EnregistrerAudio

Ce nœud enregistre des données audio dans un fichier au format FLAC. Il prend une entrée audio et l’écrit dans le répertoire de sortie en utilisant le préfixe de nom de fichier spécifié. Ce nœud est obsolète et doit être remplacé par le nœud Save Audio actuel.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `audio` | Les données audio à enregistrer | AUDIO | Oui | - |
| `préfixe_du_nom_de_fichier` | Le préfixe pour le nom du fichier de sortie (par défaut : "audio/ComfyUI") | STRING | Non | - |

*Remarque : les paramètres `prompt` et `extra_pnginfo` sont masqués et automatiquement gérés par le système.*

Si l’entrée `audio` ne reçoit aucune donnée (par exemple, lorsque la vidéo source n’a pas de piste audio), le nœud génère une erreur et aucun fichier n’est enregistré.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `audio` | Les données audio qui ont été fournies à l’entrée, transmises après l’enregistrement du fichier | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/fr.md)

---
**Source fingerprint (SHA-256):** `6ac62d315f14213091cd179a05f0bbd51f1b1a5056bb5c06ca137d2b574d6017`
