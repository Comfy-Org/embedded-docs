# Load LoRA (Text Encoder)

Applique une pile de LoRAs à un encodeur de texte CLIP dans un seul nœud. Chaque ligne de `loras` contient un fichier LoRA, sa force et un interrupteur marche/arrêt, et les lignes sont appliquées de haut en bas, de sorte que chaque ligne applique un patch au résultat de la ligne précédente. Les fichiers LoRA qui modifient l'encodeur de texte sont généralement aussi appliqués au modèle, donc ce nœud est normalement associé à Load LoRA (Model) en utilisant les mêmes lignes.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | L'encodeur de texte CLIP auquel les LoRAs seront appliqués. | CLIP | Oui | - |
| `loras` | Groupe extensible de LoRAs, appliqué à l'encodeur de texte dans l'ordre des lignes (`loras.0`, `loras.1`, etc.). Ajoutez une ligne par LoRA ; chaque ligne contient un fichier, une force et un interrupteur marche/arrêt. | DYNAMIC_GROUP | Oui | 1 à 20 lignes |

### Champs de ligne de `loras`

Chaque ligne reprend les champs suivants, et chaque champ est requis dans une ligne soumise.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `lora_name` | Le nom du fichier LoRA à appliquer. | COMBO | Oui | Plusieurs options disponibles |
| `strength` | Force d'application de ce LoRA à l'encodeur de texte. `0` le désactive, et une valeur négative inverse l'effet. (par défaut : 1.0) | FLOAT | Oui | -100 à 100 (pas de 0.01) |
| `enabled` | Désactivez pour ignorer ce LoRA sans modifier son fichier ni sa force. (par défaut : true) | BOOLEAN | Oui | false / true |

### Contraintes des paramètres

- **Nombre de lignes :** au moins une ligne doit être soumise et au plus 20 lignes sont acceptées, donc l'indice de ligne le plus élevé est 19.
- **Lignes ignorées :** une ligne est ignorée lorsque son fichier est vide, lorsque `enabled` est désactivé, ou lorsque `strength` vaut `0`. Une force négative est transmise plutôt qu'ignorée.
- **Ordre des lignes :** les lignes sont appliquées dans l'ordre où elles apparaissent, et chaque ligne part de l'encodeur de texte renvoyé par la ligne précédente.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CLIP` | L'encodeur de texte CLIP après application des lignes de LoRA qui ne sont pas ignorées. | CLIP |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLoraTextEncoder/fr.md)

---
**Source fingerprint (SHA-256):** `0b290d2caddc3937e962e65c70a5c99cbd4cdb40ab6f86bba8f0c270e5cebf00`
