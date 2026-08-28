# SamplerDPMPP_SDE

```markdown
SamplerDPMPP_SDE crée un échantillonneur DPM++ SDE (équation différentielle stochastique) destiné au processus d'échantillonnage. Cet échantillonneur fournit une méthode d'échantillonnage stochastique avec des paramètres de bruit configurables et une sélection du périphérique. Il renvoie un objet échantillonneur pouvant être utilisé dans le pipeline d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `eta` | Contrôle le caractère stochastique du processus d'échantillonnage (défaut : 1.0) | FLOAT | Oui | 0.0 - 100.0 |
| `s_bruit` | Contrôle la quantité de bruit ajoutée pendant l'échantillonnage (défaut : 1.0) | FLOAT | Oui | 0.0 - 100.0 |
| `r` | Paramètre qui influence le comportement de l'échantillonnage (défaut : 0.5) | FLOAT | Oui | 0.0 - 100.0 |
| `appareil_bruit` | Sélectionne le périphérique sur lequel les calculs de bruit sont effectués. Lorsqu'il est défini sur "cpu", l'échantillonneur `dpmpp_sde` est créé ; lorsqu'il est défini sur "gpu", l'échantillonneur `dpmpp_sde_gpu` est créé (défaut : "gpu") | COMBO | Oui | "gpu"<br>"cpu" |

Remarque : Tous les paramètres d'entrée sont marqués comme paramètres avancés. La sélection de `noise_device` change la variante d'échantillonneur créée : "cpu" correspond à `dpmpp_sde` et "gpu" correspond à `dpmpp_sde_gpu`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Renvoie un objet échantillonneur DPM++ SDE configuré pour une utilisation dans les pipelines d'échantillonnage | SAMPLER |
```

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/fr.md)

---
**Source fingerprint (SHA-256):** `56949712f245abfcc48c09d7d14a1a7778e80ba58535e538484c382d7e0d02c6`
