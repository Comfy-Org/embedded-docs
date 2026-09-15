# Supprimer l’arrière-plan

## Aperçu

Le nœud Remove Background génère un masque de premier plan qui sépare le sujet principal de l'arrière-plan d'une image d'entrée. Il utilise un modèle de suppression d'arrière-plan pour analyser l'image et produire un masque mettant en évidence les éléments de premier plan.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle_de_suppression_arrière-plan` | Modèle de suppression d'arrière-plan utilisé pour générer le masque | BACKGROUND_REMOVAL_MODEL | Oui | N/A |
| `image` | Image d'entrée dont il faut supprimer l'arrière-plan | IMAGE | Oui | N/A |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mask` | Masque de premier plan généré | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/fr.md)

---
**Source fingerprint (SHA-256):** `75b415acedaeaa1a694aeba2e4b0367524c6878e3e4a1f48b2a62898c68109f9`
