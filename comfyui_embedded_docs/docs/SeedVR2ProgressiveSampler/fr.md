# SeedVR2ProgressiveSampler

Échantillonneur séquentiel par segments temporels pour les workflows natifs SeedVR2. Ce nœud traite les latences vidéo longues en les divisant en segments temporels plus petits, en échantillonnant chaque segment séquentiellement, et en fusionnant les résultats ensemble. Il sert de remplacement direct pour le KSampler standard lors du travail avec des modèles SeedVR2 sur des séquences qui provoqueraient autrement des erreurs de mémoire insuffisante.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle utilisé pour le débruitage de la latence d'entrée | MODEL | Oui | |
| `seed` | La graine aléatoire utilisée pour créer le bruit (par défaut : 0) | INT | Oui | 0 à 0xffffffffffffffff |
| `steps` | Le nombre d'étapes utilisées dans le processus de débruitage (par défaut : 20) | INT | Oui | 1 à 10000 |
| `cfg` | L'échelle de guidage sans classifieur équilibre la créativité et l'adhésion à la consigne. Des valeurs plus élevées produisent des images correspondant mieux à la consigne, mais des valeurs trop élevées nuiront à la qualité (par défaut : 1.0) | FLOAT | Oui | 0.0 à 100.0 |
| `sampler_name` | L'algorithme utilisé lors de l'échantillonnage, peut affecter la qualité, la vitesse et le style de la sortie générée | COMBO | Oui | Plusieurs options disponibles |
| `scheduler` | Le planificateur contrôle la manière dont le bruit est progressivement supprimé pour former l'image | COMBO | Oui | Plusieurs options disponibles |
| `positive` | Le conditionnement décrivant les attributs que vous souhaitez inclure dans l'image | CONDITIONING | Oui | |
| `negative` | Le conditionnement décrivant les attributs que vous souhaitez exclure de l'image | CONDITIONING | Oui | |
| `latent` | L'image latente à débruiter | LATENT | Oui | |
| `denoise` | La quantité de débruitage appliquée, des valeurs plus faibles maintiendront la structure de l'image initiale permettant un échantillonnage image à image (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `frames_per_chunk` | Images pixels par segment temporel. Doit être une valeur 4n+1 (1, 5, 9, 13, 17, 21, ...) pour respecter les contraintes SeedVR2 (par défaut : 21) | INT | Oui | 1 à 16384 (pas de 4) |
| `temporal_overlap` | Images latentes fusionnées entre les segments adjacents pour masquer la jointure ; 0 signifie aucune fusion (par défaut : 0) | INT | Oui | 0 à 16384 |
| `chunking_mode` | manual = utilise exactement frames_per_chunk ; auto = réduit le segment jusqu'à ce qu'il tienne dans la VRAM (par défaut : "manual") | COMBO | Oui | "manual"<br>"auto" |

**Remarque sur `frames_per_chunk` :** Ce paramètre doit être un nombre d'images pixels de type 4n+1 (1, 5, 9, 13, 17, 21, ...). Le nœud générera une erreur si une valeur invalide est fournie.

**Remarque sur `temporal_overlap` :** La valeur de chevauchement est automatiquement limitée à un maximum d'une unité de moins que la taille du segment latent pour garantir un traitement valide des segments.

**Remarque sur `chunking_mode` :** Lorsqu'il est réglé sur "auto", le nœud essaiera automatiquement des tailles de segment plus petites si le segment actuel provoque une erreur de mémoire insuffisante. Si toutes les tentatives échouent, le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `latent` | La sortie latente débruitée, concaténée à partir de tous les segments temporels en un seul tenseur latent SeedVR2 réduit | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2ProgressiveSampler/fr.md)

---
**Source fingerprint (SHA-256):** `a4574c3e619954b5569551b5b2ba112ecbff918dcebb5ba718a14e77701144a9`
