Le nœud `SamplerDPMPP_2S_Ancestral` crée un échantillonneur utilisant la méthode d'échantillonnage DPM++ 2S Ancestral pour générer des images. Cet échantillonneur combine des éléments déterministes et stochastiques afin de produire des résultats variés tout en maintenant une certaine cohérence. Il permet de contrôler le niveau d'aléatoire et de bruit pendant le processus d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `eta` | Contrôle la quantité de bruit stochastique ajoutée lors de l'échantillonnage (valeur par défaut : 1.0) | FLOAT | Oui | 0.0 - 100.0 |
| `s_bruit` | Contrôle l'échelle du bruit appliqué pendant le processus d'échantillonnage (valeur par défaut : 1.0) | FLOAT | Oui | 0.0 - 100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Renvoie un objet échantillonneur configuré pouvant être utilisé dans le pipeline d'échantillonnage | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2S_Ancestral/fr.md)

---
**Source fingerprint (SHA-256):** `9634c96934850f5b746cd7c8b29727396af534133b8d54b6bdac12e9e0975189`
