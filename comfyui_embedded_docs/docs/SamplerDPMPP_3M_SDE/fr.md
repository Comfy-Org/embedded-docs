> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/fr.md)

Le nœud SamplerDPMPP_3M_SDE crée un échantillonneur DPM++ 3M SDE destiné au processus d'échantillonnage. Cet échantillonneur utilise une méthode d'équation différentielle stochastique multi-étapes du troisième ordre avec des paramètres de bruit configurables. Le nœud vous permet de choisir si les calculs de bruit sont effectués sur le GPU ou le CPU.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `eta` | FLOAT | Oui | 0.0 - 100.0 | Contrôle la stochasticité du processus d'échantillonnage (par défaut : 1.0) |
| `s_bruit` | FLOAT | Oui | 0.0 - 100.0 | Contrôle la quantité de bruit ajoutée lors de l'échantillonnage (par défaut : 1.0) |
| `appareil_bruit` | COMBO | Oui | "gpu"<br>"cpu" | Sélectionne le périphérique pour les calculs de bruit, soit GPU soit CPU (par défaut : "gpu") |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `sampler` | SAMPLER | Renvoie un objet échantillonneur configuré pour une utilisation dans les workflows d'échantillonnage |

---
**Source fingerprint (SHA-256):** `817ce8c12245063e5f2f3421f57dd55801aae96dfd8fe1bf3f88f814799b830a`
