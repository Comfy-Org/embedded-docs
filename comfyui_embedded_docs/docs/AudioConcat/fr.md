> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioConcat/fr.md)

Voici la traduction en français de la documentation du nœud AudioConcat :

Le nœud AudioConcat combine deux entrées audio en les concaténant. Il prend deux entrées audio et les relie dans l'ordre que vous spécifiez, en plaçant le second audio avant ou après le premier. Le nœud gère automatiquement les différents formats audio en convertissant l'audio mono en stéréo et en adaptant les fréquences d'échantillonnage entre les deux entrées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `audio1` | AUDIO | Oui | - | La première entrée audio à concaténer |
| `audio2` | AUDIO | Oui | - | La seconde entrée audio à concaténer |
| `direction` | COMBO | Oui | `"after"`<br>`"before"` | Indique si audio2 doit être ajouté après ou avant audio1 (par défaut : "after") |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `AUDIO` | AUDIO | L'audio combiné contenant les deux fichiers audio d'entrée concaténés |

---
**Source fingerprint (SHA-256):** `b54046e29761cf27bc5b1c065dac87846613afc0b5cbb296632628bf7d4527b7`
