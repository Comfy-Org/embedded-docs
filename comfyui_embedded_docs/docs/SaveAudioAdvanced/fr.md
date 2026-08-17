# Enregistrer l’Audio (Avancé)

```markdown
# Enregistrer l'audio (avancé)

Enregistre l'audio d'entrée dans votre répertoire de sortie ComfyUI. Vous pouvez exporter l'audio aux formats FLAC, MP3 ou Opus, avec des paramètres de qualité sélectionnables pour les fichiers MP3 et Opus.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `format` | Le format de fichier dans lequel enregistrer l'audio. | DYNAMIC_COMBO | Oui | "flac"<br>"mp3"<br>"opus" |
| `audio` | L'audio à enregistrer. | AUDIO | Oui | - |
| `filename_prefix` | Le préfixe du fichier à enregistrer. Peut inclure des jetons de formatage tels que %date:yyyy-MM-dd%. (défaut : « audio/ComfyUI ») | STRING | Oui | - |

### Entrées flac

Le format `flac` ne nécessite aucun paramètre supplémentaire.

### Entrées mp3

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `quality` | La qualité d'encodage pour les fichiers MP3. (défaut : « V0 ») | COMBO | Oui | "V0"<br>"128k"<br>"320k" |

### Entrées opus

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `quality` | La qualité d'encodage pour les fichiers Opus. (défaut : « 128k ») | COMBO | Oui | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

**Remarque :** Le paramètre `quality` n'est affiché que lorsque `format` est `mp3` ou `opus`. Si aucune valeur `quality` n'est fournie, l'audio est enregistré avec la qualité par défaut du format sélectionné.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `audio` | L'audio d'entrée, transmis après avoir été enregistré. | AUDIO |
| `ui` | Sortie d'interface contenant les informations du fichier audio enregistré. | UI |
```

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `5f3af49670b485bbd31f0ed0c5667c12e9b9b23014cadcf64442a486255d0e6d`
