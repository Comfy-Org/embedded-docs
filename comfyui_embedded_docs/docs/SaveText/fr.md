# SaveText

Le nœud Save Text enregistre le contenu textuel dans un fichier situé dans le répertoire de sortie. Il prend en charge l'enregistrement dans trois formats de fichier différents : texte brut (.txt), Markdown (.md) et JSON (.json). Lors de l'enregistrement au format JSON, le nœud tente d'analyser le texte saisi en tant que JSON valide et de le formater avec une indentation appropriée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `text` | Le contenu textuel à enregistrer dans un fichier | STRING | Oui | |
| `filename_prefix` | Préfixe pour le nom du fichier de sortie (par défaut : "ComfyUI") | STRING | Non | |
| `format` | Format de fichier pour enregistrer le texte (par défaut : "txt") | STRING | Non | `"txt"`<br>`"md"`<br>`"json"` |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `text` | Le contenu textuel d'origine qui a été enregistré dans le fichier | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/fr.md)

---
**Source fingerprint (SHA-256):** `5644d143f415773115b38d7af6d9afea20c9eadef2cea836b0384c15e0dcba6a`
