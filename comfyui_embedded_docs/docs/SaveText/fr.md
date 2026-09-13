# Enregistrer le texte

Le nœud Save Text écrit du contenu textuel dans un fichier du répertoire de sortie. Il prend en charge l'enregistrement aux formats .txt, .csv, .md ou .json et gère automatiquement la mise en forme lisible du JSON lorsqu'un JSON valide est fourni.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `text` | Le contenu textuel à enregistrer dans un fichier. Cette entrée doit être connectée à un autre nœud. | STRING | Oui | - |
| `filename_prefix` | Préfixe du nom de fichier de sortie. Un compteur à 5 chiffres est ajouté pour éviter d'écraser des fichiers existants (par défaut : "ComfyUI"). | STRING | Non | - |
| `format` | Format de fichier dans lequel enregistrer le texte (par défaut : "txt"). Lorsque "json" est sélectionné, un texte JSON valide est formaté avec une indentation de 2 espaces ; sinon, le texte est enregistré tel quel. | COMBO | Non | `"txt"`<br>`"csv"`<br>`"md"`<br>`"json"` |

### Remarques

- `text` est une entrée forcée et doit être connectée à un autre nœud ; elle ne peut pas être saisie directement.
- Le fichier enregistré est nommé `<filename_prefix>_<5-digit counter>.<extension>` et est écrit dans le répertoire de sortie de ComfyUI (dans un sous-dossier dérivé du préfixe).
- La sélection du format `"json"` tente d'analyser le texte comme du JSON. Si l'analyse réussit, le contenu est écrit avec une mise en forme lisible et une indentation de 2 espaces ; si l'analyse échoue, le texte brut est écrit sans modification.
- Le nœud renvoie le fichier enregistré à l'interface afin qu'il apparaisse avec les autres fichiers de sortie générés.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `text` | Le contenu textuel d'origine qui a été enregistré dans le fichier | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/fr.md)

---
**Source fingerprint (SHA-256):** `09bd896cab770358132834892c1b37efd2ffa0cb0aa7b02b7ef91163331dc9b1`
