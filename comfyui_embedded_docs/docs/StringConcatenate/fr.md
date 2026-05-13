> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringConcatenate/fr.md)

Le nœud StringConcatenate combine deux chaînes de texte en une seule en les joignant avec un délimiteur spécifié. Il prend deux chaînes d’entrée et un caractère ou une chaîne de délimiteur, puis produit une seule chaîne où les deux entrées sont reliées avec le délimiteur placé entre elles.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `string_a` | STRING | Oui | - | La première chaîne de texte à concaténer |
| `string_b` | STRING | Oui | - | La deuxième chaîne de texte à concaténer |
| `délimiteur` | STRING | Non | - | Le caractère ou la chaîne à insérer entre les deux chaînes d’entrée (par défaut : chaîne vide) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | STRING | La chaîne combinée avec le délimiteur inséré entre string_a et string_b |

---
**Source fingerprint (SHA-256):** `8e33665fb14a53f6c3bbfb6a4553ac7effa96d7d16d9ab2a9d4a1249abfc62e4`
