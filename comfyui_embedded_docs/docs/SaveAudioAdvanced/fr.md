# Enregistrer l’Audio (Avancé)

---

Enregistre l'audio d'entrée dans votre répertoire de sortie ComfyUI. Ce nœud vous permet d'exporter l'audio dans divers formats, notamment FLAC, MP3 et Opus, avec des paramètres de qualité configurables.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `audio` | L'audio à enregistrer. | AUDIO | Oui | - |
| `préfixe_nom_fichier` | Le préfixe du fichier à enregistrer. Peut inclure des jetons de formatage tels que %date:yyyy-MM-dd%. (par défaut : « audio/ComfyUI ») | STRING | Oui | - |
| `format` | Le format de fichier dans lequel enregistrer l'audio. | DYNAMIC_COMBO | Oui | « flac »<br>« mp3 »<br>« opus » |

### Entrées MP3

Lorsque « mp3 » est sélectionné comme format, le paramètre suivant devient disponible.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `quality` | La qualité d'encodage du fichier MP3 de sortie. (par défaut : « V0 ») | COMBO | Non | « V0 »<br>« 128k »<br>« 320k » |

### Entrées Opus

Lorsque « opus » est sélectionné comme format, le paramètre suivant devient disponible.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `quality` | La qualité d'encodage du fichier Opus de sortie. (par défaut : « 128k ») | COMBO | Non | « 64k »<br>« 96k »<br>« 128k »<br>« 192k »<br>« 320k » |

Remarque : Le paramètre `quality` n'est disponible que lorsque le format correspondant est sélectionné. Lorsque « flac » est sélectionné, aucun paramètre de qualité supplémentaire n'est disponible.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `audio` | L'audio d'entrée, transmis sans modification après avoir été enregistré. | AUDIO |

Le nœud renvoie également des informations d'interface contenant les informations sur le fichier audio enregistré.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `5f3af49670b485bbd31f0ed0c5667c12e9b9b23014cadcf64442a486255d0e6d`
