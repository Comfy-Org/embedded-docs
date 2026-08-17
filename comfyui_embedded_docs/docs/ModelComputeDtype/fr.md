# ModelComputeDtype

---

Le nœud ModelComputeDtype modifie le type de données de calcul (précision) utilisé par un modèle pendant le traitement. Il crée une copie du modèle d'entrée et applique le paramètre de précision sélectionné, ce qui peut aider à optimiser l'utilisation de la mémoire et les performances selon votre matériel. Cela est utile pour déboguer et tester différentes configurations de précision.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle d'entrée à modifier avec un nouveau type de données de calcul. | MODEL | Oui | - |
| `dtype` | Le type de données de calcul à appliquer au modèle (par défaut : "default"). Ce paramètre est marqué comme un paramètre avancé dans l'interface. | COMBO | Oui | "default"<br>"fp32"<br>"fp16"<br>"bf16" |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec le nouveau type de données de calcul appliqué. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/fr.md)

---
**Source fingerprint (SHA-256):** `ad9c39e1217fd2e343ad4f49df9d1acabbc4708966dadec5340bb975adb59854`
