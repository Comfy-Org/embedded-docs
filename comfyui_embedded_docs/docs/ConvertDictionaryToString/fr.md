# Convertir un dictionnaire en chaîne

Ce nœud convertit un dictionnaire (une collection de paires clé-valeur) en une chaîne de texte, généralement au format JSON. Vous pouvez contrôler le niveau d'indentation pour rendre la sortie plus lisible ou plus compacte.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `dictionnaire` | Le dictionnaire à convertir en chaîne de caractères | DICT | Oui | - |
| `indentation` | Espaces par niveau d'indentation. 0 produit une chaîne compacte sur une seule ligne (par défaut : 2) | INT | Non | 0 à 8 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `STRING` | Le dictionnaire converti en une chaîne au format JSON | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConvertDictionaryToString/fr.md)

---
**Source fingerprint (SHA-256):** `ae4e9889d5347acfc69166bac66f2ba63f5cd37dafab25a9e0aff6bfe7381219`
