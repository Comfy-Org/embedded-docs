# Enregistrer Audio (MP3)

Le nœud SaveAudioMP3 enregistre les données audio sous forme de fichier MP3. Il prend une entrée audio et l'écrit dans le répertoire de sortie avec un préfixe de nom de fichier personnalisable et un paramètre de qualité. Ce nœud est obsolète et pourrait être supprimé dans les versions futures.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `audio` | Les données audio à enregistrer sous forme de fichier MP3 | AUDIO | Oui | - |
| `filename_prefix` | Le préfixe du nom de fichier de sortie (par défaut : "audio/ComfyUI") | STRING | Non | - |
| `quality` | Le paramètre de qualité d'encodage MP3 (par défaut : "V0"). V0 utilise un débit binaire variable pour une haute qualité ; 128k et 320k utilisent des débits binaires fixes de 128 et 320 kbps | COMBO | Non | `"V0"`<br>`"128k"`<br>`"320k"` |
| `prompt` | Données internes du prompt, fournies automatiquement par le système | PROMPT | Non | - |
| `extra_pnginfo` | Informations PNG supplémentaires, fournies automatiquement par le système | EXTRA_PNGINFO | Non | - |

**Remarque :** Si l'entrée `audio` est None (par exemple, lorsque la vidéo source n'a pas de piste audio), le nœud lève une ValueError.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `audio` | Les données audio qui ont été enregistrées sous forme de fichier MP3 | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/fr.md)

---
**Source fingerprint (SHA-256):** `7d3b439dfd7cb211dd6568f6b5124bb225909dcf0ae150addc4ca226d947a4f0`
