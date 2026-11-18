# Aviation BBR business assessment

[Documentation index](README.md) ? [Technology assessment](Aviation_BBR_technology_assessment.md) ? [Feasibility study](Aviation_BBR_feasibility_study.md)

**Research baseline** ? 8 November 2026. Prices and sales scenarios are in USD. Development estimates are in AUD. Amounts exclude applicable taxes.

## 1. Commercial findings

The [technology assessment](Aviation_BBR_technology_assessment.md) identifies reusable elements of the private BBR event recorder and the gaps in extending them to continuous aviation instrument recording. Those gaps affect integration cost, hardware cost and customer support. The most accessible use cases to assess are bench evaluation and engineering data capture. Supplemental airborne logging depends on aircraft-specific interfaces and installation permissions. An approved flight data recorder (FDR) has distinct evidence and cost requirements.

The illustrative direct-sales case uses **USD 3,500** per unit and **USD 1,400** in recurring unit costs. At those assumptions, 50 units over 36 months yield **USD 175,000** revenue and **USD 105,000** contribution before fixed costs. The separate bottom-up development scenario is **AUD 600,000?1,018,750** through controlled release. The domestic hardware case offers limited scale, and a full investment-return model would require a common currency, dated cash flows and evidence for sales, integration margin and support costs.

Customer demand, paid evaluations, supplier quotes, installation costs and production yield remain unverified. The study uses three prospective partners as a discovery threshold and 5?10 pilot units as a cost-model input.

## 2. Customer needs and alternatives

Aircraft developers and researchers need interpretable instrument data with enough context to reconstruct test events, diagnose missing samples and recover recordings after interruptions. Existing avionics logging and general-purpose data acquisition equipment are alternatives. The commercial question is whether better recovery, accessible exports or easier integration would justify a dedicated recorder for a specific use case.

The capability and cost assumptions come from the [technology assessment](Aviation_BBR_technology_assessment.md#6-storage-and-bandwidth-sizing). A useful evaluation would measure source compatibility, timestamp quality, end-to-end retention, recoverable tail loss, independent decoding and engineering hours per integration. The 25-hour and FPGA/F-RAM/NAND reference scenario provides a common basis for estimating effort. A simpler bench or supplemental recorder could have a different retention target or hardware partition once a use case is established.

## 3. Candidate customers and addressable market

| Customer segment | Candidate use | Evidence to collect |
|---|---|---|
| Aircraft and avionics development teams | Bench integration and instrument-data capture during development | Required interfaces, existing logging gaps and budget for an evaluation |
| Universities and aerospace research groups | Repeatable data collection and engineering analysis | Export formats, purchase budget and support needs |
| Experimental aircraft developers | Supplemental instrument logging where the installation and use are permitted | Installation responsibilities, aircraft compatibility and willingness to pay |
| Equipment manufacturers | Recorder integration into their own development platforms | Recurring volume and scope for paid integration |

Bench and research use offers a way to measure integration effort and recording performance. An airborne evaluation would also require the applicable installation and operating permissions.

Possible differentiators include configurable acquisition, explicit quality and recovery behavior, and accessible engineering readout. Their value depends on measurable improvements over the customer?s existing workflow.

Section 3.1 estimates the Australian installed-base opportunity using a published fleet count and assumed serviceability. Buyer interviews and qualified opportunities would provide a separate basis for forecasting demand.

### 3.1. TMV analysis: total market value

**Definition and scope:** Here TMV means **Total Market Value**: the theoretical hardware sales value of a defined aircraft population at the modeled unit price. The starting scope is Australian registered amateur-built, single-engine piston aeroplanes. This is a deliberately narrow beachhead aligned with the supplemental experimental-aircraft scenario. Research benches and OEM development platforms remain target customers but are excluded from the numerical model because no verified customer count is available. TMV is neither company valuation nor annual recorder-industry revenue.

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

The serviceable obtainable market (SOM) models hypothetical sales constrained by direct customer acquisition and delivery capacity. Account counts and units per account are assumptions. A developer or integrator could buy for multiple aircraft. The model counts each aircraft installation once and excludes bench-only sales.

| Scenario | Purchasing accounts | Average units per account | Units over 36 months | Hardware revenue (USD) | Share of base SAM (311 units) |
|---|---:|---:|---:|---:|---:|
| Low | 10 | 2.5 | 25 | $87,500 | 8.0% |
| Base | 20 | 2.5 | 50 | $175,000 | 16.1% |
| Stretch | 40 | 2.5 | 100 | $350,000 | 32.2% |

Even the base case requires a meaningful share of a small market. The stretch case depends on distribution, customer references, manufacturing capacity and support coverage. Orders would provide evidence for using it in a funding model. The three prospective partners in section 1 are a discovery threshold. Pilot deliveries would count toward the 36-month scenario only if they qualify as sales delivered during that period.

**Stock versus annual demand:** If, purely as a sensitivity test, 5-10% of the 311-aircraft base SAM purchases each year, the result is approximately **15-31 units per year**, rounded down, or **USD 52,500-108,500 annual hardware revenue** at the target price. This assumed purchase rate includes no repeat purchase or fleet growth and cannot be applied indefinitely to an unchanged installed base. At the section 6 contribution assumption of USD 2,100 per unit, that volume yields only **USD 31,500-65,100 per year before fixed costs**. There is no evidence yet that this purchase rate can be achieved.

**Commercial implication:** The narrow Australian amateur-built segment alone does not currently justify the AUD 600,000-1,018,750 development envelope. A stronger case needs paid OEM/research integrations, a separately measured export opportunity, lower development expenditure, or a combination supported by customer evidence. USD revenues above must not be compared directly with AUD development expenditure without a dated exchange-rate assumption. Section 7's 25/100/250-unit scenarios remain general scale illustrations, not annual Australian-market forecasts; they are not additive to this SOM.

#### Evidence that could change the market estimate

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

The USD 3,500 modeled price is a pricing hypothesis to test with prospective customers. It is not derived from verified BBR manufacturing costs or demonstrated willingness to pay.

## 5. Offering and price scenarios

| Offering scenario | Illustrative price | Scope and conditions |
|---|---|---|
| Engineering evaluation kit | $1,500-3,000 per kit | Bench hardware, example data, basic download tools and limited evaluation support; configuration may be reduced from the enclosed product |
| Standard development recorder | **$3,500 target per unit**; planning range $3,000-6,000 | Enclosed and tested non-certified recorder, documented standard interfaces, readout utility and defined support |
| Customer integration | Separate statement of work | Source interfaces, parameter mapping, adapters, test procedures and acceptance evidence |
| Extended support | Separately quoted annual agreement | Defined response times, maintenance releases and compatibility assistance |
| Future approved FDR | $25,000-45,000 per unit as an exploratory target | Subject to approval route, crash-survival evidence, production costs, market validation and partner support; not currently available |

Standard hardware pricing excludes sensors, aircraft wiring, installation, custom interfaces, qualification, approval work and bespoke analysis. The standard interface set and included support allowance must be fixed before accepting production orders.

The revenue model assumes direct sales. A distributor case would need separate allowances for channel discounts, manufacturing yield, volume pricing and support.

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

Interface scope, storage design and included support are the main uncertainties in the cost ceiling. The price and contribution sensitivity above shows how a higher recurring cost would affect the case.

## 7. Sales and cost-recovery scenarios

These scenarios illustrate scale at $3,500 revenue and $1,400 recurring cost per unit. They are not an annual forecast, sales pipeline or evidence of demand. Integration and support-contract revenue are excluded because delivery effort and margins are not yet estimated.

| Units sold in a planning period | Hardware revenue | Recurring costs | Contribution before fixed costs |
|---|---:|---:|---:|
| 25 | $87,500 | $35,000 | $52,500 |
| 100 | $350,000 | $140,000 | $210,000 |
| 250 | $875,000 | $350,000 | $525,000 |

An illustrative **USD 300,000** in fixed development expenditure would require **143 units** at USD 2,100 contribution per unit. Company break-even would also depend on operating overhead, selling costs, cash timing and further development.

Section 8.1 provides an initial AUD development estimate by stage. Before seeking investment or committing delivery dates, replace its allowances with a bottom-up budget for engineering effort, prototype hardware, test equipment, third-party testing, tooling, software, insurance and working capital. Estimate cash required to buy and build pilot units before customer payments arrive. Price and fund crash protection and aviation approval separately.

Paid discovery and milestone-based development are possible revenue models for customer-specific work. Their cash flows would depend on deliverables, payment terms, acceptance criteria and cancellation terms.

## 8. Illustrative work packages and cost model

The timing columns show a sequencing scenario measured from a hypothetical funded start with an available team. Requirements, staffing and procurement lead times would determine the actual duration.

| Work package | Illustrative timing | Evidence or output |
|---|---|---|
| Customer discovery and requirements | Months 0-2 | At least 10 customer interviews; three qualified development partners; agreed interfaces and acceptance criteria; willingness-to-pay evidence |
| Architecture and bench demonstrator | Months 2-5 | Versioned format, acquisition model, readout prototype and initial BOM; simulation of rollover, faults and power-loss recovery |
| Integrated prototype | Months 5-9 | Prototype hardware, full-retention and cyclic-overwrite tests, measured storage behavior, timing evidence and independent decoding |
| Paid pilot and production preparation | Months 9-12 | Pilot commitments and acceptance results; verified build/test process, costed supply chain and defined support terms |
| Controlled commercial release | After pilot acceptance | Released configuration, production acceptance tests, published limitations and a funded support process |
| Approved FDR feasibility | Separate project decision | Identified aircraft/customer, approval basis, qualified partners, costed crash-survival and assurance plan, funding and commercial justification |

The 12-month case assumes overlapping technical work and timely procurement. Measured recovery, retention, interface compatibility and manufacturing results determine whether the scenario remains credible.

### 8.1. AUD development cost estimate by stage

**Estimate basis, 8 November 2026.** The model yields **AUD 600,000?1,018,750** through controlled release of a non-certified development recorder, including 25% contingency. The midpoint is approximately **AUD 810,000**. A separate approved-FDR feasibility work package is estimated at **AUD 62,500?125,000**. Formal qualification and approval remain uncosted.

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

Contingency is calculated as 25% of each stage's labour plus other direct costs. These totals include no GST, financing costs, large production inventory, full aircraft installation/modification programme, flight-test aircraft hire, or formal crash-survival and aviation qualification campaign. Prototype-component and equipment procurement allowances include estimated inbound freight. Overseas purchases need exchange-rate allowances when supplier quotes are obtained.

**Future approved-FDR development and qualification remain uncosted.** Feasibility must establish the target assurance level, equipment and installation approval routes, crash-protected memory approach, independent verification, accredited testing and retest exposure before a credible programme budget can be presented. The optional feasibility allowance is not an estimate of certification cost and does not imply that approval can be completed within the non-certified product budget.

Section 7 uses an illustrative **USD 300,000** expense for the unit recovery calculation. A combined return model would use dated cash flows and a common currency for development costs and revenues.

## 9. Customer and pilot evidence

A product brief, interface questionnaire and representative instrument-data demonstration would support interviews with engineering buyers. Their existing logging methods, integration costs, interfaces, data-loss tolerance and purchasing process would provide the comparison baseline.

Three comparable evaluations could test whether a common configuration is viable. Scoping custom adapters separately would show how much integration is repeatable. Pilot evidence would include sustained recording, usable exports, timestamp and quality behavior, and measured recovery after interruptions.

Interview-to-pilot conversion, engineering hours per integration, recurring unit cost, production yield and support hours would show whether the modeled price and contribution are achievable.

## 10. Licensing and reuse dependencies

The public [Aviation-BBR repository](https://github.com/Ala-Ismail/Aviation-BBR) contains MIT-licensed material. The private [BBR baseline](https://github.com/Ala-Ismail/BBR) requires authorized access. Publication of this assessment does not grant access to or change the license of the private repository.

Revenue should come from delivered hardware, tested configurations, integration and support. Do not base the business case on exclusive access to material already published under MIT. Before shipping a product, establish the rights to every reused design, HDL block, software component and vendor IP, and define which deliverables will be public, private or supplied under customer contracts.

Authorized access and reuse rights are dependencies for any option that uses private BBR implementation material.

## 11. Commercial risks and evidence

| Risk | Effect | Evidence or scenario to assess |
|---|---|---|
| Existing avionics logging meets customer needs | Weak willingness to pay | Validate specific unmet requirements before hardware investment |
| Too many bespoke interfaces | Integration consumes hardware margin | Publish a standard configuration; charge separately for custom engineering |
| NAND, ECC or recovery complexity | Higher cost and delayed release | Prototype the storage path early and verify interruption behavior |
| Component availability or low production yield | Cost ceiling is missed | Obtain supplier quotes and pilot-build yield data before fixing production prices |
| Buyers expect approved crash-protected recording | Product is unsuitable for the intended purchase | State product status and operating limits in quotations and specifications |
| Support and liability costs exceed allowances | Lower margin and higher cash needs | Define support scope, review insurance needs and measure pilot support effort |
| Approval programme begins before demand is proven | Capital required exceeds available funding | Make approval a separately funded, customer-backed decision |

## 12. Commercial uncertainties

The strongest evidence for a bench product would be a quoted configuration, a measured integration effort and buyers willing to pay for evaluation against a specific use case. A repeatable airborne offering would also require installation and support costs from representative aircraft. The Australian market model excludes research and OEM systems, service revenue and exports until those segments have independently sourced inputs.

The [feasibility study](Aviation_BBR_feasibility_study.md) combines these commercial uncertainties with the technology evidence and identifies what would change the assessment for each option.
