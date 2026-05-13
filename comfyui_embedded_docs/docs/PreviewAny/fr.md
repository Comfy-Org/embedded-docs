> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/fr.md)

Le nœud PreviewAny affiche un aperçu de tout type de données d’entrée au format texte. Il accepte tout type de données en entrée et les convertit en une représentation textuelle lisible. Le nœud gère automatiquement différents types de données, notamment les chaînes de caractères, les nombres, les booléens et les objets complexes, en tentant de les sérialiser au format JSON.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `source` | ANY | Oui | Tout type de données | Accepte tout type de données d’entrée pour l’affichage de l’aperçu |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `UI Text Display` | STRING | Affiche les données d’entrée converties au format texte dans l’interface utilisateur. Renvoie également le texte sous forme de chaîne de caractères pour un traitement ultérieur. |

---
**Source fingerprint (SHA-256):** `6011c39a31ef9a6786a1dff6e135edcf35def2f715b49301dd49a6467f859271`
