> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CaseConverter/fr.md)

Voici la traduction en français de la documentation du nœud Case Converter :

Le nœud Case Converter transforme les chaînes de texte en différents formats de casse. Il prend une chaîne d'entrée et la convertit en fonction du mode sélectionné, produisant une chaîne de sortie avec la mise en forme de casse spécifiée appliquée. Le nœud prend en charge quatre options de conversion de casse différentes pour modifier la capitalisation de votre texte.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `string` | STRING | Oui | - | La chaîne de texte à convertir dans un format de casse différent |
| `mode` | STRING | Oui | `"UPPERCASE"`<br>`"lowercase"`<br>`"Capitalize"`<br>`"Title Case"` | Le mode de conversion de casse à appliquer (par défaut : `"UPPERCASE"`) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | STRING | La chaîne d'entrée convertie dans le format de casse spécifié |

---
**Source fingerprint (SHA-256):** `2493daccd5bdd86ce3fb24c6658057f5e50c2d6ed7616785f40806826f9a60dc`
