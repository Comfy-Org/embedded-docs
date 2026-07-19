# ExtendIntermediateSigmas

Le nœud ExtendIntermediateSigmas prend une séquence existante de valeurs sigma et insère des valeurs sigma intermédiaires supplémentaires entre elles. Il vous permet de spécifier le nombre d'étapes supplémentaires à ajouter, la méthode d'espacement pour l'interpolation, ainsi que des limites sigma de début et de fin optionnelles pour contrôler où l'extension se produit dans la séquence sigma.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `sigmas` | La séquence sigma d'entrée à étendre avec des valeurs intermédiaires | SIGMAS | Oui | - |
| `étapes` | Nombre d'étapes intermédiaires à insérer entre les sigmas existants (par défaut : 2) | INT | Oui | 1 à 100 |
| `commencer_à_sigma` | Limite sigma supérieure pour l'extension - n'étend que les sigmas inférieurs à cette valeur (par défaut : -1,0, ce qui signifie l'infini) | FLOAT | Oui | -1,0 à 20000,0 |
| `finir_à_sigma` | Limite sigma inférieure pour l'extension - n'étend que les sigmas supérieurs à cette valeur (par défaut : 12,0) | FLOAT | Oui | 0,0 à 20000,0 |
| `espacement` | La méthode d'interpolation pour espacer les valeurs sigma intermédiaires (par défaut : "linear") | COMBO | Oui | `"linear"`<br>`"cosine"`<br>`"sine"` |

**Remarque :** Le nœud insère uniquement des sigmas intermédiaires entre les paires de sigmas existantes où le sigma actuel est à la fois inférieur ou égal à `start_at_sigma` et supérieur ou égal à `end_at_sigma`. Lorsque `start_at_sigma` est défini sur -1,0, il est traité comme l'infini, ce qui signifie que seule la limite inférieure `end_at_sigma` s'applique.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sigmas` | La séquence sigma étendue avec des valeurs intermédiaires supplémentaires insérées | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/fr.md)

---
**Source fingerprint (SHA-256):** `f51ed433fc38365334ff8e4072174dc04982a8a00770d07f544320a6863577c4`
