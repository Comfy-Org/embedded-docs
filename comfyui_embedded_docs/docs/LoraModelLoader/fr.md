> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/fr.md)

Le nœud LoraModelLoader applique les pondérations d'un LoRA (Adaptation de Bas Rang) entraîné à un modèle de diffusion. Il modifie le modèle de base en chargeant les pondérations LoRA depuis un modèle LoRA entraîné et en ajustant leur intensité d'influence. Cela permet de personnaliser le comportement des modèles de diffusion sans avoir à les réentraîner entièrement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle de diffusion auquel le LoRA sera appliqué. |
| `lora` | LORA_MODEL | Oui | - | Le modèle LoRA à appliquer au modèle de diffusion. |
| `intensité_modèle` | FLOAT | Oui | -100.0 à 100.0 | L'intensité de modification du modèle de diffusion. Cette valeur peut être négative (par défaut : 1.0). |
| `bypass` | BOOLEAN | Oui | Vrai ou Faux | Lorsqu'il est activé, applique le LoRA en mode bypass sans modifier les pondérations du modèle de base. Utile pour l'entraînement et lorsque les pondérations du modèle sont déchargées (par défaut : Faux). |

**Remarque :** Lorsque `strength_model` est défini sur 0, le nœud renvoie le modèle d'origine sans appliquer aucune modification LoRA.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `modèle` | MODEL | Le modèle de diffusion modifié avec les pondérations LoRA appliquées. |

---
**Source fingerprint (SHA-256):** `82afa7dbbc990f1a9f202f920aaf8fad7fe69dc35e75ed8a95eb63c9dec74961`
