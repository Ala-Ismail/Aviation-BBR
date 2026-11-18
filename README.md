# Aviation BBR

A technology-led assessment of whether the BBR FPGA/VHDL event recorder could support continuous recording of flight instruments, sensors and aircraft-system data.

## Assessments

1. **[Technology assessment](Aviation_BBR_technology_assessment.md)** is the technical reference. It documents the private BBR baseline, aircraft and approval reference cases, retention and storage calculations, FPGA and microcontroller alternatives, and the evidence each option would need.
2. **[Business assessment](Aviation_BBR_business_assessment.md)** uses those capability and integration assumptions to assess candidate customers, Australian market size, illustrative pricing, and development costs.
3. **[Feasibility study](Aviation_BBR_feasibility_study.md)** combines the technology and commercial evidence to compare a bench demonstrator, a supplemental recorder, and an approved flight data recorder.

## Evidence status

The capacity model gives about 27.3 hours at 175,000 bytes/s if 16 GiB is available to the recording stream. FPGA fit, sustained media service, power-loss recovery, crash protection, aircraft installation and commercial demand remain open. This public repository contains the studies and reference diagrams. The existing event-recorder implementation and its historical test reports are in the [private BBR repository](https://github.com/Ala-Ismail/BBR).

The MIT license covers the contents of this public repository. Access to and reuse of private BBR materials require separate authorization. [MIT License](LICENSE)

## Website

Run `npm ci` and `npm run build` to render the assessment pages from Markdown. Open `dist/index.html` for a local preview. The Vercel configuration uses the same build and serves `dist/`.
