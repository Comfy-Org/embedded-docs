# ComfyCloudMageFlowTextToImageNode

Ce nœud génère une image à partir d'un prompt textuel en envoyant la requête au flux de travail texte-vers-image Mage-Flow dans le Comfy Cloud. Il exécute la passe de génération complète en 30 étapes plutôt que la passe turbo distillée plus rapide, et il accepte un prompt négatif pour décrire le contenu que vous ne souhaitez pas voir dans l'image finale. Le prompt négatif est pris en charge dans ce mode à 30 étapes ; d'après le résumé du nœud, la variante turbo distillée ne peut pas l'utiliser correctement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | La description textuelle de l'image à générer. | STRING | Oui | Free-form text |
| `negative_prompt` | Texte décrivant le contenu qui ne doit pas apparaître dans l'image générée. Ce paramètre est utilisé pendant la passe de génération standard à 30 étapes, mais la variante turbo distillée n'utilise pas efficacement les prompts négatifs. | STRING | Non | Free-form text |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image générée à partir du prompt textuel et du prompt négatif fournis. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTextToImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `80f4ecf1df3f2c46d94138f8ada817e12cc49e69e69a001630776ed644868367`
