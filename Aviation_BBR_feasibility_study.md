# Aviation BBR feasibility study

[Documentation index](README.md) · [Technology assessment](Aviation_BBR_technology_assessment.md) · [Business assessment](Aviation_BBR_business_assessment.md)

## 1. Assessment outcome

A bench investigation is technically plausible given the recorder functions reported for private BBR and the storage capacity arithmetic. Continuous recording, recovery, interface integration and independent decoding still need demonstration. A supplemental airborne recorder adds aircraft-specific installation, power and environmental questions. The approved flight data recorder (FDR) case remains indeterminate until there is an aircraft and approval basis, a defensible crash-recovery boundary, and costed qualification work.

The technology assessment is the basis for all three options. Its 25-hour FPGA/F-RAM/NAND scenario is a common reference for sizing and stress testing. A specific use case could change the retention target, acquisition partition, storage technology or amount of reusable BBR logic. [Technology assessment findings](Aviation_BBR_technology_assessment.md#1-findings-and-scope)

## 2. Options under assessment

| Option | Technology basis | Commercial and operational evidence | Current assessment |
|---|---|---|---|
| Bench demonstrator | Representative data source, continuous capture, explicit time and quality, power interruption and independent export. Compare reuse of BBR where access and rights permit with a peripheral/DMA approach. | Compare against current logging tools using setup time, recovery and time to usable data. Establish whether a research or OEM team would pay for evaluation. | Plausible for gathering evidence. Build scope and reuse effort remain open. |
| Supplemental airborne recorder | A bench-verified path, aircraft-specific interface and power contracts, environmental limits, recording-priority readout, and an installation path for the intended aircraft. | Cost a repeatable configuration, installation and support. Test the USD 3,500 price and USD 1,400 recurring-cost assumptions with buyer and supplier evidence. | Conditional on compatibility, recovery performance, installation permissions and demand. |
| Approved FDR | Aircraft applicability and recording window, parameter and calibration records, protected storage and recovery, assurance, environmental and crash-survival evidence, and independent extraction. | Identify an aircraft or operator partner and price the equipment and installation routes, qualification, retest and support. | Indeterminate. The existing capacity estimate and optional feasibility allowance cover only portions of this case. |

The commercial inputs apply to the same capability boundaries as the technology assessment. The Australian experimental-aircraft sales cases inform the supplemental option. Demand for bench systems, OEM integrations and approved FDRs would need separate evidence. [Business assessment market model](Aviation_BBR_business_assessment.md#31-tmv-analysis-total-market-value)

## 3. Evidence that would change the outcome

| Question | Evidence needed | Effect on feasibility |
|---|---|---|
| Which acquisition partition suits the use case? | One representative parameter dictionary and source workload, including bursts, sample timing, source age and invalid inputs. Measure the encoded rate and compare FPGA and peripheral/DMA options against the same inputs. | Determines what can be reused and whether the 10M50 reference envelope is justified. |
| Can the archive keep up and retain the required history? | Demonstrate usable bytes after reservations and measure cumulative media service under repeated stalls, ECC, retries and readout. Test cyclic overwrite and record maximum queue occupancy. | Determines storage/controller choice, staging capacity and the defensible retention claim. |
| How much of the end of a recording can be recovered? | Measure loss from the acquisition input through independent decode during power cuts. For crash-protected operation, account for data staged outside the enclosure and verify recovery after the applicable crash exposure. | Determines the required commit interval, power hold-up and crash enclosure boundary. |
| Can the recorder be used in a representative aircraft? | Identify the aircraft, operating category, interfaces, isolation and power behavior. For the approved case, trace applicable rules, standards and installation evidence, including preservation across archive wrap where required. | Determines whether the scope supports a bench evaluation, a supplemental installation or an approved article and installation. |
| Does a repeatable commercial configuration exist? | Quote a representative BOM and support scope, measure integration effort, and document willingness to pay. Use dated revenues and expenses in one currency to compare cash needs across options. | Determines whether the modeled contribution and development envelope justify further work. |

The technology assessment retains the detailed test criteria, numeric assumptions and source limitations. [Reference storage scenario](Aviation_BBR_technology_assessment.md#63-fpga-and-nonvolatile-storage-reference-scenario) · [Assurance and verification evidence](Aviation_BBR_technology_assessment.md#9-assurance-and-verification-evidence)

## 4. Cost and decision boundaries

The business assessment estimates **AUD 37,500–62,500** for discovery and requirements and **AUD 131,250–200,000** for the architecture and bench-demonstrator work package, both including contingency. These are work-package scenarios. The **AUD 600,000–1,018,750** range covers the modeled non-certified path through controlled release. The optional **AUD 62,500–125,000** approved-FDR feasibility range covers preliminary specialist and planning work. Full approval and qualification costs remain unknown. [Development cost model](Aviation_BBR_business_assessment.md#81-aud-development-cost-estimate-by-stage)

The lowest-scope decision is whether a representative data set, a benchmark against existing logging, and a small recording and recovery demonstration would answer a specific customer question. Evidence of repeatable technical performance, installation feasibility and paid demand would support assessing an airborne product. An approved FDR requires aircraft-specific evidence and a separate commercial case.
