# SUSHI-konfigurasjon

## Konfigurasjonsparametre - UNDER UTVIKLING

### `version`

Versjonen til Implementation Guide-en. Følger [semantisk versjonering](https://semver.org/):

```yaml
version: 2.2.3-test    # Utviklingsversjon
version: 2.2.3         # Stabil release
version: 2.3.0-beta    # Beta-versjon
```

**Format:** `MAJOR.MINOR.PATCH[-suffix]`
- **MAJOR**: Bryte bakoverkompatibilitet
- **MINOR**: Ny funksjonalitet (bakoverkompatibel)
- **PATCH**: Feilrettinger
- **suffix**: `-test`, `-beta`, `-rc1`, etc.

---

### `releaseLabel`

Indikerer publiseringsstatus. Påvirker banner og metadata i publisert IG.

#### Utviklingsstadier
| Label | Beskrivelse | Bruk |
|-------|-------------|------|
| `ci-build` | Kontinuerlig bygg fra main-branch | Daglig utvikling, ustabil |
| `snapshot` | Utviklingssnapshot | Mellomlagring |
| `draft` | Tidlig utkast | Første versjon, ikke klar for review |

#### Testfaser
| Label | Beskrivelse | Bruk |
|-------|-------------|------|
| `qa-preview` | Kvalitetssikringsversjon | Intern testing før publisering |
| `ballot` | Offisiell HL7 ballot-versjon | Offentlig høring/avstemning |

#### Produksjonsstadier
| Label | Beskrivelse | Bruk |
|-------|-------------|------|
| `trial-use` | Standard for Trial Use (STU) | Første produksjonsrelease, kan endre seg |
| `release` | Offisiell stabil release | Anbefalt for produksjon |
| `update` | Mindre oppdatering | Patch til eksisterende release |
| `normative` | Normativ standard | Stabil, garantert bakoverkompatibel |

#### Spesielle
| Label | Beskrivelse | Bruk |
|-------|-------------|------|
| `informative` | Kun informativt innhold | Veiledning uten normative krav |
| `deprecated` | Utgått versjon | Frarådes, bruk nyere versjon |

---

### `status`

ImplementationGuide-ressursens formelle status.

| Status | Beskrivelse |
|--------|-------------|
| `draft` | Under utvikling |
| `active` | Aktiv og i bruk (standard) |
| `retired` | Ikke lenger i bruk |
| `unknown` | Ukjent status |

**Merk:** `status` beskriver ressursen generelt, mens `releaseLabel` beskriver denne spesifikke versjonen.

---

## Typiske Konfigurasjoner

### Under Utvikling
```yaml
version: 2.2.3-test
releaseLabel: ci-build
status: active
```

### Klar for Testing
```yaml
version: 2.3.0-beta
releaseLabel: qa-preview
status: active
```

### Produksjonsrelease
```yaml
version: 2.3.0
releaseLabel: trial-use
status: active
```

### Stabil/Moden Release
```yaml
version: 3.0.0
releaseLabel: release
status: active
```

---

## Anbefalinger for NoBasis

1. **Utvikling:** Bruk `ci-build` med `-test` suffix
2. **Intern testing:** Endre til `qa-preview` og fjern `-test`
3. **Første prod:** Bruk `trial-use` for å signalisere at endringer kan komme
4. **Stabil versjon:** Oppgrader til `release` når profiler er modne
5. **Versjonering:** Bump MAJOR ved breaking changes, MINOR ved nye profiler

---

## Publisering

Når du er klar til å publisere en ny versjon:

1. **Oppdater sushi-config.yaml:**
   ```yaml
   version: 2.2.3
   releaseLabel: trial-use
   ```

2. **Commit og push:**
   ```bash
   git add no-basis/sushi-config.yaml
   git commit -m "Release version 2.2.3"
   git push
   ```

3. **Trigger manuell release:**
   - Gå til GitHub Actions → "Publish FHIR IG Release"
   - Klikk "Run workflow"
   - Versjonen publiseres til `https://hl7norway.github.io/basisprofiler-r4-fsh/2.2.3/`

---

## Referanser

- [SUSHI Dokumentasjon](https://fshschool.org/docs/sushi/configuration/)
- [HL7 IG Publisher](https://confluence.hl7.org/display/FHIR/IG+Publisher+Documentation)
- [Semantisk Versjonering](https://semver.org/)
