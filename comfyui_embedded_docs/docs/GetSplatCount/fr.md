# Obtenir le nombre de Splats

Le nœud Obtenir le Nombre de Splats renvoie le nombre total de splats (points gaussiens) dans un lot de splats, additionné pour tous les éléments du lot. Il transmet les données de splat d'origine sans modification tout en fournissant un compte du nombre de splats individuels qu'il contient.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `splat` | Les données de splat dont il faut compter le nombre de splats | SPLAT | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `nombre` | Les données de splat d'origine, transmises sans modification | SPLAT |
| `count` | Le nombre total de splats additionné sur l'ensemble du lot | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetSplatCount/fr.md)

---
**Source fingerprint (SHA-256):** `fbb913b70bbbe4701b91783b6f47969d9132737c464ae590243f9f38061a05dc`
