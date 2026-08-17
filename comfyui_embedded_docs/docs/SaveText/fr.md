# Enregistrer le texte

Le nœud Save Text écrit le contenu textuel dans un fichier du répertoire de sortie. Il prend en charge l'enregistrement aux formats .txt, .csv, .md ou .json, et gère automatiquement la mise en forme du JSON lorsqu'un JSON valide est fourni.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `text` | Le contenu textuel à enregistrer dans un fichier. Cette entrée doit être connectée depuis un autre nœud. | STRING | Oui | - |
| `filename_prefix` | Préfixe du nom de fichier de sortie. Un compteur à 5 chiffres est ajouté pour éviter d'écraser les fichiers existants (par défaut : « ComfyUI »). | STRING | Non | - |
| `format` | Le format de fichier dans lequel enregistrer le texte (par défaut : « txt »). Lorsque « json » est sélectionné, le texte JSON valide est mis en forme avec une indentation de 2 espaces ; sinon, le texte est enregistré tel quel. | COMBO | Non | `"txt"`<br>`"csv"`<br>`"md"`<br>`"json"` |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `text` | Le contenu textuel d'origine qui a été enregistré dans le fichier | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/fr.md)

---
**Source fingerprint (SHA-256):** `09bd896cab770358132834892c1b37efd2ffa0cb0aa7b02b7ef91163331dc9b1`
