# Concaténer Audio

Voici la traduction en français de la documentation du nœud AudioConcat :

Le nœud AudioConcat combine deux entrées audio en les concaténant. Il prend deux entrées audio et les relie dans l'ordre que vous spécifiez, en plaçant le second audio avant ou après le premier. Le nœud gère automatiquement les différents formats audio en convertissant l'audio mono en stéréo et en adaptant les fréquences d'échantillonnage entre les deux entrées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio1` | La première entrée audio à concaténer | AUDIO | Oui | - |
| `audio2` | La seconde entrée audio à concaténer | AUDIO | Oui | - |
| `direction` | Indique si audio2 doit être ajouté après ou avant audio1 (par défaut : "after") | COMBO | Oui | `"after"`<br>`"before"` |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `AUDIO` | L'audio combiné contenant les deux fichiers audio d'entrée concaténés | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioConcat/fr.md)

---
**Source fingerprint (SHA-256):** `b54046e29761cf27bc5b1c065dac87846613afc0b5cbb296632628bf7d4527b7`
