# Flux Essayage Virtuel

Ce nœud effectue un essayage virtuel en habillant une personne avec une image de vêtement fournie. Il envoie les images de la personne et du vêtement au service BFL Flux VTO, qui génère une image réaliste de la personne portant le vêtement. Une instruction textuelle facultative peut décrire comment le vêtement doit s'ajuster ou à quoi il doit ressembler.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `person` | Image de la personne à habiller. | IMAGE | Oui | - |
| `garment` | Image du vêtement à appliquer. | IMAGE | Oui | - |
| `prompt` | Instruction de style facultative en langage naturel (par ex. comment le vêtement doit s'ajuster). La valeur par défaut est une chaîne vide. | STRING | Non | - |
| `seed` | La graine aléatoire utilisée pour créer le bruit. Valeur par défaut : 0. | INT | Non | 0 à 18446744073709551615 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image obtenue montrant la personne portant le vêtement fourni. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVTONode/fr.md)

---
**Source fingerprint (SHA-256):** `5e0777dedcbd6275e31a16f6f5d78f4166147266c0c88531c5843a027702e594`
