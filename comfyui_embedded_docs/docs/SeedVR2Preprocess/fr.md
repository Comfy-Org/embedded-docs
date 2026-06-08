# Pré-traiter l'entrée SeedVR2

Ce nœud ajoute un remplissage à une image redimensionnée pour la préparer au modèle SeedVR2. Il supprime le canal alpha lors du traitement, lequel est ensuite restauré par le nœud compagnon Post-traiter la sortie SeedVR2 en utilisant l'image redimensionnée d'origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `resized_images` | L'image redimensionnée à traiter. | IMAGE | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `images` | L'image avec remplissage prête pour le traitement SeedVR2. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/fr.md)

---
**Source fingerprint (SHA-256):** `b8135d0e27f75a673f52d080c6704de8cc86d15b5d16eca055d55e2d20837dc7`
