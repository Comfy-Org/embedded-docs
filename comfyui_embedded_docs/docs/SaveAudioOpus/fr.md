# Enregistrer Audio (Opus)

Le nœud SaveAudioOpus enregistre des données audio dans un fichier au format Opus. Il prend une entrée audio et l'exporte sous forme de fichier Opus compressé avec des paramètres de qualité configurables. Ce nœud est obsolète et pourrait être supprimé dans les versions futures.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `audio` | Les données audio à enregistrer sous forme de fichier Opus. Le nœud génère une erreur si aucune donnée audio n'est fournie (par exemple, lorsque la vidéo source n'a pas de piste audio). | AUDIO | Oui | - |
| `filename_prefix` | Le préfixe du nom de fichier de sortie (par défaut : "audio/ComfyUI") | STRING | Non | - |
| `quality` | Le réglage de qualité audio (débit binaire) pour le fichier Opus (par défaut : "128k") | COMBO | Non | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `audio` | Les données audio d'entrée, renvoyées après l'enregistrement du fichier Opus sur le disque. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/fr.md)

---
**Source fingerprint (SHA-256):** `a2f585f45299759738fa85f6b73f51680d4e86da57d3fc9c2236e66114fa3d6c`
