# Enregistrer le texte

Le nœud Enregistrer le texte écrit le contenu textuel dans un fichier situé dans le répertoire de sortie. Il prend en charge l'enregistrement aux formats .txt, .md ou .json, et gère automatiquement la mise en forme JSON (pretty-printing) lorsque du JSON valide est fourni.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `text` | Le contenu texte à enregistrer dans un fichier. Cette entrée doit être connectée depuis un autre nœud. | STRING | Oui | - |
| `filename_prefix` | Préfixe du nom de fichier de sortie. Un compteur à 5 chiffres est ajouté pour éviter d'écraser les fichiers existants (par défaut : "ComfyUI"). | STRING | Non | - |
| `format` | Le format de fichier pour enregistrer le texte (par défaut : "txt"). Lorsque « json » est sélectionné, le texte JSON valide est mis en forme avec une indentation de 2 espaces ; sinon, le texte est enregistré tel quel. | COMBO | Non | `"txt"`<br>`"md"`<br>`"json"` |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `text` | Le contenu textuel d'origine qui a été enregistré dans le fichier | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/fr.md)

---
**Source fingerprint (SHA-256):** `5644d143f415773115b38d7af6d9afea20c9eadef2cea836b0384c15e0dcba6a`
