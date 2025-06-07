
Le nœud KSampler est conçu pour des opérations d'échantillonnage avancées au sein des modèles génératifs, permettant la personnalisation des processus d'échantillonnage à travers divers paramètres. Il facilite la génération de nouveaux échantillons de données en manipulant les représentations de l'espace latent, en utilisant le conditionnement et en ajustant les niveaux de bruit.

## Entrées

| Paramètre       | Data Type | Description                                                                                                               |
|-----------------|-------------|---------------------------------------------------------------------------------------------------------------------------|
| `model`         | `MODEL`     | Spécifie le modèle génératif à utiliser pour l'échantillonnage, jouant un rôle crucial dans la détermination des caractéristiques des échantillons générés. |
| `seed`          | `INT`       | Contrôle l'aléatoire du processus d'échantillonnage, assurant la reproductibilité des résultats lorsqu'il est défini à une valeur spécifique.                         |
| `steps`         | `INT`       | Détermine le nombre d'étapes à suivre dans le processus d'échantillonnage, affectant le détail et la qualité des échantillons générés.           |
| `cfg`           | `FLOAT`     | Ajuste le facteur de conditionnement, influençant la direction et la force du conditionnement appliqué lors de l'échantillonnage.                     |
| `sampler_name`  | COMBO[STRING] | Sélectionne l'algorithme d'échantillonnage spécifique à utiliser, impactant le comportement et le résultat du processus d'échantillonnage.                     |
| `scheduler`     | COMBO[STRING] | Choisit l'algorithme de planification pour contrôler le processus d'échantillonnage, affectant la progression et la dynamique de l'échantillonnage.           |
| `positive`      | `CONDITIONING` | Définit le conditionnement positif pour guider l'échantillonnage vers les attributs ou caractéristiques souhaités.                                         |
| `negative`      | `CONDITIONING` | Spécifie le conditionnement négatif pour orienter l'échantillonnage loin de certains attributs ou caractéristiques.                                     |
| `latent_image`  | `LATENT`    | Fournit une représentation de l'espace latent à utiliser comme point de départ ou de référence pour le processus d'échantillonnage.                            |
| `denoise`       | `FLOAT`     | Contrôle le niveau de débruitage appliqué aux échantillons, affectant la clarté et la netteté des images générées.                   |

## Sorties

| Paramètre   | Data Type | Description |
|-------------|-------------|-------------|
| `latent`    | `LATENT`    | Représente la sortie de l'espace latent du processus d'échantillonnage, encapsulant les échantillons générés. |
