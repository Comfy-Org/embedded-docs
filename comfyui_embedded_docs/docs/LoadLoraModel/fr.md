# Load LoRA (Model)

Appliquez une pile de LoRAs à un modèle de diffusion dans un seul nœud. Chaque ligne de `loras` contient un fichier LoRA, sa force et un interrupteur marche/arrêt, et les lignes sont appliquées de haut en bas, de sorte que chaque ligne applique son patch au résultat de la ligne du dessus. Utilisez ce nœud au lieu d'enchaîner plusieurs chargeurs de LoRA uniques lorsqu'un flux de travail applique une longue liste de LoRAs au même modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion auquel les LoRAs seront appliqués. | MODEL | Oui | - |
| `loras` | Groupe extensible de LoRAs, appliqués au modèle dans l'ordre des lignes (`loras.0`, `loras.1`, etc.). Ajoutez une ligne par LoRA ; chaque ligne contient un fichier, une force et un interrupteur marche/arrêt. | DYNAMIC_GROUP | Oui | 1 à 20 lignes |

### Champs de ligne de `loras`

Chaque ligne répète les champs suivants, et chaque champ est requis dans une ligne soumise.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `lora_name` | Le nom du fichier LoRA à appliquer. | COMBO | Oui | Plusieurs options disponibles |
| `strength` | Force d'application de ce LoRA. `0` le désactive, et une valeur négative inverse l'effet. (valeur par défaut : 1.0) | FLOAT | Oui | -100 à 100 (pas 0.01) |
| `enabled` | Désactivez pour ignorer ce LoRA sans modifier son fichier ni sa force. (valeur par défaut : true) | BOOLEAN | Oui | false / true |

### Contraintes des paramètres

- **Nombre de lignes :** au moins une ligne doit être soumise et au plus 20 lignes sont acceptées, donc l'indice de ligne le plus élevé est 19.
- **Lignes ignorées :** une ligne est ignorée lorsque son fichier est vide, lorsque `enabled` est désactivé, ou lorsque `strength` vaut `0`. Une force négative est transmise plutôt qu'ignorée.
- **Ordre des lignes :** les lignes sont appliquées dans l'ordre où elles apparaissent, et chaque ligne part du modèle renvoyé par la ligne précédente.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le modèle de diffusion avec chaque ligne de LoRA activée appliquée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLoraModel/fr.md)

---
**Source fingerprint (SHA-256):** `a656bba0248d2f6d4eb65e15e3a19f2e76edecd4b34710921a02f3ba5c598e1d`
