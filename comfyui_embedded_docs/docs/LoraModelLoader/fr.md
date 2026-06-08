Le nœud LoraModelLoader applique les pondérations d'un LoRA (Adaptation de Bas Rang) entraîné à un modèle de diffusion. Il modifie le modèle de base en chargeant les pondérations LoRA depuis un modèle LoRA entraîné et en ajustant leur intensité d'influence. Cela permet de personnaliser le comportement des modèles de diffusion sans avoir à les réentraîner entièrement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de diffusion auquel le LoRA sera appliqué. | MODEL | Oui | - |
| `lora` | Le modèle LoRA à appliquer au modèle de diffusion. | LORA_MODEL | Oui | - |
| `intensité_modèle` | L'intensité de modification du modèle de diffusion. Cette valeur peut être négative (par défaut : 1.0). | FLOAT | Oui | -100.0 à 100.0 |
| `bypass` | Lorsqu'il est activé, applique le LoRA en mode bypass sans modifier les pondérations du modèle de base. Utile pour l'entraînement et lorsque les pondérations du modèle sont déchargées (par défaut : Faux). | BOOLEAN | Oui | Vrai ou Faux |

**Remarque :** Lorsque `strength_model` est défini sur 0, le nœud renvoie le modèle d'origine sans appliquer aucune modification LoRA.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle de diffusion modifié avec les pondérations LoRA appliquées. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/fr.md)

---
**Source fingerprint (SHA-256):** `82afa7dbbc990f1a9f202f920aaf8fad7fe69dc35e75ed8a95eb63c9dec74961`
