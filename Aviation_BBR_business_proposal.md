# Aviation BBR business proposal

[Documentation index](README.md) | [Technical design](Aviation_BBR_design.md)

**Date:** 8 November 2026  
**Status:** Draft commercial proposal for customer discovery and development planning  
**Currency:** Selling prices and commercial scenarios are in US dollars (USD). Section 8.1 development estimates are in Australian dollars (AUD). Amounts exclude applicable taxes; development-budget inclusions and exclusions are stated below.

## 1. Proposal

Develop Aviation BBR into a configurable flight instrument data recorder for aircraft development, research and experimental applications. Start with a non-certified engineering product targeting a **$3,500 direct selling price per unit**, supported by separately priced integration services. Pursue a crash-protected, approved flight data recorder only after customer demand, technical feasibility and a funded approval route have been established.

The immediate commercial objective is to secure three development partners, agree their recording requirements and obtain paid pilot commitments before committing to production hardware.

This is a proposal for a product under development. The public repository currently contains a design study and architecture diagrams; it does not contain an implemented or validated aviation recorder. The private baseline BBR is a potential source of reusable engineering, not evidence that the aviation product is complete. No customers, orders, supplier quotations or investment commitments are established by this document.

![Proposed Aviation BBR architecture](images/aviation-bbr-top-level.png)

## 2. Customer problem and proposed value

Aircraft developers and research teams need to capture numerical instrument, sensor and aircraft-system data, reconstruct test events and identify missing or corrupted measurements. Configuring interfaces, recovering data after power interruptions and converting raw recordings into usable engineering data can consume significant integration effort.

Aviation BBR would offer a documented recording path with continuous capture, source identity, timestamps, explicit data-quality information and independent readout. The intended value is dependable, interpretable data and a manageable integration effort. Customer interviews must establish whether these benefits justify a dedicated recorder instead of existing avionics logging or a general-purpose data acquisition system.

Proposed capabilities follow the [technical design](Aviation_BBR_design.md):

- Continuous instrument recording with a provisional 25-hour retention target.
- FPGA acquisition and buffering with defined timing and source-validity behavior.
- Mirrored F-RAM staging and a NAND archive, subject to component and controller validation.
- Recoverable recording chunks and measured power-loss behavior.
- A documented data format, download utility and engineering-data export.

These are development targets. Interface count, sampling performance, usable storage, recoverable tail loss and environmental limits must be specified and verified before being included as guaranteed sales specifications. Voice, image and video recording are outside the current design scope. Crash protection is a separate future development activity.

## 3. Initial customers and positioning

| Customer segment | Proposed use | Commercial approach |
|---|---|---|
| Aircraft and avionics development teams | Bench integration and instrument-data capture during development | Paid evaluation followed by a defined pilot |
| Universities and aerospace research groups | Repeatable data collection and engineering analysis | Evaluation kit with documented interfaces and export tools |
| Experimental aircraft developers | Supplemental instrument logging where the installation and use are permitted | Limited pilot with agreed installation responsibilities |
| Equipment manufacturers | Recorder integration into their own development platforms | Hardware supply plus separately scoped engineering services |

Begin with bench and research use. Any airborne pilot must establish the applicable installation and operating permissions before flight. The initial product is not offered as a replacement for a required approved FDR.

The proposed differentiation is configurable acquisition, explicit quality and recovery behavior, and accessible engineering readout. FPGA implementation is an enabling technology; it is not, by itself, a reason for customers to pay a premium.

Section 3.1 provides an initial market-sizing model using a published Australian fleet baseline and explicit assumptions. It is not a validated demand forecast or a global market valuation. Interview evidence and qualified opportunities should precede a sales forecast.

### 3.1. TMV analysis: total market value

**Definition and scope:** In this proposal, TMV means **Total Market Value**: the theoretical hardware sales value of a defined aircraft population at the proposed unit price. The starting scope is Australian registered amateur-built, single-engine piston aeroplanes. This is a deliberately narrow beachhead aligned with the proposed experimental-aircraft offering. Research benches and OEM development platforms remain target customers but are excluded from the numerical model because no verified customer count is available. TMV is neither company valuation nor annual recorder-industry revenue.

**Published baseline:** CASA's *Annual Report 2024-25*, table A.15, printed page 169, records **1,558 amateur-built, single-engine piston aeroplanes** at 30 June 2025. Table A.14 records **16,545 aircraft** on the register overall. The broader total includes many aircraft outside the initial product scope and is not used as the addressable market. These are historical registered-fleet counts, not current active-aircraft counts or evidence of recorder demand. [CASA Annual Report 2024-25](https://www.casa.gov.au/sites/default/files/2025-11/casa-annual-report-2024-2025.pdf#page=172).

The following calculations assume one recorder per aircraft at **USD 3,500**, no discounts and no installation revenue. They describe a one-time installed-base opportunity, not annual recurring revenue. Bench kits, support, integration services, future fleet growth and replacement purchases are excluded to avoid unsupported additions or double counting. Aircraft eligibility and installation permissions still require individual assessment.

| Market layer | Calculation | Units | Hardware value (USD) | Interpretation |
|---|---|---:|---:|---|
| TMV / theoretical total addressable market (TAM) for this beachhead | 1,558 aircraft x 1 recorder x $3,500 | 1,558 | **$5,453,000** | Upper bound assuming every aircraft buys; not achievable revenue guidance |
| Serviceable available market (SAM), low assumption | Floor of 1,558 x 10% | 155 | **$542,500** | Assumed subset with suitable interfaces, a feasible installation and an unmet recording need |
| SAM, base assumption | Floor of 1,558 x 20% | 311 | **$1,088,500** | Working discovery hypothesis; neither eligibility nor willingness to pay is verified |
| SAM, high assumption | Floor of 1,558 x 30% | 467 | **$1,634,500** | Requires broader compatibility and demonstrated customer need |

The 10-30% serviceability range is a management assumption, not a CASA statistic. Validate it by screening aircraft configuration, existing logging capability, installation effort, interface compatibility and an identified buyer. Do not classify an aircraft as serviceable solely because it is amateur-built.

#### Obtainable sales over 36 months after commercial release

The serviceable obtainable market (SOM) below is a set of sales hypotheses constrained by direct customer acquisition and delivery capacity. It is not an existing pipeline. Account counts and units per account are assumptions; an account may be a developer or integrator buying for several aircraft. Bench-only sales are outside this model, and each aircraft installation must be counted once even if an integrator and owner both appear in the contact list.

| Scenario | Purchasing accounts | Average units per account | Units over 36 months | Hardware revenue (USD) | Share of base SAM (311 units) |
|---|---:|---:|---:|---:|---:|
| Low | 10 | 2.5 | 25 | $87,500 | 8.0% |
| Base | 20 | 2.5 | 50 | $175,000 | 16.1% |
| Stretch | 40 | 2.5 | 100 | $350,000 | 32.2% |

Even the base case requires a meaningful share of a small market. The stretch case needs strong distribution, proven customer references and sufficient manufacturing/support capacity; it must not be used as the funding baseline before orders substantiate it. The three pilot partners in section 1 are development objectives, not these purchasing accounts. Count any qualifying pilot deliveries within the 36-month totals only if delivered during that period, not as extra sales.

**Stock versus annual demand:** If, purely as a sensitivity test, 5-10% of the 311-aircraft base SAM purchases each year, the result is approximately **15-31 units per year**, rounded down, or **USD 52,500-108,500 annual hardware revenue** at the target price. This assumed purchase rate includes no repeat purchase or fleet growth and cannot be applied indefinitely to an unchanged installed base. At the section 6 contribution assumption of USD 2,100 per unit, that volume yields only **USD 31,500-65,100 per year before fixed costs**. There is no evidence yet that this purchase rate can be achieved.

**Commercial implication:** The narrow Australian amateur-built segment alone does not currently justify the AUD 600,000-1,018,750 development envelope. A stronger case needs paid OEM/research integrations, a separately measured export opportunity, lower development expenditure, or a combination supported by customer evidence. USD revenues above must not be compared directly with AUD development expenditure without a dated exchange-rate assumption. Section 7's 25/100/250-unit scenarios remain general scale illustrations, not annual Australian-market forecasts; they are not additive to this SOM.

#### Validation and expansion gates

1. Build a deduplicated Australian prospect list and screen at least 30 candidate aircraft or projects for technical fit, present logging capability, installation path and buyer budget. Treat this as a targeted discovery sample, not a representative statistical survey.
2. Complete the section 8 customer interviews and secure three paid pilot commitments with a defined standard configuration. Record actual quotes, objections, acquisition effort and support requirements.
3. Replace the assumed serviceability percentages and account conversion with documented prospect evidence before publishing an investor forecast. Reconcile annual sales with lead time, procurement timing and production capacity.
4. Size research/OEM benches and each export geography separately using primary fleet/customer data and local installation requirements. Remove overlaps before combining markets. No global TMV or growth rate is claimed by this draft.
5. Evaluate the approved-FDR market only after feasibility defines the product, approval route and eligible fleet. Do not apply the future USD 25,000-45,000 price to the initial non-certified beachhead to enlarge the opportunity.

## 4. Market price references

Public references provide context for pricing, but are not equivalent product comparisons:

| Reference | Published price context | Limitation |
|---|---|---|
| FAA Investigative Technologies Aviation Rulemaking Committee, final report dated 29 August 2025, section VI.B, printed page 21 | Approximately $3,000 for a light recording unit to $60,000 for an ED-112-compliant FDR | Broad hardware range; aircraft modification and installation are excluded. [Report](https://www.faa.gov/media/105721) |
| Air Power, part 2100-2045-23, checked 8 November 2026 | Listed price $38,244; refundable core charge $10,000; total before core return $48,244 | Listing states new condition and backorder. Price and terms require confirmation; this is not an Aviation BBR quotation. [Listing](https://www.airpowerinc.com/2100-2045-23) |

The $3,500 initial target is a pricing hypothesis to test with prospective customers. It is not derived from verified BBR manufacturing costs or demonstrated willingness to pay.

## 5. Product and revenue model

| Offering | Proposed price | Proposed scope and conditions |
|---|---|---|
| Engineering evaluation kit | $1,500-3,000 per kit | Bench hardware, example data, basic download tools and limited evaluation support; configuration may be reduced from the enclosed product |
| Standard development recorder | **$3,500 target per unit**; planning range $3,000-6,000 | Enclosed and tested non-certified recorder, documented standard interfaces, readout utility and defined support |
| Customer integration | Separate statement of work | Source interfaces, parameter mapping, adapters, test procedures and acceptance evidence |
| Extended support | Separately quoted annual agreement | Defined response times, maintenance releases and compatibility assistance |
| Future approved FDR | $25,000-45,000 per unit as an exploratory target | Subject to approval route, crash-survival evidence, production costs, market validation and partner support; not currently available |

Standard hardware pricing excludes sensors, aircraft wiring, installation, custom interfaces, qualification, approval work and bespoke analysis. The standard interface set and included support allowance must be fixed before accepting production orders.

Use direct sales for initial pilots. Distributor pricing needs a separate model because channel discounts reduce realized revenue. Do not promise volume discounts until manufacturing yield, support load and procurement costs are measured.

## 6. Illustrative unit economics

The following is a **cost allowance**, not a supplier-backed BOM. It assumes direct sales of the standard non-certified recorder at $3,500. The $1,400 total is a cost ceiling to test during design and procurement.

| Recurring cost category | Target allowance per unit |
|---|---:|
| Electronics, PCB, FPGA, memory and standard interface components | $650 |
| Enclosure, connectors and mounting hardware | $150 |
| Assembly and production testing | $200 |
| Yield loss, procurement and inbound freight allowance | $150 |
| Warranty and repair reserve | $100 |
| Included customer support allowance | $150 |
| **Total recurring cost allowance** | **$1,400** |

At this allowance, gross contribution is **$2,100 per unit**, or **60% of revenue**. This simplified commercial model is not an accounting policy. It excludes fixed development, tools, salaries outside allocated production/support, sales, administration, insurance, finance costs and future approval expenditure.

| Direct selling price | Recurring unit cost | Contribution per unit | Contribution margin |
|---|---:|---:|---:|
| $3,000 | $1,400 | $1,600 | 53.3% |
| $3,500 | $1,400 | $2,100 | 60.0% |
| $3,500 | $2,000 | $1,500 | 42.9% |
| $4,500 | $2,000 | $2,500 | 55.6% |

If the required aircraft interfaces or storage implementation make the cost ceiling unrealistic, reduce the standard configuration, increase price or stop the product before production commitments.

## 7. Sales scenarios and development funding

These scenarios illustrate scale at $3,500 revenue and $1,400 recurring cost per unit. They are not an annual forecast, sales pipeline or evidence of demand. Integration and support-contract revenue are excluded because delivery effort and margins are not yet estimated.

| Units sold in a planning period | Hardware revenue | Recurring costs | Contribution before fixed costs |
|---|---:|---:|---:|
| 25 | $87,500 | $35,000 | $52,500 |
| 100 | $350,000 | $140,000 | $210,000 |
| 250 | $875,000 | $350,000 | $525,000 |

For illustration, recovering **$300,000 of fixed development expenditure alone** would require **143 units** at $2,100 contribution each. This does not establish company break-even: operating overhead, selling costs, cash timing and further development must also be covered. The $300,000 figure is an example, not an engineering budget or funding request.

Section 8.1 provides an initial AUD development estimate by stage. Before seeking investment or committing delivery dates, replace its allowances with a bottom-up budget for engineering effort, prototype hardware, test equipment, third-party testing, tooling, software, insurance and working capital. Estimate cash required to buy and build pilot units before customer payments arrive. Price and fund crash protection and aviation approval separately.

Prefer paid discovery and milestone-based development contracts for customer-specific work. Any deposits should be tied to written deliverables, acceptance criteria, delivery assumptions and cancellation terms. Customer commitments must not be represented as guaranteed production revenue before their conditions are satisfied.

## 8. Development stages and release gates

Timing below is an initial planning assumption measured from a funded project start with an available engineering team. Team capacity, procurement and requirements review must establish the actual schedule.

| Stage | Indicative timing | Required evidence before proceeding |
|---|---|---|
| Customer discovery and requirements | Months 0-2 | At least 10 customer interviews; three qualified development partners; agreed interfaces and acceptance criteria; willingness-to-pay evidence |
| Architecture and bench demonstrator | Months 2-5 | Versioned format, acquisition model, readout prototype and initial BOM; simulation of rollover, faults and power-loss recovery |
| Integrated prototype | Months 5-9 | Prototype hardware, full-retention and cyclic-overwrite tests, measured storage behavior, timing evidence and independent decoding |
| Paid pilot and production preparation | Months 9-12 | Pilot commitments and acceptance results; verified build/test process, costed supply chain and defined support terms |
| Controlled commercial release | After pilot acceptance | Released configuration, production acceptance tests, published limitations and a funded support process |
| Approved FDR feasibility | Separate project decision | Identified aircraft/customer, approval basis, qualified partners, costed crash-survival and assurance plan, funding and commercial justification |

The initial 12-month sequence is not a delivery commitment. Do not launch against a date if recovery, retention, interface compatibility or production evidence remains incomplete.

### 8.1. AUD development cost estimate by stage

**Estimate basis, 8 November 2026:** These are preliminary engineering estimates, not supplier quotations or a fixed-price offer. Budget **AUD 600,000-1,018,750** through controlled release of the non-certified development recorder, including a 25% contingency. A practical midpoint planning allowance is approximately **AUD 810,000**. Approved-FDR feasibility adds **AUD 62,500-125,000** and does not fund development or approval of that future product.

The model assumes a blended **AUD 150 per productive person-hour**, covering engineering, verification, readout software, documentation and project coordination. This is an assumed fully burdened project rate, not a quoted contractor rate or employee wage. It includes employment/contracting burden and routine business overhead allocated to those hours; do not add the same labour costs again. Australian recruitment guides can inform subsequent role-specific costing, but do not validate this project's blended rate or effort: [Hays engineering salary guide](https://www.hays.com.au/salary-guide/engineering).

All amounts in the following table are **AUD thousands (k)**. Stage costs are incremental; sum them rather than treating each row as a cumulative budget. Low and high values reflect different effort and procurement outcomes, not statistical confidence limits.

| Development stage | Productive person-hours | Labour at AUD 150/hour (k) | Other direct costs (k) | Base cost (k) | Budget including 25% contingency (k) |
|---|---:|---:|---:|---:|---:|
| Customer discovery and requirements | 160-240 | 24-36 | 6-14 | 30-50 | **37.50-62.50** |
| Architecture and bench demonstrator | 600-900 | 90-135 | 15-25 | 105-160 | **131.25-200.00** |
| Integrated prototype | 1,000-1,600 | 150-240 | 35-70 | 185-310 | **231.25-387.50** |
| Paid pilot and production preparation | 600-1,000 | 90-150 | 30-60 | 120-210 | **150.00-262.50** |
| Controlled commercial release | 200-400 | 30-60 | 10-25 | 40-85 | **50.00-106.25** |
| **Non-certified product subtotal** | **2,560-4,140** | **384-621** | **96-194** | **480-815** | **600.00-1,018.75** |
| Approved FDR feasibility, optional additional stage | 240-480 | 36-72 | 14-28 | 50-100 | **62.50-125.00** |
| **Total including optional feasibility** | **2,800-4,620** | **420-693** | **110-222** | **530-915** | **662.50-1,143.75** |

Other direct cost allowances cover the following stage-specific work:

- **Discovery:** interview travel, requirements workshops and initial commercial/installation advice.
- **Bench demonstrator:** development boards, memory evaluation hardware, tool licences, purchased standards and bench fixtures.
- **Integrated prototype:** two PCB build/revision cycles, prototype enclosures, components, laboratory access and preliminary EMC/environmental checks. These checks are not formal aviation qualification.
- **Pilot preparation:** an assumed 5-10 pilot units, production-test fixtures, limited field support/travel and documentation delivery. This allowance funds pilot hardware once; pilot units must not also be charged as production inventory in the development budget. Any pilot revenue is modelled separately and has not been deducted.
- **Commercial release:** manufacturing handover, initial test-station/tooling costs, packaging setup and release-specific insurance/legal allowances. Ongoing premiums, overhead and support beyond the release effort need an operating budget.
- **Approved FDR feasibility:** specialist assurance advice, approval-basis planning, crash-survivable memory options and preliminary laboratory/manufacturing quotations. The labour column covers internal coordination; specialist external advice is in other direct costs.

The effort assumes one standard acquisition configuration, reuse of baseline BBR only after technical and rights review, access to existing general laboratory equipment, and a small engineering team with overlapping hardware, FPGA, software and verification work. At 1,400 productive hours per person-year, the non-certified estimate represents approximately **1.8-3.0 person-years**. The indicative schedule therefore requires appropriate team capacity and parallel work; it is not a solo developer's 12-month promise. Extensive new aircraft-bus adapters or a largely new NAND/ECC controller could exceed this range.

Contingency is calculated as 25% of each stage's labour plus other direct costs. Release funding by stage against the section 8 acceptance gates. These totals include no GST, financing costs, large production inventory, full aircraft installation/modification programme, flight-test aircraft hire, or formal crash-survival and aviation qualification campaign. Prototype-component and equipment procurement allowances include estimated inbound freight. Overseas purchases need exchange-rate allowances when supplier quotes are obtained.

**Future approved-FDR development and qualification remain uncosted.** Feasibility must establish the target assurance level, equipment and installation approval routes, crash-protected memory approach, independent verification, accredited testing and retest exposure before a credible programme budget can be presented. The optional feasibility allowance is not an estimate of certification cost and does not imply that approval can be completed within the non-certified product budget.

The earlier **USD 300,000** recovery example in section 7 remains a separate arithmetic illustration; it is not this AUD budget. No AUD/USD exchange rate has been applied. Before presenting a combined investment-return model, choose and date an exchange-rate assumption and convert costs and revenues into one currency.

## 9. Sales and pilot plan

Prepare a short product brief, the architecture diagram, an interface questionnaire and a demonstration using representative instrument data. Approach engineering decision makers directly and record their present logging method, integration costs, required interfaces, data-loss tolerance and purchasing process.

Select three pilot partners with similar core requirements to avoid creating three unrelated products. Agree a fixed standard configuration and quote custom adapters separately. Each pilot should demonstrate sustained recording, readable export, timestamp/quality behavior and measured recovery after interruptions against written acceptance criteria.

Measure conversion from interview to paid pilot, engineering hours per integration, recurring unit cost, production yield, support hours and pilot acceptance. Release the standard product only when customers accept its measured capabilities at a price that supports the cost model.

## 10. Intellectual property and delivery model

The public [Aviation-BBR repository](https://github.com/Ala-Ismail/Aviation-BBR) contains MIT-licensed material. The private [BBR baseline](https://github.com/Ala-Ismail/BBR) requires authorized access. Publication of this proposal does not grant access to or change the license of the private repository.

Revenue should come from delivered hardware, tested configurations, integration and support. Do not base the business case on exclusive access to material already published under MIT. Before shipping a product, establish the rights to every reused design, HDL block, software component and vendor IP, and define which deliverables will be public, private or supplied under customer contracts.

This proposal introduces no dependency on publishing private BBR source or copying its private documents into the public repository.

## 11. Main business risks

| Risk | Effect | Proposed response |
|---|---|---|
| Existing avionics logging meets customer needs | Weak willingness to pay | Validate specific unmet requirements before hardware investment |
| Too many bespoke interfaces | Integration consumes hardware margin | Publish a standard configuration; charge separately for custom engineering |
| NAND, ECC or recovery complexity | Higher cost and delayed release | Prototype the storage path early and verify interruption behavior |
| Component availability or low production yield | Cost ceiling is missed | Obtain supplier quotes and pilot-build yield data before fixing production prices |
| Buyers expect approved crash-protected recording | Product is unsuitable for the intended purchase | State product status and operating limits in quotations and specifications |
| Support and liability costs exceed allowances | Lower margin and higher cash needs | Define support scope, review insurance needs and measure pilot support effort |
| Approval programme begins before demand is proven | Capital required exceeds available funding | Make approval a separately funded, customer-backed decision |

## 12. Proposed next decision

Proceed with customer discovery and a costed bench-demonstrator plan. Retain **$3,500 per unit** as the initial standard-recorder price hypothesis and **$1,400 per unit** as the recurring-cost ceiling. Revisit both after interviews, supplier quotations and prototype testing.

The next commercial deliverables are three qualified pilot opportunities, a standard interface specification, a quoted BOM, a validated engineering work estimate and a staged cash budget refining section 8.1. The proposed initial discovery-stage allowance is **AUD 37,500-62,500 including contingency**; the non-certified product funding envelope is **AUD 600,000-1,018,750**. These are estimates for review, not an approved funding commitment. No certified-product launch date or sales forecast is approved by this draft.
