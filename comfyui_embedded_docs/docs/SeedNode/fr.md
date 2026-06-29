# Graine

Le nœud Seed génère une valeur entière fixe ou aléatoire. Il est couramment utilisé pour contrôler la reproductibilité des opérations aléatoires dans d'autres nœuds en fournissant un point de départ cohérent pour leur génération de nombres aléatoires.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `graine` | La valeur de départ à utiliser. L'option de contrôle après génération détermine si la valeur reste fixe ou change après chaque génération. | INT | Oui | 0 à 9223372036854775807 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `graine` | La valeur de départ générée. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedNode/fr.md)

---
**Source fingerprint (SHA-256):** `19f9b22945bb152ff5066195067f1b6b4c006589f26c7533fad905044ac3b7fa`
