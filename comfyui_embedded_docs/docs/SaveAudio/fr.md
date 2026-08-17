# EnregistrerAudio

Le nœud SaveAudio enregistre des données audio dans un fichier au format FLAC. Il prend une entrée audio, l'écrit dans le répertoire de sortie en utilisant le préfixe de nom de fichier spécifié, et transmet le même audio en sortie. Ce nœud est obsolète et doit être remplacé par le nœud Save Audio actuel.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `audio` | Les données audio à enregistrer | AUDIO | Oui | - |
| `filename_prefix` | Le préfixe pour le nom de fichier de sortie (par défaut : "audio/ComfyUI") | STRING | Non | - |

Le nœud génère une erreur si `audio` est None, ce qui peut se produire lorsque la vidéo source ne comporte pas de piste audio.

Les paramètres `prompt` et `extra_pnginfo` sont masqués et gérés automatiquement par le système.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `audio` | Les mêmes données audio que celles enregistrées dans le fichier | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/fr.md)

---
**Source fingerprint (SHA-256):** `6ac62d315f14213091cd179a05f0bbd51f1b1a5056bb5c06ca137d2b574d6017`
