# Graine

Le nœud Seed fournit une valeur entière qui peut être utilisée comme graine pour contrôler la reproductibilité des opérations aléatoires dans d'autres nœuds. En fournissant une valeur de départ cohérente, il aide à garder des résultats reproductibles si nécessaire.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `graine` | La valeur de graine à utiliser. L'option de contrôle après génération détermine si la valeur reste fixe ou change après chaque génération ; dans ce nœud, elle est définie comme fixe. | INT | Oui | 0 à 9223372036854775807 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `graine` | La valeur de départ générée. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedNode/fr.md)

---
**Source fingerprint (SHA-256):** `19f9b22945bb152ff5066195067f1b6b4c006589f26c7533fad905044ac3b7fa`
