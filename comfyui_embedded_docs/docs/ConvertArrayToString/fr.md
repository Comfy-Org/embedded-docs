# Convertir un tableau en chaîne

Le nœud Convert Array to String prend un tableau (liste) d'éléments et le convertit en une chaîne JSON formatée. Cela est utile lorsque vous devez sérialiser des données de tableau pour les afficher, les journaliser ou les transmettre à d'autres systèmes qui attendent une entrée de type chaîne.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `tableau` | Le tableau à convertir en chaîne JSON | ARRAY | Oui | - |
| `indentation` | Espaces par niveau d'indentation. 0 produit une chaîne compacte sur une seule ligne (par défaut : 2) | INT | Non | 0 à 8 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `STRING` | Le tableau converti en chaîne formatée JSON | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConvertArrayToString/fr.md)

---
**Source fingerprint (SHA-256):** `ac8397fed0336f546403ee3e1f17d7e8f5973190b102e74943f098bf6905f726`
