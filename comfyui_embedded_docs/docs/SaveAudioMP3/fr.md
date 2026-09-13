# Enregistrer Audio (MP3)

Le nœud SaveAudioMP3 sauvegarde les données audio dans un fichier MP3. Il prend une entrée audio et l'exporte vers le répertoire de sortie avec un nom de fichier et un réglage de qualité personnalisables, en gérant automatiquement le nommage des fichiers et la conversion au format MP3. **Ce nœud est obsolète et pourra être supprimé dans les versions futures.**

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `audio` | Les données audio à sauvegarder dans un fichier MP3 | AUDIO | Oui | - |
| `filename_prefix` | Le préfixe du nom de fichier de sortie (par défaut : "audio/ComfyUI") | STRING | Non | - |
| `quality` | Le réglage de qualité audio du fichier MP3 (par défaut : "V0") | COMBO | Non | `"V0"`<br>`"128k"`<br>`"320k"` |
| `prompt` | Données de prompt internes, fournies automatiquement par le système | PROMPT | Non | - |
| `extra_pnginfo` | Informations PNG supplémentaires, fournies automatiquement par le système | EXTRA_PNGINFO | Non | - |

**Remarque :** Si l'entrée `audio` est None (par exemple, lorsque la vidéo source ne contient pas de piste audio), le nœud lève une ValueError.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `audio` | Les données audio qui ont été sauvegardées dans un fichier MP3 | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/fr.md)

---
**Source fingerprint (SHA-256):** `7d3b439dfd7cb211dd6568f6b5124bb225909dcf0ae150addc4ca226d947a4f0`
