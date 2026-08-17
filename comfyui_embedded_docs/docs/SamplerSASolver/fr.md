# ÉchantillonneurSASolveur

Le nœud SamplerSASolver implémente un algorithme d'échantillonnage personnalisé pour les modèles de diffusion. Il utilise une approche prédicteur-correcteur avec des paramètres d'ordre configurables et des paramètres d'équation différentielle stochastique (EDS) pour générer des échantillons à partir du modèle d'entrée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle de diffusion à utiliser pour l'échantillonnage | MODEL | Oui | - |
| `eta` | Contrôle le facteur d'échelle de la taille du pas (par défaut : 1.0) | FLOAT | Non | 0.0 - 10.0 |
| `sde_start_percent` | Le pourcentage de départ du processus de débruitage où l'échantillonnage SDE commence, converti en une valeur sigma à l'aide du programme d'échantillonnage du modèle (par défaut : 0.2) | FLOAT | Non | 0.0 - 1.0 |
| `sde_end_percent` | Le pourcentage de fin du processus de débruitage où l'échantillonnage SDE s'arrête, converti en une valeur sigma à l'aide du programme d'échantillonnage du modèle (par défaut : 0.8) | FLOAT | Non | 0.0 - 1.0 |
| `s_noise` | Contrôle la quantité de bruit ajoutée pendant l'échantillonnage (par défaut : 1.0) | FLOAT | Non | 0.0 - 100.0 |
| `predictor_order` | L'ordre du composant prédicteur dans le solveur (par défaut : 3) | INT | Non | 1 - 6 |
| `corrector_order` | L'ordre du composant correcteur dans le solveur (par défaut : 4) | INT | Non | 0 - 6 |
| `use_pece` | Active ou désactive la méthode PECE (Predict-Evaluate-Correct-Evaluate) | BOOLEAN | Non | - |
| `simple_order_2` | Active ou désactive les calculs simplifiés de second ordre | BOOLEAN | Non | - |

Remarque : Toutes les entrées sauf `model` sont des paramètres avancés, masqués par défaut dans l'interface du nœud.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `sampler` | Un objet échantillonneur configuré pouvant être utilisé avec les modèles de diffusion | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/fr.md)

---
**Source fingerprint (SHA-256):** `31da2d436665bf533c28b32248f632edab8f6d92372402904702ae954230f98d`
